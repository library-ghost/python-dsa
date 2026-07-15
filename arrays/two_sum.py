# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def two_sum(numbers, target_sum):
  previous_nums = {}

  for index, num in enumerate(numbers):
    complement = target_sum - num

    if complement in previous_nums:
      return (previous_nums[complement], index)

    previous_nums[num] = index
        
#examples
print(two_sum([3, 2, 5, 4, 1], 8)) # -> (0, 2)

print(two_sum([4, 7, 9, 2, 5, 1], 5)) # -> (0, 5)

print(two_sum([4, 7, 9, 2, 5, 1], 3)) # -> (3, 5)

# time: O(n)
# space: O(n)
