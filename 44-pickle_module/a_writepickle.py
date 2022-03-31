import pickle

l = [10, 20, 30, 40]

file = open('a_writedata.txt', 'wb')

# wb means write binary

pickle.dump(l,file)