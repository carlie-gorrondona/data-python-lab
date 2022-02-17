open_file = open('CupcakeInvoices.csv')

# for item in open_file:
#     print(item)

# for row in open_file:
#     item = row.split(',')
#     print(item[2])

# for row in open_file:
#     item = row.split(',')
#     quantity = float(item[3])
#     price = float(item[4])
#     print(price * quantity)

total = 0

for row in open_file:
    item = row.split(',')
    quantity = float(item[3])
    price = float(item[4])
    total = total + (quantity * price)

total_two_decimals = "{:.2f}".format(total)

print(total_two_decimals)

open_file.close()
