import numpy as np
import lmdb

env = lmdb.open("./train", map_size=4096 * 4096)
txn = env.begin(write=True)

txn.put(key='1'.encode(), value='aaa'.encode())

txn.commit()

txn1 = env.begin(write=True)
txn2 = env.begin(write=False)

txn1.delete(key='1'.encode())
txn1.commit()

txn3 = env.begin(write=False)

assert txn3.get(key='1'.encode()) is None
txn3.abort()

print(txn2.get(key='1'.encode()))
txn2.abort()
env.close()
