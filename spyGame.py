# Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums):

    zeroZeroSeven = 0

    for num in nums:
        if zeroZeroSeven < 2:
            if num == 0: 
                zeroZeroSeven += 1
        elif zeroZeroSeven == 2:
            if num == 7:
                zeroZeroSeven = 0
                return True
    return False

# Check
result1 = spy_game([1,2,4,0,0,7,5])
print(result1) # --> True
result2 = spy_game([1,0,2,4,0,5,7])
print(result2) # --> True
result3 = spy_game([1,7,2,0,4,5,0])
print(result3) # --> False