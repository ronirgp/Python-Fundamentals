sales = [
    {"product": "Gasoline", "quantity": 120, "price": 4.25},
    {"product": "Diesel", "quantity": 80, "price": 4.80},
    {"product": "Oil", "quantity": 25, "price": 12.99},
    {"product": "Gasoline", "quantity": 150, "price": 4.25}
    
]

total_sales = 0

for sale in sales:
    if sale["product"] == "Gasoline":
        total = sale["quantity"] * sale["price"]
        total_sales += total

print(total_sales)



# for sale in sales:
#     if  sale["quantity"] > 100:
#         total = sale["quantity"] * sale["price"]
#         total_sales += total

# for sale in sales:
#     if sale["price"] > 4.50:
#         total = sale["quantity"] * sale["price"]
#         total_sales += total
#         print(total_sales)
        
        
        

