# Write a function that returns the lesser of two given numbers if both numbers are even, 
# but returns the greater if one or both numbers are odd

def lesser_of_two_evens(a, b):
    both_evens = (a % 2 == 0) and (b % 2 == 0)
    odds_found = (a % 2 != 0) or (b % 2 != 0)
    if (odds_found):
        # print('odds_found')
        return a if a >= b else b
    elif (both_evens):
        # print('both_evens')
        return a if a <= b else b

# Check
result1 = lesser_of_two_evens(2, 4)  
print(result1) # --> 2

result2 = lesser_of_two_evens(2, 5)  
print(result2) # --> 5