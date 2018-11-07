import random

#input since p & g are shared and not secret
def genPrivkey(self, p, g):
	'Generate a private key from 2 prime numbers'
	
	#limit for number range
	n = 10,000
	
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
	x = random.randrange(3, 10000, 2) #had to hardcode, n is not working
	while not (isPrime(x, k)):
		x = random.randrange(3, 10000, 2) #had to hardcode, n is not working
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
	if a == b:
		print("Keys match")
	else:
		print("Keys do not match")


#max times to check if prime
k = 100
#limit for number range
n = 10000
#generate random prime numbers g and p
p = genPrime(n, k)
g = genPrime(n, k)

#generate private key for A

privKeyA = genPrivKey(p, g)
A = privKeyA[1]

#generate private key for B

privKeyB = genPrivKey(p, g)
B = privKeyA[1]

#generate public key for A
pubKeyA = genPubKey(a, B, p)

#generate public key for B
pubKeyB = genPubKey(b, A, p)

#verify that the keys match
verifyKeys(pubKeyA, pubKeyB)
	
