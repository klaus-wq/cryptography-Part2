def xor(a: str, b: str):
    if len(a) > len(b):
        a = a.zfill(len(b))
    elif len(b) > len(a):
        b = b.zfill(len(a))
    res = bin(int(a, 2) ^ int(b, 2))[2:].zfill(len(a))
    return res

def sdvig(str: str, n: int):
    arrTxt = str[n:] + str[:n]
    return arrTxt

def substitution(N1:str):
    __Sbox =    [[ 4, 10,  9,  2, 13,  8,  0, 14,  6, 11,  1, 12,  7, 15,  5,  3],
    [14, 11,  4, 12,  6, 13, 15, 10,  2,  3,  8,  1,  0,  7,  5,  9],
    [ 5,  8,  1, 13, 10,  3,  4,  2, 14, 15, 12,  7,  6,  0,  9, 11],
    [ 7, 13, 10,  1,  0,  8,  9, 15, 14,  4,  6, 12, 11,  2,  5,  3],
    [ 6, 12,  7,  1,  5, 15, 13,  8,  4, 10,  9, 14,  0,  3, 11,  2],
    [ 4, 11, 10,  0,  7,  2,  1, 13,  3,  6,  8,  5,  9, 12, 15, 14],
    [13, 11,  4,  1,  3, 15,  5,  9,  0, 10, 14,  7,  6,  8,  2, 12],
    [ 1, 15, 13,  0,  5,  7, 10,  4,  9,  2,  3, 14,  6, 11,  8, 12]]
    # 8 блоков по 4 бита
    blocks4b = []
    for i in range(4):
        a = N1[:8]
        blocks4b.append(a[4:])
        blocks4b.append(a[:4])
        N1 = N1[8:]
        #blocks4b.append(N1[:4])
        #N1 = N1[4:].zfill(4)
    # for i in range(len(blocks4b)):
    #     print(int(blocks4b[i], 2))
    blocksAfterSbox = ''
    for i in range(8):
        blocksAfterSbox+=bin(__Sbox[i][int(blocks4b[i], 2)])[2:].zfill(4)
    return sdvig(blocksAfterSbox, 11)

def round_feistel_scheme(L0: str, R0: str, key: str):
    # RES = (N1 + Ki) mod 2 ^ 32
    RES = bin((int(L0, 2) ^ int(key, 2)) % 2**32)[2:].zfill(32)

    # RES = RES -> Sbox, << 11
    RES = substitution(RES)
    tmp = RES
    L0, R0 = xor(RES, R0), L0
    return L0, R0

def feistel_scheme(block:str, keys:list, flag:int):
    L0 = block[:32]
    R0 = block[32:]
    if flag == 1:
        # K0, K1, K2, K3, K4, K5, K6, K7, K0, K1, K2, K3, K4, K5, K6, K7, K0, K1, K2, K3, K4, K5, K6, K7
        for i in range(3):
            for j in range(len(keys)):
                L0, R0 = round_feistel_scheme(L0, R0, keys[j])
        # K7, K6, K5, K4, K3, K2, K1, K0
        for i in range(len(keys)):
            L0, R0 = round_feistel_scheme(L0, R0,  keys[len(keys) - 1 - i])
        L0, R0 = R0, L0
    else:
        # K0, K1, K2, K3, K4, K5, K6, K7
        for i in range(len(keys)):
            L0, R0 = round_feistel_scheme(L0, R0, keys[i])
        # K7, K6, K5, K4, K3, K2, K1, K0, K7, K6, K5, K4, K3, K2, K1, K0, K7, K6, K5, K4, K3, K2, K1, K0
        for i in range(3):
            for j in range(len(keys)):
                L0, R0 = round_feistel_scheme(L0, R0, keys[len(keys) - 1 - j])
        L0, R0 = R0, L0
    return L0 + R0

def GOST_zamena(keys1, text, flag):
    keys = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        keys[i] = keys1[:32]
        keys1 = keys1[32:]

    blocksBin, file = [text], 0

    block64b = ''
    for i in range(len(blocksBin)):
        block64b += feistel_scheme(blocksBin[i], keys, flag)
    #print('res', block64b)
    return block64b

def toInt(text):
    text1 = text
    textInt = []
    for i in range(len(text)//8):
        textInt.append(int(text1[:8], 2))
        text1 = text1[8:]
    return textInt

def toLittle(K):
    res = ''
    for i in range(len(K) // 8):
        res += K[len(K) - 8:len(K)]
        K = K[0:len(K) - 8]
    return res

#0001101100001011101111000011001011001110101111001010101101000010
#0110101001100011111100011100101101000000010001101011000011111100
#print(GOST_zamena('0101010001101101001000000011001101101000011001010110110000110010011010010111001101100101001000000111001101110011011011100110001000100000011000010110011101111001011010010110011101110100011101000111001101100101011010000110010100100000001011000011110101110011', '0000000000000000000000000000000000000000000000000000000000000000', 1))