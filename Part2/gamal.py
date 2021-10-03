from primes import generator
from basicAlg import gcd

def find_X(p):
    c = generator(2, p - 3, 1)[0]
    while gcd(c, p - 1) != '1':
        c = generator(2, p - 3, 1)[0]
    return c
