# Write a python program to calculate the area of triangle.
import math
def area_of_triangle(a, b, c):
    try:
        a, b, c = float(a), float(b), float(c)
        if(a + b > c and a + c > b and b + c > a):
            s = (a + b + c) / 2
            area = math.sqrt(s * (s-a) * (s-b) * (s-c))
            return area
        else:
            return "Invalid input. Triangle is not possible"
    except ValueError:
        return "Invalid input. Please enter numeric values."

# Example usage
a , b, c  = input("A= ") , input("B= ") , input("C= ")
print(area_of_triangle(a, b, c))
