'''
for <var> in <iter>:
    <statements block A>
else:
    <statements block B>

while <condition>:
    <statements block A>
else:
    <statements block B>

1. The number of items in the iterator is exhausted - Natural Exit
2. The loop can exit because of the break statement as well - Abrupt Exit

If the loop exits naturally, then statements block B will execute once
else if the loop exits because of the break statement then statements block B will NOT execute

'''

n = int(input('Enter a number: '))

for i in range(2, n):
    if(n % i == 0):
        print('The number is not prime')
        break
else:
    print('The number is prime')
