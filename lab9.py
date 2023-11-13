import pandas as pd

import matplotlib.pyplot as plt

equipment_df = pd.read_csv('russia_losses_equipment.csv')
corrections_df = pd.read_csv('russia_losses_equipment_correction.csv')
personnel_df = pd.read_csv('russia_losses_personnel.csv')

equipment_df.drop_duplicates(inplace=True)
corrections_df.drop_duplicates(inplace=True)
personnel_df.drop_duplicates(inplace=True)

df_cleaned = equipment_df.dropna(inplace=True)
df_cleaned = corrections_df.dropna(inplace=True)
df_cleaned = personnel_df.dropna(inplace=True)

merged_df = pd.merge(equipment_df,corrections_df, how='inner', on='date')

equipment_df.describe()
unique_counts_equipment  = equipment_df.nunique()
min_value_equip = corrections_df.min()
max_value_equip = corrections_df.max()
display(min_value_equip, max_value_equip, unique_counts_equipment)

plt.figure(figsize=(10,5))
plt.plot(equipment_df['date'], equipment_df['aircraft'])
plt.xlabel('Дата')
plt.ylabel('Кількість втраченої техніки')
plt.title('Динаміка втрат літаків')
plt.show()