import pickle

file = open('a_writedata.txt', 'rb')
# rb means read binary


l = pickle.load(file)

print(l)