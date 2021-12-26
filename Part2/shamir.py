from RSA import gcd
from primes import generator

def find_C(p):
    c = generator(2, p - 2, 1)[0]
    while c >= p-1 or gcd(c, p - 1) != '1':
        c = generator(2, p - 2, 1)[0]
    return c