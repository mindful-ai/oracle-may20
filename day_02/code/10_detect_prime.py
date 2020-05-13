# Project A

# Program to find out if a number is prime or not

# input

n = int(input('Enter a number: '))

# process

prime = True

for i in range(2, n):
    if(n % i == 0):
        prime = False
        break

# output

if(prime): # prime == True
    print('This is a prime number')
else:      # not prime
    print('This is not a prime number')


    
