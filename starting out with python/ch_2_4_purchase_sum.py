tax = 0.07
net_value1 = int(input("Enter the net value of purchased item 1: "))
net_value2 = int(input("Enter the net value of purchased item 2: "))
net_value3 = int(input("Enter the net value of purchased item 3: "))
net_value4 = int(input("Enter the net value of purchased item 4: "))
net_value5 = int(input("Enter the net value of purchased item 5: "))
tax_value = (net_value1 + net_value2 + net_value3 + net_value4 + net_value5) * tax
gross_value = (net_value1 + net_value2 + net_value3 + net_value4 + net_value5) + tax_value
print("You paid {} in tax and the gross value of your purchases is {}".format(tax_value, gross_value))
