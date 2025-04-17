# Add Python code to seperate odd and even number

def separate_odd_even():
    numbers = [1, 2, 3, 4, 5, 6,7, 8, 9, 10]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    even_numbers = [num for num in numbers if num % 2 == 0]
    return odd_numbers, even_numbers
# Call the function to get the result
odd_numbers, even_numbers = separate_odd_even()
print("Odd numbers: ", odd_numbers)
print("Even numbers: ", even_numbers)
