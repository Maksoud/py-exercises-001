# Given two integers, return True if the sum of the integers is 20 or 
# if one of the integers is 20. If not, return False

def makes_twenty(n1, n2):
    return True if (n1 == 20 or n2 == 20) or (n1 + n2 == 20) else False

# Check
result1 = makes_twenty(20, 10)
print(result1) # --> True
result2 = makes_twenty(12, 8)
print(result2) # --> True
result3 = makes_twenty(2, 3)
print(result3) # --> False