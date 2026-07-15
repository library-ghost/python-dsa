# Write a function, all_even, that takes in a list of numbers as an argument. The function should return a boolean indicating whether or not every element of the list is an even number.
# You can assume that the list is non-empty.

def all_even(numbers):
    for num in numbers:
        if num % 2 != 0:
            return False
    return True

# examples
print(all_even([4, 90, 68, 6, -2])) # -> True

print(all_even([14, 40, 36, 3])) # -> False

print(all_even([30, 24, 2048, 0, 12, 50])) # -> True