# Python Module ciphersuite
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
# Use crypto random generation to get a key with length n


def gen():
    rkey = bytearray(os.urandom(16))
    for i in range(16):
        rkey[i] = rkey[i] & 1
    return bytes(rkey)

# Bitwise XOR operation.


def enc(k, m, iv):
    cipher = Cipher(algorithms.AES(k), modes.CBC(iv), default_backend())
    encryptor = cipher.encryptor()
    cph = encryptor.update(m) + encryptor.finalize()
    return cph


# Reverse operation
def dec(k, c, iv):
    cipher = Cipher(algorithms.AES(k), modes.CBC(iv), default_backend())
    decryptor = cipher.decryptor()
    msg = decryptor.update(c) + decryptor.finalize()
    return msg
