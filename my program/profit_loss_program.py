import math 
print("\n---Profit and Loss program---")

selling_price = int(input("Enter Selling price: ")) # S.P stand Selling Price
buying_price  = int(input("Enter Buying Price: "))

if selling_price > buying_price:
    profit = selling_price - buying_price 
    print(f"Profit: {profit}")
    percentage_profit = (profit/ buying_price) * 100 
    print(f"Percentage profit: {round(percentage_profit, 2)}%")
else:
    loss = buying_price - selling_price
    print(f"Loss: {loss}")
    percentage_loss = (loss/ buying_price) * 100
    print(f"Percentage loss: {round(percentage_loss, 2)}%")


