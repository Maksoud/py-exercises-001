# Given a sentence, return a sentence with the words reversed

def master_yoda(text):
    splitted = text.split(" ")
    return " ".join(splitted[::-1])

# Check
result1 = master_yoda('I am home')
print(result1) # --> 'home am I'
result2 = master_yoda('We are ready')
print(result2) # --> 'ready are We'