import numpy as np
import lmdb

env = lmdb.open("./train", map_size=4096 * 4096, max_dbs=3)
txn1 = env.begin(write=True)
subdb1 = env.open_db(key='firstDB'.encode(), txn=txn1)
txn1.put('a'.encode(), '1'.encode())
txn1.commit()

txn2 = env.begin(write=True)
subdb2 = env.open_db(key='secondDB'.encode(), txn=txn2)
txn2.commit()

txn4 = env.begin(db=subdb1, write=True)
txn4.put('person'.encode(), 'Gera'.encode())
txn4.commit()

txn3 = env.begin(db=subdb1, write=False)
for key, value in txn3.cursor():
    print(key, value)
txn3.abort()
env.close()
