def triangle_type(a, b, c):
if a == b == c:
    return "Equilateral"
elif a == b or b == c or a == c:
    return "Isosceles"
else:
    return "Scalene"
side1 = float(input("Enter length of first side: "))
side2 = float(input("Enter length of second side: "))
side3 = float(input("Enter length of third side: "))
print(f"The triangle is {triangle_type(side1, side2, side3)})