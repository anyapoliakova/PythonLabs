def IsPrime(n):
    if n == 1: 
        return False  
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n

def sum_primes(arr):
    sum = 0
    for element in arr:
        if IsPrime(element):
            sum += element
    return None if sum == 0 else sum

print('sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ->', sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print('sum_primes([2, 3, 4, 11, 20, 50, 71]) ->', sum_primes([2, 3, 4, 11, 20, 50, 71]))
print('sum_primes([]) ->', sum_primes([]))
