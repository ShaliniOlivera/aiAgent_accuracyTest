import os
import json

# Set up paths
base_path = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(base_path, "inventory", "inventory.json")

# Check if the inventory.json file exists before loading
if not os.path.exists(json_path):
    raise FileNotFoundError(f"\u274c Inventory file not found: {json_path}")

# Load inventory.json
with open(json_path, "r") as file:
    product_data = json.load(file)

# Define expected results dictionary
expected_results = {
    "accessories": ", ".join([
        product["name"] for product in product_data
        if product.get("category") == "Accessories" and product.get("stock", 0) > 0
    ]) or "No accessories found",
    
    "electronics": ", ".join([
        product["name"] for product in product_data
        if product.get("category") == "Electronics" and product.get("stock", 0) > 0
    ]) or "No electronics found",

    "all": ", ".join([
        f"{product['name']} ({product['price']})" for product in product_data
        if product.get("stock", 0) > 0
    ]) or "No products found"

}
