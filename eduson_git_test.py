ticket_price = 260
discount = 0.75
price = 0

for i in range(9):
    count = i + 1
    if count % 3 == 0:
        price += ticket_price * discount
        print(price, ticket_price * discount, count)
    else:
        price += ticket_price
        print(price, ticket_price, count)

print(price)