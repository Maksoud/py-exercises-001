# Write a function takes a two-word string 
# and returns True if both words begin with same letter

def animal_crackers(text):
    splitted = text.lower().split()
    return splitted[0][0] == splitted[1][0]

# Check
result1 = animal_crackers('Levelheaded Llama')
print(result1) # --> True

result2 = animal_crackers('Crazy Kangaroo')
print(result2) # --> False