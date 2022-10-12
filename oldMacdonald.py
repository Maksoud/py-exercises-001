# Write a function that capitalizes the first 
# and fourth letters of a name

def old_macdonald(name):

    result = []

    for idx, letter in enumerate(name):

        if (idx == 0) or (idx == 3):
            result.append(letter.capitalize())
        else:
            result.append(letter)

    return ''.join(result)

# Check
result = old_macdonald('macdonald')
print(result) # 'MacDonald'