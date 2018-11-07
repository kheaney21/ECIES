import random
import sys
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto import Random


class ECIES:
	'Class for ECIES object'
	def __init__(self, p, g):
		self.privKeyResult = self.genPrivKey(p, g)
		self.privKey = self.privKeyResult[0]
		self.result = self.privKeyResult[1]
	
	#def EC():
		# curve y^2 = x^3 + ax + b

	#input since p & g are shared and not secret
	def genPrivKey(self, p, g):
		'Generate a private key from 2 prime numbers'
	
		#limit for number range
		n = 10000
	
		#generate random number a for private key
		a = random.randint(2, n)
	
		#calculate result A
		A = g**a % p

		return (a, A)
	
	def genPubKey(self, a, B, p):
		'Generate public key with secret number a, result B, and shared p'
	
		#calculate public key
		pubKey = B**a % p
	
		return pubKey
	
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
	
	def verifyKeys(self, a, b):
		'Verify that they keys a & b match'
		if a == b:
			print("Keys match")
			print(a)
		else:
			print("Keys do not match")
			print("a " + str(a))
			print("b " + str(b))
		
	def getHash(x):
		'Get SHA 256 Hash'
		x = SHA256.new(x)
		return x
	
	def encrypt(key, filename):
		'Encrypts a file based on ECIES and Diffie Hellman'
		#read file as string
		plainText = open(filename, "r+")
		iv = Random.new().read(AES.block_size)
		cipher = AES.new(getHash(key), AES.MODE_CBC, iv)
		plainText.write(cipher)

	def decrypt(key, filename):
		'Decrypts a file based on ECIES and Diffie Hellman'
		cipherText = open(filename, "r+")
		iv = cipherText[:AES.block_size]
		cipher = AES.new(getHash(key), AES.MODE_CBC, iv)
		plainText = cipher.decrypt(cipherText[AES.block_size:])
		filename.write(plainText)
	

#---------------------------------------------

#max times to check if prime
k = 10000
#limit for number range
n = 10000
#generate random prime numbers g and p
#p = genPrime(n, k)
#g = genPrime(n, k)

	#generate private key for A

#privKeyA = genPrivKey(p, g)
#A = privKeyA[1]
#print("A " + str(A))

	#generate private key for B

#privKeyB = genPrivKey(p, g)
#B = privKeyB[1]
#print("B " + str(B))

	#generate public key for A
#a = privKeyA[0]
#pubKeyA = genPubKey(a, B, p)
#print("pubKey " + str(pubKeyA))

	#generate public key for B
#b = privKeyB[0]
#pubKeyB = genPubKey(b, A, p)

	#verify that the keys match
#verifyKeys(pubKeyA, pubKeyB)


