# Write a function that takes in a single letter, and returns a 5x5 representation of that letter

dictA = """
   *  
  * * 
 *****
 *   *
 *   *
"""
dictB = """
 ****
 *   *
 ****
 *   *
****
"""
dictC = """
  **** 
 *    *
 *
 *    *
  ****
"""
dictD = """
 ****
 *   *
 *    *
 *   *
 ****
"""

def print_big(letter):
    match letter.lower():
        case "a":
            return dictA
        case "b":
            return dictB
        case "c":
            return dictC
        case "d":
            return dictD
        case _:
            return "not found!"

result1 = print_big('a')
print(result1)
result2 = print_big('b')
print(result2)
result3 = print_big('c')
print(result3)
result4 = print_big('d')
print(result4)