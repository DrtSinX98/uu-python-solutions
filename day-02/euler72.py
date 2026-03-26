#!/usr/bin/python
from math import sqrt

@profile
def gen_primes(n):
    l = range(2, n)
    primes = []
    for j in range(0, len(l)):
        p = True
        for d in primes:
            if d > sqrt(l[j]):
                break
            if l[j] % d == 0:
                p = False
                break
        if p:
            primes.append(l[j])
    return primes

@profile
def factorize(n, primes):
    factors = []
    for p in primes:
        if p * p > n:  # Optimized loop break
            break
        while n % p == 0:
            n = n // p  # Integer division
            factors.append(p)
            
    if n > 1:
        factors.append(n)
    return factors

@profile
def fast_phi(n, primes):
    factors = factorize(n, primes)
    phi = factors[0] - 1
    for i in range(1, len(factors)):
        if factors[i] == factors[i-1]:
            phi *= factors[i]  # Mathematically simplified
        else:
            phi *= (factors[i] - 1)
    return phi

primes = gen_primes(1000)
m = 10000 
fraq = 0

for i in range(2, m + 1):
    fraq += fast_phi(i, primes)

print(fraq)