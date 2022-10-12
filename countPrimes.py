# Write a function that returns the number of prime numbers that exist up to and 
# including a given number

def count_primes(num):

    primes = 0

    for sequence in range(2, num+1):
        for i in range(2, sequence):
            if (sequence % i) == 0:
                # print(sequence, "is not a prime number")
                break
        else:
            # print(sequence, "is a prime number")
            primes+=1

    return primes

# Check
result = count_primes(100)
print(result) # --> 25