# Geometry Calculator
# Programmed by Mayon & Varadhan
# GitHub: https://github.com/mayonpatel/Mayon-Varadhans-Programming

import math  # Import the math module for pi

# Get the shape from the user
shape = input("[CASE SENSITIVE] What shape do you want to calculate the area of? (Circle/Triangle/Square/Rectangle)? ")

# Calculate the area based on the shape
if shape == "Circle":
    # Get the radius from the user
    radius = float(input("What is the radius of the circle: "))
    # Calculate the area of the circle
    circle_area = math.pi * radius ** 2
    # Print the area of the circle
    print(f"The area of the circle is {circle_area}!")
elif shape == "Triangle":
    # Get the base and height from the user
    base = float(input("What is the base of the triangle: "))
    height = float(input("What is the height of the triangle: "))
    # Calculate the area of the triangle
    triangle_area = base * height / 2
    # Print the area of the triangle
    print(f"The area of the triangle is {triangle_area}!")
elif shape == "Square":
    # Get the side length from the user
    side_length = float(input("What is side length of the square? "))
    # Calculate the area of the square
    square_area = side_length * side_length
    # Print the area of the square
    print(f"The area of the square is {square_area}")
elif shape == "Rectangle":
    # Get the length and width from the user
    length = float(input("What is length of the rectangle? "))
    width = float(input("What is width of the rectangle? "))
    # Calculate the area of the rectangle
    rectangle_area = length * width
    # Print the area of the rectangle
    print(f"The area of the rectangle is {rectangle_area}")
else:
    # Print an error message if the input is invalid
    print("Invalid input!")
