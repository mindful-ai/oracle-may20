try:
    f = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\transcripts\lyrics.txt")
    a = '123' + '10'
    c = int(ghf, 8)
except FileNotFoundError:
    print('The file not found!')
except TypeError:
    print('Type mismatch for the operator')
except Exception as E:
    print('Unknown exception!')
    print(E)
else:
    print('The file is open!')
    f.close()
finally:
    print('Thank you')



print('The program execution continues!')
