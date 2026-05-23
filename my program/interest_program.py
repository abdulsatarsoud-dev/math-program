import math
print("\n---Interest program---")

p = int(input("Enter amount borrowed(principal): ")) # p stand for principal
r = int(input("Enter rate: ")) # r stand for rate
t = int(input("Enter time (year): ")) # t stand for time 

i = (p * r * t) / 100   # i stand for interest

print(f"The interest: {i}")