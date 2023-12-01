# ex-3 Read this JSON (https://dummyjson.com/products)
# and convert json to CSV of products
# id, title, description ..... images
# images is an array in the JSON.
# Figure out a way to handle nested data in CSVs

import requests
import csv


def json_to_csv(url):
    """
    Fetches JSON data from the specified URL and converts it to a CSV file.

    Parameters:
    - url (str): The URL containing JSON data.

    Output:
    - Creates a CSV file named 'products.csv' with product information.

    Example:
        url = "https://dummyjson.com/products"
        json_to_csv(url)
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        json_data = response.json()
        products_data = json_data.get("products")
        headers = list(products_data[0].keys())

        with open("products.csv", "w", newline="") as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=headers)
            csv_writer.writeheader()

            for product in products_data:
                product["images"] = " ".join(product.get("images", []))
                csv_writer.writerow(product)
        print("CSV file 'products.csv' created successfully.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from the URL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


url = "https://dummyjson.com/products"
json_to_csv(url)
