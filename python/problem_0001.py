# copilot: disable

# Daily Coding Problem: Problem #1 [Easy]

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

def two_nums_sum_k(numbers, k):
    read_nums = list()
    for num in numbers:
        if k - num in read_nums:
            return True
        read_nums.append(num)
    return False

if __name__ == "__main__":
    numbers_input = input("Enter numbers seperated by spaces: ")
    numbers = [int(x.strip()) for x in numbers_input.split(" ")]
    
    k = int(input("Enter the target sum k: "))

    result = two_nums_sum_k(numbers, k)
    print(f"Result: {result}")