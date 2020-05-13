print('project_a.py ', __name__)

# Re-do Project A with a different approach (Ref: 10_detect_prime.py)
# How to write a user defined function and test it

def checkprime(n):
    prime = True

    for i in range(2, n):
        if(n % i == 0):
            prime = False
            break
        
    return prime


# ---------------------------------------


if __name__ == '__main__':
    
    # Project A

    print('This is project A')

    # input

    x = int(input('Enter a number: '))

    # process

    res = checkprime(x)

    # output

    if(res): 
        print('This is a prime number')
    else:      
        print('This is not a prime number')

