import random

#input since p & g are shared and not secret
def genPrivKey(p, g):
	'Generate a private key from 2 prime numbers'
	
	#limit for number range
	n = 10000
	
	#generate random number a for private key
	a = random.randint(2, n)
	
	#calculate result A
	A = g**a % p
	#print("a " + str(a))
	#print("g " + str(g))
	#print("p " + str(p))
	#print("A " + str(A))
	
	
	return (a, A)
	
def genPubKey(a, B, p):
	'Generate public key with secret number a, result B, and shared p'
	
	#calculate public key
	pubKey = B**a % p
	#print("B " + str(B))
	#print("a " + str(a))
	#print("p " + str(p))
	
	return pubKey
	
def genPrime(n, k):
	'Generate a prime number'
	y = random.randrange(80, 120)
	x = random.randrange(3, n, 2)
	count = 0
	print("k " + str(k))
	while (not isPrime(x, k) and count < k):
		x = random.randrange(51, n, 2)
		count = count + 1
		print(str(count) + " x " + str(x))
	#print("final x1 " + str(x1))
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
	
def verifyKeys(a, b):
	if a == b:
		print("Keys match")
		print(a)
	else:
		print("Keys do not match")
		print("a " + str(a))
		print("b " + str(b))


#max times to check if prime
k = 10000
#limit for number range
n = 10000
#generate random prime numbers g and p
p = genPrime(n, k)
g = genPrime(n, k)

#generate private key for A

privKeyA = genPrivKey(p, g)
A = privKeyA[1]
print("A " + str(A))

#generate private key for B

privKeyB = genPrivKey(p, g)
B = privKeyB[1]
print("B " + str(B))

#generate public key for A
a = privKeyA[0]
pubKeyA = genPubKey(a, B, p)
#print("pubKey " + str(pubKeyA))


#generate public key for B
b = privKeyB[0]
pubKeyB = genPubKey(b, A, p)

#verify that the keys match
verifyKeys(pubKeyA, pubKeyB)
