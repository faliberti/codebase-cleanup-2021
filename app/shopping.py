import os
import datetime
from pandas import read_csv

# defining functions

def format_usd(my_price):
    """
    Formats a number as USD with a dollar sign and two decimals
    Paramaters: my_price is a number that is formated
    """
    return f"${my_price:,.2f}"

def lookup_product(product_id, all_products):
    """
    Paramaters :
        product_id (str)
        all_products (list of dict) each dict with an "id", "name", "department", "aisle", and "price" attribute
    """
    matching_products = [p for p in all_products if str(p["id"]) == str(product_id)]
    if any(matching_products):
        return matching_products[0]
    else:
        return None

# READ INVENTORY OF PRODUCTS

products_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
products_df = read_csv(products_filepath)
products = products_df.to_dict("records")

# CAPTURE PRODUCT SELECTIONS

selected_products = []
while True:
    selected_id = input("Please select a product identifier: ")
    if selected_id.upper() == "DONE":
        break
    else:
        matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
        if any(matching_products):
            selected_products.append(matching_products[0])
        else:
            print("OOPS, Couldn't find that product. Please try again.")

date = datetime.date.today()
time = datetime.datetime.now()

subtotal = sum([float(p["price"]) for p in selected_products])

# PRINT RECEIPT
checkout_datetime_format = str(date) + " " + str(time.strftime("%I:%M:%S %p"))
tax_rate = 0.0875
tax_amount = tax_rate * subtotal
total_amount = subtotal + tax_amount

receipt = ""
for p in selected_products:
    receipt += "SELECTED PRODUCT: " + p["name"] + "   " + format_usd(p["price"]) + "\n"
receipt += "---------\n"
receipt += f"SUBTOTAL: {format_usd(subtotal)}\n"
receipt += f"TAX: {format_usd(tax_amount)}\n"
receipt += f"TOTAL: {format_usd((total_amount))}\n"
receipt += "---------\n"
receipt += "THANK YOU! PLEASE COME AGAIN SOON!\n"
receipt += "---------\n"

print("---------")
print("CHECKOUT AT: " + checkout_datetime_format)
print("---------")
print(receipt)

# WRITE RECEIPT TO FILE

receipt_id = checkout_datetime_format
receipt_filepath = os.path.join(os.path.dirname(__file__), "..", "receipts", f"{receipt_id}.txt")

with open(receipt_filepath, "w") as receipt_file:
        receipt_file.write("------------------------------------------\n")
        receipt_file.write(receipt)