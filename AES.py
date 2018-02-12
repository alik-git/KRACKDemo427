from Crypto.Cipher import AES
from Crypto.Util import Counter
ctr = Counter.new(128)
obj = AES.new('0000000000000000', AES.MODE_CTR, counter=ctr)
message = "eeeeee"
ctexts = []
for i in range(6):
	ciphertext = obj.encrypt(message[i:i+1])
	print(ciphertext)
	ctexts.append(ciphertext)
ctr2 = Counter.new(128)
obj2 = AES.new('0000000000000000', AES.MODE_CTR, counter=ctr2)
for i in range(6):
	print(obj2.decrypt(ctexts[i]))



