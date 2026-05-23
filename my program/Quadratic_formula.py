import math
print("\n---Quadratic Equation Solver---")

# Quadratic eqaution form ax**2 + bx + c = 0

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

D = b**2 - (4*a*c) # D == discriminant
print(f"Discriminant: {D}")
if D > 0:
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D))/(2*a)
else:
    print("No real roots")
print(f"The value of x1: {x1}")
print(f"The value of x2: {x2}")

# Sum and product of roots

sum = -b/a
product = c/a

print(f"Sum of roots: {sum}")
print(f"Product of root: {product}")