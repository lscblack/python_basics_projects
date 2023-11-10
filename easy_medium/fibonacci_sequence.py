# Write a Python program to generate the first n terms of the Fibonacci sequence.
nums = [0, 1]
for x in range(0, 8):
    nums.append(nums[x] + nums[x + 1])
print(nums)
# Or you can loop through the array print one by one like this un comment to see how it works
"""
for s in nums:
    print(s)
"""