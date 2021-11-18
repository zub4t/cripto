import cbc
import os


iv = os.urandom(16)
key = cbc.gen()

with open("iv_file", "wb") as binary_file:
    binary_file.write(iv)
with open("key_file", "wb") as binary_file:
    binary_file.write(key)

print(type(iv), " ")
cp = cbc.enc(key, b"meu nome e marco", iv)

print('cipher text ',cp,"\n")

print("iv:",iv.hex(),"\nkey:",key.hex())
with open("secrets.txt.enc", "wb") as binary_file:
    binary_file.write(cp)

stream = os.popen(
    "openssl aes-128-cbc -nopad -d  -in secrets.txt.enc -out secrets.txt.new -iv "+iv.hex()+" -K "+key.hex()+" ; cat secrets.txt.new")
output = stream.read()
print("openSSL out ",output)
print("dec function ",cbc.dec(key,cp,iv))
