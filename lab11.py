from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()

main_page_url = 'https://varta1.com.ua/archive/'

wait_time = 5

df = pd.DataFrame({'Date': [], 'Text': []})

def update_df(date, text):
    df.loc[len(df)] = {'Date': date, 'Text': '\n'.join(text)}
    df.to_csv('archives.csv', index=False)

def scrape_article(article_url, date):
    try:
        driver.get(article_url)
        main = driver.find_elements(By.CSS_SELECTOR, "main p")
        text = [p.text for p in main]
        update_df(date, text)
    except StaleElementReferenceException:
        pass

def scrape_date_page(date_url, date):
    try:
        driver.get(date_url)
        articles = driver.find_elements(By.CSS_SELECTOR, "article.post > a[href]")

        for article in articles:
            article_url = article.get_attribute('href')
            scrape_article(article_url, date)

    except NoSuchElementException:
        pass

dates_to_visit = [
    {'year': 2019, 'month': 6, 'day': 13},
    {'year': 2020, 'month': 6, 'day': 13},
    {'year': 2021, 'month': 6, 'day': 13},
    {'year': 2022, 'month': 6, 'day': 13},
    {'year': 2023, 'month': 6, 'day': 13},
]

for date_info in dates_to_visit:
    date_url = f'https://varta1.com.ua/archive/{date_info["year"]}-{date_info["month"]}-{date_info["day"]}/'
    scrape_date_page(date_url, f'{date_info["year"]}-{date_info["month"]}-{date_info["day"]}')

driver.quit()
