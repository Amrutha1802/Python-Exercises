# ex-3 Read this JSON (https://dummyjson.com/products)
# and convert json to CSV of products
# id, title, description ..... images
# images is an array in the JSON.
# Figure out a way to handle nested data in CSVs

from urllib.request import urlopen 
import csv
import json

def json_to_csv(url):
    response = urlopen(url) 
    json_data = json.loads(response.read()) 
    products_data=json_data.get("products")
    max_images = max(len(product["images"]) for product in products_data)
    header = list([key for key in products_data[0].keys() if "image" not in key]) + [f"images/{i}" for i in range(max_images)]
    with open('products.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        for product in products_data:
            row = {f"images/{i}": product["images"][i] if i < len(product["images"]) else "" for i in range(max_images)}
            row.update({key: value for key, value in product.items() if key != "images"})
            writer.writerow(row)


url = "https://dummyjson.com/products"
json_to_csv(url)
