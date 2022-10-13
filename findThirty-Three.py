# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
    for idx, num in enumerate(nums):
        # print(idx, num)
        # alternative solution
        # if nums[i:i+2] == [3,3]
        if idx > 0:
            result = (nums[idx-1] == 3 and num == 3)
    return result

# Check
result1 = has_33([1, 3, 3])
print(result1) # True
result2 = has_33([1, 3, 1, 3])
print(result2) # False
result3 = has_33([3, 1, 3])
print(result3) # False