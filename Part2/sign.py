from basicAlg import exgcd, gcd
from random import randint

def find_k(p):
    k = randint(1, p-2)
    while gcd(k, p-1) != '1' or exgcd(k, p-1) == 'Обратный элемент не существует':
        k = randint(1, p-2)
    return k