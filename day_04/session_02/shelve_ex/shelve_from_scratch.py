class complex:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):     # oa + ob   ====> self + other
        return complex(self.a + other.a, self.b + other.b)

    def __sub__(self, other):     # oa - ob   ====> self + other
        return complex(self.a - other.a, self.b - other.b)

    def __str__(self):
        return str(self.a) + ' + j' +  str(self.b)

    def addcomplex(self, complexobj):
        pass

# -----------------------------------------------------


L = ['red', 'green', 'blue']

D = {'name':'anil', 'age':35}

complexobjs = [complex(i, j) for i in range(10) for j in range(10) if (i + j) % 4 == 0]

'''
print(L)
print(D)

for obj in complexobjs:
    print(obj)
'''

N = []
while True:
    un = int(input('# '))
    N.append(un)
    if(un == 0):
        break



print(L)
print(D)

for obj in complexobjs:
    print(obj)

print(N)


# shelving process

import shelve

db = shelve.open("persistant_states.db")

db['list'] = L
db['dict'] = D
db['user'] = N
#db['objs'] = complexobjs

db.sync()

db.close()
