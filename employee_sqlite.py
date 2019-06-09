#! usr/bin/env python3

import csv
import sqlite3

# Create the database
connection = sqlite3.connect('/Users/AaronKo/w1d5/employees.db')
cursor = connection.cursor()

# Create the table
cursor.execute("DROP TABLE IF EXISTS employee;")
cursor.execute('''CREATE TABLE employee(User varchar, cellphone varchar, 
                homephone varchar, workphone varchar, email varchar, country varchar);''')
connection.commit()

# Load the SFC file into CSV reader
with open("/Users/AaronKo/w1d5/employees.csv", "r") as csvfile:
    rows = csv.reader(csvfile)

# Iterate through the csv reader, inserting values into the database
    for row in rows:
        cursor.execute("INSERT INTO employee VALUES (?, ?, ?, ?, ?, ?);", row)

# Commit changes and close connection
connection.commit()
connection.close()
