# Write a python program to find even numbers from 1 to 200 using function.
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
