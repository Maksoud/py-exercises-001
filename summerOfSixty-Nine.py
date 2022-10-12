# Return the sum of the numbers in the array, except ignore sections of numbers starting 
# with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). 
# Return 0 for no numbers.

def summer_69(arr):
    
    Sum = 0
    ignore = False

    for num in arr:

        if (ignore == False):
            if (num == 6): 
                ignore = True
            else:
                Sum += num
        else:
            if (num == 9):
                ignore = False

    return Sum

# Check
result1 = summer_69([1, 3, 5])
print(result1) # --> 9
result2 = summer_69([4, 5, 6, 7, 8, 9])
print(result2) # --> 9
result3 = summer_69([2, 1, 6, 9, 11])
print(result3) # --> 14