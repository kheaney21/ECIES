import sys
import random
import base64
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto import Random
from ECIES import ECIES


def getInput(user1, user2, p):
	'Gets input from user'
	option = input("1 - Encrypt, 2 - Decrypt \n")
	filename = raw_input("Enter file name with extension \n")
	if option == 1:
		pubKey = user1.genPubKey(user1.privKey, user2.result, p)
		encrypt(pubKey, filename)
	elif option == 2:
		decrypt(user1.privKey, filename)
	else:
		print("Invalid input")
		
def genPrime(n, k):
	'Generate a prime number'

	x = random.randrange(51, n, 2)
	count = 0
	print("k " + str(k))
	while (not isPrime(x, k) and count < k):
		x = random.randrange(51, n, 2)
		count = count + 1
		#print(str(count) + " x " + str(x))
	print("final x " + str(x))
	print("count " + str(count))
	return x
			
#check if prime via miller-rabin test
def isPrime(n, k):
	'Check if prime via Miller-Rabin test'
		
	#calculate d
	temp = n
	s = 0
	while temp % 2 == 0:
		temp = temp/2
		s = s + 1
			
	d = n/(2**s)
		
	count = 0
	while count < k:
		#update counter
		count = count + 1
		#generate pseudorandom number
		a = random.randint(2, n - 1)
		x = a**d % n
		if (x == 1 or x == n - 1):
			continue
		for i in range (s-1):
			x = (x**2) % n
			if x == 1:
				return False
			if x == n - 1:
				continue
				
		return False
	return True
		
def encrypt(key, filename):
	'Encrypts a file with AES'
	#read file as string
	file = open(filename, "r+")
	iv = Random.new().read(AES.block_size)
	cipher = AES.new(str(key).encode().ljust(32), AES.MODE_CFB, iv)
	cipherText = cipher.encrypt(str(file))
	#result = base64.b64encode(cipher.encrypt(str(plainText)))
	file.write(cipherText)
	

def decrypt(key, filename):
	'Decrypts a file with AES'
	file = open(filename, "r+")
	#cipherText = base64.b64decode(str(file) + "===")
	#iv = file[:AES.block_size]
	cipher = AES.new(str(key).encode().ljust(32), AES.MODE_CFB, iv)
	#need to pad to multiple of 16
	plainText = cipher.decrypt(str(file))
	#plainText = cipher.decrypt(cipherText[AES.block_size:])
	file.write(plainText)
	
#max times to check if prime
k = 5000
#limit for number range
n = 10000
#generate random prime numbers g and p
p = genPrime(n, k)
g = genPrime(n, k)

user1 = ECIES(p, g)
user2 = ECIES(p, g)

getInput(user1, user2, p)
getInput(user1, user2, p)
	
	
