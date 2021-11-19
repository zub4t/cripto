import cbc
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from itertools import groupby


def printTheArray(arr, n):
    for i in range(0, n):
        print(arr[i], end=" ")
    print()


def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


def generateAllBinaryStrings(n, arr, i):
    if i == n:
        test_key = [None] * 128
        c = 0
        for bit in arr:
            for k in range(0, 8):
                test_key[k + (c*8)] = str(bit)
            c = c+1

        s = (''.join(test_key))
        print(s)
        #s = s[::-1]
        s = bytes(int(s[i: i + 8], 2) for i in range(0, len(s), 8))
       # print(s)
        f = open('group_15.txt', 'rb')
        m = f.readline()
        m = m[0:16]
        
        cipher = Cipher(algorithms.AES(s), modes.ECB(), default_backend())
        decryptor = cipher.decryptor()
        msg = decryptor.update(m) + decryptor.finalize()
       
        if (all_equal(msg)):
            print(s)
        return
    arr[i] = 0
    generateAllBinaryStrings(n, arr, i + 1)
    arr[i] = 1
    generateAllBinaryStrings(n, arr, i + 1)


if __name__ == "__main__":
    n = 16
    arr = [None] * 16
    generateAllBinaryStrings(n, arr, 0)
    # print(cbc.gen())
