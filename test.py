#!/usr/bin/env python

from Crypto.Cipher import AES
from Crypto.Util import Counter

ctr = Counter.new(50000) 

aes = AES.new('random_key', AES.MODE_CTR, counter = ctr)

message1 = "Fool me once, shame on you"
message2 = "Fool me twice, shame on me"

ciphertext1 = aes.encrypt(message1)
ciphertext2 = aes.encrypt(message2)

print(ciphertext1)
print(ciphertext2)


