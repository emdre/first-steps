shares = 2000
purchase_price = 40
paid = shares * 40
commission_purchase = 0.03 * (shares * purchase_price)
sales_price = 42.75
commission_sales = 0.03 * (shares * sales_price)
earned = shares * sales_price
print(earned - paid - commission_sales - commission_purchase)
