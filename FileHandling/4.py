#read a csv file and print only the names

import csv

try:
    with open('qst4.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  
                print(row[0]) # Assuming the name is in the first column
except FileNotFoundError:
    print("The file was not found.")