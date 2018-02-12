#!/usr/bin/env python

from Crypto.Cipher import AES
from Crypto.Util import Counter

ctr1 = Counter.new(128) 
ctr2 = Counter.new(128)

aes1 = AES.new('random_key_isall', AES.MODE_CTR, counter = ctr1)
aes2 = AES.new('random_key_isall', AES.MODE_CTR, counter = ctr2)

message1 = "Fool me once, shame on you"
message2 = "Fool me twice, shame on me"

ciphertext1 = aes1.encrypt(message1)
ciphertext2 = aes2.encrypt(message2)

ciphertext1 = ciphertext1.encode("hex")
ciphertext2 = ciphertext2.encode("hex")

print 'Messages'
print(message1.encode("hex"))
print(message2.encode("hex"))

print 'Cihper Text2'
print(ciphertext1)
print(ciphertext2)

'''
Cipher Texts:
c7041f44d10f1801d4e081c61dee4cbf32090d0f90f5420cc554 c7041f44d10f1801cff98bc054e21fa43b05054adff40c55c744

Cipher Texts XOR:
00000000000000001b190a06490c531b090c08454f014e590210


466f6f6c206d65206f6e63652c207368616d65206f6e20796f75 466f6f6c206d652074776963652c207368616d65206f6e206d65

Messages XOR:
00000000000000001b190a06490c531b090c08454f014e590210
'''
