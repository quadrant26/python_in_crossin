import pickle

test_data = ['Save me!', 123.456, True]

f = open('test.data', 'wb')
pickle.dump(test_data, f, True)
f.close()

f1 = open('test.data', 'rb')
data = pickle.load(f1)
f1.close()
print(data)
