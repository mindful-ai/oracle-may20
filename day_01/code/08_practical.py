# Program to display the difference of the two numbers


# input

a = input("Enter a number: ")
b = input("Enter another number: ")

# process

a = int(a)
b = int(b)
res = a - b

# output

print('-'*50)

print('DIFFERENCE: ', abs(a - b))

if(res > 0):
    print('The result is positive')
elif(res < 0):
    print('The result is negative')
else:
    print('The result is zero')



    
