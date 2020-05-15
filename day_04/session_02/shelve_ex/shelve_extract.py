import shelve

db = shelve.open("persistant_states.db")

L = db['list']
N = db['user']

R = db['dict']

db.close()

print(L, type(L))
print(N, type(N))

print(R, type(R))
