import math

question = input("What shape do you want to calculate the area of? [rectangle, circle, triangle]")

if question == "circle":
    r = float(input("What is the radius of your circle?[cm]"))

    circle_area = r + math.pi
    print("The area of your circle is:",circle_area, ("cm^2"))

if question == "rectangle":
    l = float(input("What is the length of your rectangle?[cm] "))
    w = float(input("What is the width of your rectangle?[cm]"))

    rectangle_area = l*w
    print("The area of your rectangle is:", rectangle_area, "cm^2")

if question == "triangle":
    b= float(input("What is the base of your triangle? [cm]"))
    h = float(input("What is the height of your triangle?[cm]"))

    triangle_area = b*h/2
    print("The area of your triangle is:", triangle_area, "cm^2")



