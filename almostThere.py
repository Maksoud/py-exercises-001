# Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(n):
    return True if (n >= (100 - 10) and n <= (100 + 10)) or (n >= (200 - 10) and n <= (200 + 10)) else False

# Check
result1 = almost_there(90)
print(result1) # --> True
result2 = almost_there(104)
print(result2) # --> True
result3 = almost_there(150)
print(result3) # --> False
result4 = almost_there(209)
print(result4) # --> True