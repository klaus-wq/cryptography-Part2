import math
from bitarray import bitarray

def before_coding(text):
    file = 0
    bitArray = bitarray(endian="big")
    if type(text) == str:
        bitArray.frombytes(text.encode("utf-8"))
    else:
        bitArray.frombytes(text)
        file = 1
    return file, bitArray

def appendPaddingBytes(bitArray):
    bitArray.append(1)
    while len(bitArray) % 512 != 448:
        bitArray.append(0)
    return bitarray(bitArray, endian="big")

def appendLength(bitArray, length):
    # lengthBin = bin(length)[2:].zfill(8)
    # while len(lengthBin) != 64:
    #     lengthBin+='0'
    # bitArray.extend(lengthBin)

    lengthBitArray = bitarray()
    # if length > 2**64:
    #     lengthBin = bin(length)[2:].zfill(64)
    #     lengthBitArray.extend(lengthBin)
    #     X = bin(int.from_bytes(lengthBitArray.tobytes(), byteorder="little"))[2:].zfill(64)
    #     bitArray.extend(X[32:])
    # else:
    lengthBin = bin(length)[2:].zfill(64)
    lengthBitArray.extend(lengthBin)
    X = int.from_bytes(lengthBitArray.tobytes(), byteorder="little")
    bitArray.extend(bin(X)[2:].zfill(64))
    return bitArray

def fromBitsToInt(bitArray):
    X = []
    for i in range(len(bitArray)//32):
        tmp = bitArray[:32]
        X.append(int.from_bytes(tmp.tobytes(), byteorder="little"))
        bitArray = bitArray[32:]
    return X

def ABCD(intArray):
    A0 = 0x67452301
    B0 = 0xEFCDAB89
    C0 = 0x98BADCFE
    D0 = 0x10325476
    F = lambda x, y, z: (x & y) | (~x & z)
    G = lambda x, y, z: (x & z) | (y & ~z)
    H = lambda x, y, z: x ^ y ^ z
    I = lambda x, y, z: y ^ (x | ~z)
    rotateLeft = lambda x, n: (x << n) | (x >> (32 - n))
    modularAdd = lambda a, b: (a + b) % pow(2, 32)
    T = [int(pow(2, 32) * abs(math.sin(i + 1))) for i in range(64)]

    for i in range(len(intArray)//16):
        X = intArray[0:16]
        intArray = intArray[16:]

        A = A0
        B = B0
        C = C0
        D = D0
        for i in range(4 * 16):
            if 0 <= i <= 15:
                k = i
                s = [7, 12, 17, 22]
                temp = F(B, C, D)
            elif 16 <= i <= 31:
                k = ((5 * i) + 1) % 16
                s = [5, 9, 14, 20]
                temp = G(B, C, D)
            elif 32 <= i <= 47:
                k = ((3 * i) + 5) % 16
                s = [4, 11, 16, 23]
                temp = H(B, C, D)
            elif 48 <= i <= 63:
                k = (7 * i) % 16
                s = [6, 10, 15, 21]
                temp = I(B, C, D)

            temp = modularAdd(temp, X[k])
            temp = modularAdd(temp, T[i])
            temp = modularAdd(temp, A)
            temp = rotateLeft(temp, s[i % 4])
            temp = modularAdd(temp, B)

            A = D
            D = C
            C = B
            B = temp

        A0 = modularAdd(A0, A)
        B0 = modularAdd(B0, B)
        C0 = modularAdd(C0, C)
        D0 = modularAdd(D0, D)
    return A0, B0, C0, D0


def MD5(text):
    file, bitArray = before_coding(text)
    length = len(bitArray) % pow(2, 64)
    step1 = appendPaddingBytes(bitArray)
    step2 = appendLength(step1, length)
    intArray = fromBitsToInt(step2)
    A, B, C, D = ABCD(intArray)

    # tmp1 = step2
    # X = []
    # for i in range(len(step2)//8):
    #     x = tmp1[:8]
    #     X.append(int.from_bytes(x.tobytes(), byteorder="little"))
    #     tmp1 = tmp1[8:]

    tmp = bitarray(endian="big")
    tmp.extend(bin(A)[2:].zfill(32))
    tmp.extend(bin(B)[2:].zfill(32))
    tmp.extend(bin(C)[2:].zfill(32))
    tmp.extend(bin(D)[2:].zfill(32))
    res = ''
    for i in range(4):
        res+=hex(int.from_bytes(tmp[:32].tobytes(), byteorder="little"))[2:]
        tmp = tmp[32:]
    return res