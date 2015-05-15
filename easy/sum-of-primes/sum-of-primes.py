import math

def isPrime(x):
    iterate_len = int(math.sqrt(x))

    for i in range(2, iterate_len + 1):
        if x % i == 0:
            return False

    return True


sum = 0
prime_counter = 0
counter = 2
while True:

    if isPrime(counter):
        sum += counter
        prime_counter += 1

    counter += 1

    if prime_counter == 1000:
        break


print sum