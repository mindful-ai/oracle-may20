# Project B

print('11_project_b.py ', __name__)

# Get a range from the user and pull all the prime numbers
# from that range

import project_a

# input
print('Starting project B')

start = int(input('Enter the start point:' ))
end = int(input('Enter a end point: '))


# process

primes = []
for n in range(start, end + 1):
    if(project_a.checkprime(n)):
        primes.append(n)


# output

print('PRIMES: ')
print(primes)
