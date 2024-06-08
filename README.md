Job Tasks:
1. Write a python program to find the largest of three numbers.

```py
def largest_of_three(a, b, c):
    try:
        a, b, c = float(a), float(b), float(c)
        if a >= b and a >= c:
            return a
        elif b >= a and b >= c:
            return b
        else:
            return c
    except ValueError:
        return "Invalid input. Please enter numeric values."

# Example usage
a, b, c = input("A= "), input("B= ") ,input("C= ")
print(largest_of_three(a, b, c))
```

2. Write a python program to calculate the area of triangle.

```py
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
```

3. Write a python program to find even numbers from 1 to 200 using function.

```py
def even_numbers(start, end):
    try:
        start , end = int(start) , int(end)
        list_even_numbers =  []
        for i in range(start, end + 1):
            if i % 2 == 0:
                list_even_numbers.append(i)
        return list_even_numbers
    except ValueError:
        return "Invalid input. Please enter numeric values."
    
# Example usage
print(even_numbers(0, 200))
```

4. Write a python program to find the area of circle and area of rectangle using function.

```py
import math

def area_of_circle(radius):
    try:
        radius = float(radius)
        return math.pi * radius * radius
    except ValueError:
        return "Invalid input. Please enter a numeric value for radius."

# Example usage
radius = input("Radius= ")
print(area_of_circle(radius))

def area_of_rectangle(length, width):
    try:
        length, width = float(length), float(width)
        return length * width
    except ValueError:
        return "Invalid input. Please enter numeric values for length and width."

# Example usage
length, width = input("length= ") , input("Width= ")
print(area_of_rectangle(length, width))
```

5. Write a python program to find out which word is vowel or consonant using function.

```py
def is_vowel(char):
    vowels = 'aeiouAEIOU'
    if char in vowels:
        return True
    return False

def is_vowel_or_consonant(word):
    try:
        if not isinstance(word, str):
            raise ValueError("Input must be a string.")
        result = {}
        for char in word:
            if char.isalpha():
                result[char] = 'Vowel' if is_vowel(char) else 'Consonant'
        return result
    except ValueError as ve:
        return str(ve)

# Example usage
value = input("Input: ")
print(is_vowel_or_consonant(value))
```

6. Write a python program to find grade of a student in diploma Curriculum.

```py
def find_grade_letter(marks):
    try:
        marks = float(marks)
        if marks < 0 or marks > 100:
            return "Marks should be between 0 and 100."
        if marks >= 80:
            return 'A+'
        elif marks >= 75:
            return 'A'
        elif marks >= 70:
            return 'A-'
        elif marks >= 65:
            return 'B+'
        elif marks >= 60:
            return 'B'
        elif marks >= 55:
            return 'B-'
        elif marks >= 50:
            return 'C+'
        elif marks >= 45:
            return 'C'
        elif marks >= 40:
            return 'D'
        else:
            return 'F'
    except ValueError:
        return "Invalid input. Please enter numeric values."

# Example usage
mark = input("Mark = ")
print(find_grade_letter(mark))
```

7. Write a python program to find the factorial of a number using function.

```py
def factorial(n):
    try:
        n = int(n)
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    except ValueError as ve:
        return str(ve)

# Example usage
n = input("n = ")
print(factorial(n))
```

8. Write a python program to display the multiplication table

```py
# Write a python program to display the multiplication table.

def multiplication_table(n):
    try:
        n = int(n)
        for i in range(1, 11):
            print(f"{n} x {i} = {n*i}")
    except ValueError:
        print("Invalid input. Please enter an integer.")


# Example usage
n = input("n = ")
multiplication_table(n)
```

9. Write a python function that takes a number as input and returns whether it's a prime number or not.

```py
def is_prime(n):
    try:
        n = int(n)
        if n <= 1:
            return False
        elif n == 2:
            return True
        else: 
            for i in range(2, n):
                if(n % i == 0):
                    return False
            return True
    except ValueError:
        return "Invalid input. Please enter an integer."


# Example usage
n = input("n = ")
print(is_prime(n))
```

10. Write python program to swap two numbers using function.

```py
def swap(a, b):
    try:
        a, b = float(a), float(b)
        return b, a
    except ValueError:
        return "Invalid input. Please enter numeric values."

# Example usage
a, b = input("a = "), input("b = ") 
print(swap(a, b))
```