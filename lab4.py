import time

events = [
  (476, "Fall of the Western Roman Empire"),
  (1066, "Norman Conquest of England"),
  (1492, "Christopher Columbus's first voyage to the Americas"),
  (1776, "United States Declaration of Independence"),
  (1789, "Start of the French Revolution"),
  (1865, "End of the American Civil War"),
  (1969, "Apollo 11 Moon landing"),
  (1989, "Fall of the Berlin Wall")
]

dictionaryOfYears = {}

yearsToVisit = [1492, 1776, 1969, 1989]

def timePortal():
  print("Now you will go on a trip at the times you specified")
  try:
    for year in yearsToVisit:
      if year in [event[0] for event in events]:
        event = [event[1] for event in events if event[0] == year][0]
        dictionaryOfYears[year] = event
        time.sleep(1)
        print(f"You are traveling in {year} with event {event}")
      else:
        raise (f"Event for year {year} not found")
  except:
    raise ValueError("Such year not found")

def addEvent(year, description):
  events.append((year, description))
  dictionaryOfYears[year] = description

def deleteEvent(year):
  dictionaryOfYears.pop(year)

def showDictionary():
  for year, desc in dictionaryOfYears.items():
    print(f"{year} - {desc}")

def showEvents():
  for year, desc in events:
    print(f"{year} - {desc}")

while True:
  print("1. Add event\n2. Show events\n3. Delete event\n4. Portal\n5. Show Dictionary\n6. Exit")
  choice = int(input("Enter your choice: "))

  if choice == 1:
    year = int(input("Enter year: "))
    desc = input("Enter description of event: ")
    addEvent(year, desc)
  elif choice == 2:
    showEvents()
  elif choice == 3:
    try:
      year = int(input("Enter deleted year of event: "))
      deleteEvent(year)
    except ValueError:
      raise ValueError("No such year")
  elif choice == 4:
    timePortal()
  elif choice == 5:
    showDictionary()
  elif choice == 6:
    break