# Write a function that takes in a single letter, and returns a 5x5 representation of that letter

bigLetters = {
    "a":"""
   *  
  * * 
 *****
 *   *
 *   *
""",
    "b":"""
 ****
 *   *
 ****
 *   *
 ****
""",
    "c":"""
  **** 
 *    *
 *
 *    *
  ****
""",
    "d":"""
 ****
 *   *
 *    *
 *   *
 ****
"""
}

def print_big(letter):
    return bigLetters[letter.lower()]

result1 = print_big('a')
print(result1)
result2 = print_big('b')
print(result2)
result3 = print_big('c')
print(result3)
result4 = print_big('d')
print(result4)