# Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, 
# if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(a, b, c):

    Sum = sum([a, b, c])

    if (Sum > 21):
        if (11 in [a, b, c]):
            Sum -= 10
        if (Sum > 21):
            return 'BUST'
    return Sum

# Check
result1 = blackjack(5, 6, 7)
print(result1) # --> 18
result2 = blackjack(9, 9, 9)
print(result2) # --> 'BUST'
result3 = blackjack(9, 9, 11)
print(result3) # --> 19