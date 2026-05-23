import math 
print("\n---Area of Circle⚪ program---")

r = float(input("Enter radius of circle: ")) # r stand for radius of circle
unit = input("Enter unit: ")

area = math.pi * (r ** 2)
c = 2 * math.pi * r # c stand for circumference of the circle
print(f"Area of circle: {round(area, 2)}{unit}^2")
print(f"Circumference of circle: {round(c, 2)}{unit}")