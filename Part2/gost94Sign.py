from random import randint, getrandbits
from primes import isPrime, generator
from basicAlg import degree

def find_a(p, q):
    a = 1
    while a == 1:
        d = randint(2, p - 2)
        a = pow(d, (p - 1) // q, p)
    return a

def find_krs(a, p, q, h, x):
    s = 0
    r = 0
    while s == 0 or r == 0:
        k = randint(2, q - 1)
        r = pow(a, k, p) % q
        s = (k * h + x * r) % q
    return k, r, s

def calc_t(t0):
    t = [t0]
    while t[-1] >= 17:
        t.append(t[-1] // 2)
        s = len(t)
    return t, s

def next_prime(s):
    tmp = 2 ** (s - 1) + 1
    while isPrime(tmp) == False:
        tmp += 2
    return tmp

def gen_c():
    c = randint(1, 2 ** 16 - 1)
    while c % 2 == 0:
        c = randint(1, 2 ** 16 - 1)
    return c

def calc_y1(y0, c, size):
    y = [y0] * size
    for i in range(1, size):
        y[i] = (19381 * y[i - 1] + c) % 2 ** 16

    y1 = 0
    for i in range(size - 1):
        y1 += y[i] * (2 ** (161))
    return y1, y[-1]

def gen_PQ():
    x0 = randint(1, 2 ** 16 - 1)
    c = gen_c()
    t = 510
    t_arr, s = calc_t(t)
    p_s = next_prime(s)
    p = [0] * s
    p[-1] = p_s
    m = s - 1
    y0 = x0

    while m > 0:
        rm = t_arr[m - 1] // 16

        p[m - 1] = 2 ** (t + 1)
        while p[m - 1] > 2 ** t:
            Ym, y0 = calc_y1(y0, c, rm)

            N = ((2 ** (t_arr[m - 1] - 1)) // p[m]) + ((2 ** (t_arr[m - 1] - 1) * Ym) // (p[m] * 2 ** (16 * rm)))
            if N % 2 == 0:
                N = N
            else:
                N+=1

            k = 0
            flag = False
            while not flag:
                p[m - 1] = p[m] * (N + k) + 1

                a = pow(2, p[m] * (N + k), p[m - 1])
                b = pow(2, N + k, p[m - 1])

                if p[m - 1] > 2 ** t:
                    break
                if (a == 1) and (b != 1):
                    flag = True
                else:
                    k += 2
        m -= 1
    return p[0], p[1]

def gen_PQ1():
    q = generator(10**77, 10**78, 1)[0]
    print(bin(q)[2:][0])
    print(len(bin(q)))
    b = randint(1, 10)
    p = b * q + 1
    while isPrime(p) != True or bin(p)[2:][0] != '1':
        q = generator(10 ** 77, 10 ** 78, 1)[0]
        b = (p - 1) // q
        p = b * q + 1
    return p, q

# p, q = gen_PQ()
# print(len(bin(p)))
# print(len(bin(q)))