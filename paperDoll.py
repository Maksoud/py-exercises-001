# Given a string, return a string where for every character in the original 
# there are three characters

def paper_doll(text):
    result = []
    for letter in text:
        result.append(letter*3)
    return "".join(result)

# Check
result1 = paper_doll('Hello')
print(result1) # --> 'HHHeeellllllooo'
result2 = paper_doll('Mississippi')
print(result2) # --> 'MMMiiissssssiiippppppiii'