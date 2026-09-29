# def calculate_total(quantity, price):
#     return quantity * price


# gasoline_total = calculate_total(120, 4.25)
# diesel_total = calculate_total(80, 4.80)

# print(gasoline_total)
# print(diesel_total)

sales = [
    {"product": "Gasoline", "quantity": 120, "price": 4.25},
    {"product": "Diesel", "quantity": 80, "price": 4.80},
    {"product": "Oil", "quantity": 25, "price": 12.99},
    {"product": "Gasoline", "quantity": 150, "price": 4.25}
]

def calculate_total(quantity, price):
    return quantity * price
total_sales = 0
for sale in sales:
    if sale["price"] > 4.50:
        total = calculate_total(sale["quantity"], sale["price"])
        total_sales += total
        print(total_sales)