import os

import csv

csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')


with open(csvpath, newline='') as csvfile:

            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
            
                total_months = sum(1 for row in csvreader)
                print(total_months)