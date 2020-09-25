import os
import csv

csv_path = os.path.join("..", "Resources", "budget_data.csv")

# Open and read csv
with open(csv_path, 'r') as revenue_file:
    csv_reader = csv.reader(revenue_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(revenue_file)
    print(f"Header: {csv_header}")


    months = []
   # Total number of months included in the dataset
    rows = []
    for rows in csv_reader:
        months.append(rows[0])

    months = [rows for rows in csv_reader]
    
    print(months)


    
