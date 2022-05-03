import lmdb
import pickle


class Person:
    Name = ""
    Age = 1

    def __init__(self, name, age):
        self.Name = name
        self.Age = age



env = lmdb.open("./train", map_size=4096 * 4096)
txn = env.begin(write=True)

person = Person('qwe', 1)
txn.put(key='1'.encode(), value=pickle.dumps(person))
a = pickle.loads(txn.get(key='1'.encode()))
print(a.Name)
txn.abort()
env.close()
