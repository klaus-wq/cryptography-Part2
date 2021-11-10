from gost89 import GOST_zamena

def xor1(a, b):
    return [a[i] ^ b[i] for i in range(len(a))]

# Шифрование по ГОСТ 28147-89
def E(h, K):
    Hint = []
    for i in range(len(h)//8):
        Hint.append(int(h[:8], 2))
        h = h[8:]
    Kint = []
    for i in range(len(K)//8):
        Kint.append(int(K[:8], 2))
        K = K[8:]
    keys = [0] * 8
    for i in range(8):
        keys[i] = Kint[i * 4:(i + 1) * 4]
    A = Hint[:4]
    B = Hint[4:]

    for j in range(3):
        for i in range(8):
            tmp = one_step(A, keys[i])
            tmp = xor1(tmp, B)
            B = A
            A = tmp

    for i in range(7, -1, -1):
        tmp = one_step(A, keys[i])
        tmp = xor1(tmp, B)
        B = A
        A = tmp

    res = B + A
    resBin = ''
    for i in range(len(res)):
        resBin+=bin(res[i])[2:].zfill(8)
    return resBin

# один шаг из шифрования ГОСТ 28147-89
def one_step(A, K):
    # Набор S-блоков компании CryptoPro
    # S = [
    #     [10,4,5,6,8,1,3,7,13,12,14,0,9,2,11,15],
    #     [5,15,4,0,2,13,11,9,1,7,6,3,12,14,10,8],
    #     [7,15,12,14,9,4,1,0,3,11,5,2,6,10,8,13],
    #     [4,10,7,12,0,15,2,8,14,1,6,5,13,11,9,3],
    #     [7,6,4,11,9,12,2,10,1,8,0,14,15,13,3,5],
    #     [7,6,2,4,13,9,15,0,10,1,5,11,8,14,12,3],
    #     [13,14,4,1,7,0,5,10,3,12,8,15,6,2,9,11],
    #     [1,3,10,9,5,11,4,15,8,6,7,14,13,0,2,12]]

    # «Тестовый» набор S-блоков
    S = [
        [4, 10, 9, 2, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 3],
        [14, 11, 4, 12, 6, 13, 15, 10, 2, 3, 8, 1, 0, 7, 5, 9],
        [5, 8, 1, 13, 10, 3, 4, 2, 14, 15, 12, 7, 6, 0, 9, 11],
        [7, 13, 10, 1, 0, 8, 9, 15, 14, 4, 6, 12, 11, 2, 5, 3],
        [6, 12, 7, 1, 5, 15, 13, 8, 4, 10, 9, 14, 0, 3, 11, 2],
        [4, 11, 10, 0, 7, 2, 1, 13, 3, 6, 8, 5, 9, 12, 15, 14],
        [13, 11, 4, 1, 3, 15, 5, 9, 0, 10, 14, 7, 6, 8, 2, 12],
        [1, 15, 13, 0, 5, 7, 10, 4, 9, 2, 3, 14, 6, 11, 8, 12]]

    res = [0] * 4
    c = 0
    for i in range(4):
        c += A[i] + K[i]
        res[i] = c & 0xff
        c >>= 8

    for i in range(8):
        if i & 1:
            x = res[i >> 1] & 0xf0
        else:
            x = res[i >> 1] & 0x0f
        res[i >> 1] ^= x
        if i & 1:
            x >>= 4

        x = S[i][x]
        if i & 1:
            res[i >> 1] |= x << 4
        else:
            res[i >> 1] |= x

    res = [res[3]] + res[:3]
    tmp = res[0] >> 5

    for i in range(1, 4):
        nTmp = res[i] >> 5
        res[i] = ((res[i] << 3) & 0xff) | tmp
        tmp = nTmp
    res[0] = ((res[0] << 3) & 0xff) | tmp
    return res

def toLittle(K):
    res = ''
    for i in range(len(K) // 8):
        res += K[len(K) - 8:len(K)]
        K = K[0:len(K) - 8]
    return res

def before_coding(text):
    if type(text) == str:
        text = text.encode("utf-8")
    else:
        text = text
    b = hex(int.from_bytes(text, "big"))[2:]
    res1 = ''
    for i in range(len(b)):
        res1+=bin(int(b[i], 16))[2:].zfill(4)
    return res1

def transA(block):
    y = []
    for i in range(4):
        y.append(block[:64])
        block = block[64:]
    return y[1] + y[2] + y[3] + bin(int(y[0], 2) ^ int(y[1], 2))[2:].zfill(64)

def transP(block):
    fi = [0 for i in range(32)]
    for i in range(4):
        for k in range(1, 9):
            fi[i + 1 + 4*(k-1) - 1] = 8*i + k - 1
    Y = []
    for i in range(len(block)//8):
        Y.append(block[:8])
        block = block[8:]
    res = ''
    for i in range(len(Y)):
        res+=Y[fi[i]] #Y[fi[len(Y)-i-1]]
    return res

def genKeys(Hin, m):
    C = [0, 0x00ff00ff00ff00ffff00ff00ff00ff0000ffff00ff0000ffff000000ffff00ff, 0]
    U = Hin
    V = m
    W = bin(int(U, 2) ^ int(V, 2))[2:].zfill(256)
    K = []
    K.append(transP(W))
    for i in range(1, 4):
        U = bin(int(transA(U), 2) ^ C[i-1])[2:].zfill(256)
        V = transA(transA(V))
        W = bin(int(U, 2) ^ int(V, 2))[2:].zfill(256)
        K.append(transP(W))
    K1 = K[0]
    res = ''
    for i in range(len(K1)//4):
        res+=hex(int(K1[:4], 2))[2:][:1]
        K1 = K1[4:]
    return K

def transShifr(Hin, K):
    h = []
    for i in range(len(Hin)//64):
        h.append(Hin[:64])
        Hin = Hin[64:]
    S = ''
    for i in range(4):
        S+=GOST_zamena(K[i], h[i], 1)
    K1 = S
    res = ''
    for i in range(len(K1)//4):
        res+=hex(int(K1[:4], 2))[2:][:1]
        K1 = K1[4:]
    return S

def psi(block):
    Y = []
    for i in range(len(block) // 16):
        Y.append(block[:16])
        block = block[16:]
    tmp = bin(int(Y[0], 2) ^ int(Y[1], 2))[2:].zfill(16)
    tmp = bin(int(tmp, 2) ^ int(Y[2], 2))[2:].zfill(16)
    tmp = bin(int(tmp, 2) ^ int(Y[3], 2))[2:].zfill(16)
    tmp = bin(int(tmp, 2) ^ int(Y[12], 2))[2:].zfill(16)
    tmp = bin(int(tmp, 2) ^ int(Y[15], 2))[2:].zfill(16)
    res = ''
    for i in range(1, 16, 1):
        res+=Y[i]
    res = res + tmp
    return res

def transShuffle(Hin, S, m):
    Hout = S
    for i in range(12):
        Hout = psi(Hout)
    Hout = bin(int(Hout, 2) ^ int(m, 2))[2:].zfill(256)
    Hout = psi(Hout)
    Hout = bin(int(Hin, 2) ^ int(Hout, 2))[2:].zfill(256)
    for i in range(61):
        Hout = psi(Hout)
    K1 = Hout
    res = ''
    for i in range(len(K1)//4):
        res+=hex(int(K1[:4], 2))[2:][:1]
        K1 = K1[4:]
    return Hout

def funcF(Hin, m):
    K = genKeys(Hin, m)
    shifr = transShifr(Hin, K)
    shuffle = transShuffle(Hin, shifr, m)
    return shuffle

def GOST94(text, Hin):
    bitArray = before_coding(text)
    Sum = '0'.zfill(256)
    L = '0'.zfill(256)
    for i in range(0, len(bitArray) - 255, 256):
        m = bitArray[:256]
        bitArray = bitArray[256:]
        Hin = funcF(Hin, m)
        Sum = bin((int(Sum, 2) + int(m, 2)) % pow(2, 256))[2:].zfill(256)
    L = toLittle(bin((int(L, 2) + int((bin(256)[2:]), 2)) % pow(2, 256))[2:].zfill(256))

    if len(bitArray) > 0:
        length = len(bitArray)
        while len(bitArray) != 256:
            bitArray = bitArray + '0'
        L = bin(length)[2:].zfill(8) + L[8:]
        Hin = funcF(Hin, bitArray)
        Sum = bin((int(Sum, 2) + int(bitArray, 2)) % pow(2, 256))[2:].zfill(256)

    Hin = funcF(Hin, L)
    Hin = funcF(Hin, Sum)

    resHex = ''
    for i in range(len(Hin)//4):
        resHex+=hex(int(Hin[:4], 2))[2:][:1]
        Hin = Hin[4:]
    return resHex

text1 = 'This is message, length=32 bytes'
print(GOST94(text1, '00'.zfill(256)))

