"""Triangle Classifier:
Write a program that classifies a triangle based on its side lengths.

Given three input values representing the lengths of the sides,

determine if the triangle is equilateral (all sides are equal),

isosceles (exactly two sides are equal), or scalene (no sides are equal).

Use an if-else statement to classify the triangle.
"""

side1 = int(input("enter the length of side one : "))
side2 = int(input("enter the length of side two : "))
side3 = int(input("enter the length of side three : "))
if side1 == side2 == side3:
    print("The triangle is equilateral")
elif side1==side2 or side2==side3 or side3==side1:
    print("the triangle is isoceles")
else:
    print("the triangle is scalene")


