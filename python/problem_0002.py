# copilot: disable

# Daily Coding Problem: Problem #2 [Hard]

# Given an array of integers, return a new array such that each element
# at index i of the new array is the product of all the numbers in the 
# original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected 
# output would be [120, 60, 40, 30, 24]. If our input was 
# [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

def integers_to_products(numbers):
    products = list()
    i=0
    for num in numbers:
        product = 1
        integers = numbers.copy()
        integers.pop(i)
        for x in integers:
            product = product * x
        products.append(product)
        i = i + 1
    return products

if __name__ == "__main__":
    numbers_input = input("Enter integers seperated by spaces: ")
    numbers = [int(x.strip()) for x in numbers_input.split(" ")]
    
    result = integers_to_products(numbers)
    print(f"Result: {result}")