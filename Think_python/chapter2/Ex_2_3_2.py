price_per_book = 24.95
discount =0.60
quantity = 60
discount_price = price_per_book*discount *quantity
shipping = 0.75*(quantity-1)+3
total_price = discount_price+shipping 
print("discount_price",discount_price) # 898.1999999999999
print("shipping",shipping) # 47.25
print("total_price",total_price) # 945.4499999999999