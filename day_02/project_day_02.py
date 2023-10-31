name_salesman = input("Type your name:_")
sold_salesman = int(input("Type your sales this month:_"))
tax = 13/100
commission = round(sold_salesman * tax, 2)

print(f"Hi {name_salesman}, your earnings this month was ${commission}")
