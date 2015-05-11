import math

def isPalindrome(x):
    str_array = list(str(x))
    iterate_len = len(str_array) / 2

    for i in range(iterate_len):
        if str_array[i] !=  str_array[len(str_array) - 1 - i]:
            return False

    return True

def isPrime(x):
    iterate_len = int(math.sqrt(x))

    for i in range(2, iterate_len + 1):
        if x % i == 0:
            return False

    return True



largest_prime = 0
for i in range(3, 1000):
    if isPalindrome(i) and isPrime(i):
        largest_prime = i

print largest_prime