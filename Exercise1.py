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


def create_csv(data):
    """
    Creates and returns a path for a CSV file named 'data.csv' from a given data.
    The function checks if the input is a valid nested array before creating the CSV file.
    If the input is invalid or empty, a message is printed, and no CSV file is created.

    Parameters:
    - data(list) : A nested list where the first element contains headers and the remaining elements contain data rows.

    Returns:
    - str: The path to the generated CSV file .
    """
    try:
        if not data or not all(isinstance(innerlist, list) for innerlist in data):
            print("Invalid data , please provide non empty nested array")
            return "File cannot be created "
        with open("data.csv", "w") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)
    except Exception as e:
        print(f"An error occurred : {e}")
        return "File cannot be created"
    return os.path.abspath("data.csv")


nested_list = [
    ["empid", "name", "address"],
    [1, "John", "HYD"],
    [2, "Bob", "AP"],
]
csv_path = create_csv(nested_list)
print(csv_path)
