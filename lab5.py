import csv

class Database:
  def __init__(self):
    self.fieldnames = ['brand', 'model', 'year', 'color']
    self.filename = 'database_cars.csv'

    with open(self.filename, 'w', newline='') as cvs_file:
      self.writer = csv.DictWriter(cvs_file, fieldnames=self.fieldnames)

      self.writer.writeheader()
  
  def add_record(self, brand, model, year, color):
    record = {
      "brand": brand,
      "model": model,
      "year": year,
      "color": color,
    }

    with open(self.filename, 'a', newline='') as cvs_file:
      writer = csv.DictWriter(cvs_file, fieldnames=self.fieldnames)
      writer.writerow(record)

  def read_records(self):
    with open(self.filename, 'r') as csv_file:
      csv_reader = csv.DictReader(csv_file)
      line_count = 0
      for row in csv_reader:
        if line_count == 0:
          print(f'Column names are {", ".join(row)}')
          line_count += 1
        print(f'\t{row["brand"]} have model {row["model"]} is year {row["year"]} and have color {row["color"]}')
        line_count += 1

  def find_record(self, criterion):
    with open(self.filename, 'r') as csv_file:
      csv_reader = csv.DictReader(csv_file)
      for row in csv_reader:
        for fieldname in self.fieldnames:
          if criterion in row[fieldname]:
            print(f'{row["brand"]} have model {row["model"]} is year {row["year"]} and have color {row["color"]}')

  def delete_record(self, criterion): 
    records_to_keep = []

    with open(self.filename, 'r+') as csv_file:
      reader = csv.DictReader(csv_file)

      for row in reader:
        match = False
        for fieldname in self.fieldnames:
          if criterion in row[fieldname]:
            match = True
            break

        if not match:
          records_to_keep.append(row)

    with open(self.filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
        writer.writeheader()
        writer.writerows(records_to_keep)
  
  def update_record(self, field_to_update, criteria, updated_value):
    records_to_update = []

    with open(self.filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            if row[field_to_update] == criteria:
                row[field_to_update] = updated_value
            records_to_update.append(row)

    with open(self.filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
        writer.writeheader()
        writer.writerows(records_to_update)

  def get_statistic(self):
    with open(self.filename, 'r') as csv_file:
      reader = csv.DictReader(csv_file)

      average = 0
      count_record = 0
      for row in reader:
        average += int(row["year"])
        count_record += 1

      print(f"Average is year {int(average / count_record)}")

database = Database()
database.add_record("Tesla", "X", "2022", "Black")
database.add_record("BMW", "M3", "2015", "White")
database.delete_record("2022")
database.update_record("color", "Black", "White")
database.read_records()
database.get_statistic()