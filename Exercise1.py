# ex-1 write a function that will take a nested array and return a csv path: data.csv
# The first element in the nested array are headers and the remaining elements are data
# [
# 	[“empid”, “name”, “address”],
# 	[1, “John”, “HYD”],
# 	[2, “Bob”, “AP”],
# ]
# data.csv

import csv
import os


def addData(employeeData):
    with open('data.csv', 'w', newline='') as file:
        headers=employeeData[0]
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(employeeData[1:])
    return os.path.abspath('data.csv')

print("path of file is "+ addData([
	["empid", "name", "address"],
	[1, "John", "HYD"],
	[2, "Bob", "AP"],
]))
