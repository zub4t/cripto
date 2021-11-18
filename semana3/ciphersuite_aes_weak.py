# Python Module ciphersuite
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Use crypto random generation to get a key with length n
def gen(): 
	rkey = bytearray(os.urandom(16))
	for i in range(16): rkey[i] = rkey[i] & 1
	return bytes(rkey)

# Bitwise XOR operation.
def enc(k, m):
	cipher = Cipher(algorithms.AES(k), modes.ECB())
	encryptor = cipher.encryptor()
	cph = b""
	for ch in m:
		cph += encryptor.update((ch*16).encode())
	cph += encryptor.finalize()
	return cph


# Reverse operation
def dec(k, c):
	assert len(c) % 16 == 0
	cipher = Cipher(algorithms.AES(k), modes.ECB())
	decryptor = cipher.decryptor()
	blocks = len(c)//16
	msg = b""
	for i in range(0,(blocks)):
		msg+=decryptor.update(c[i*16:(i+1)*16])
		msg=msg[:-15]
	msg += decryptor.finalize()
	return msg
