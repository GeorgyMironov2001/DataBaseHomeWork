import redis
import json
import time

start_time = time.time()

client = redis.Redis(host='127.0.0.1')

with open('string_test.json') as f_str:
    templates_str = json.load(f_str)

for item in templates_str:
    client.set(item['name'], item['age'])
    # print("---%s---" % (time.time() - prev_time))


print("общее время загрузки данных при загрузке сетом %s" % (time.time() - start_time))

start_time = time.time()

for item in templates_str:
    client.get(item['name'])
    # print("---%s---" % (time.time() - prev_time))

print("общее время получения данных при выгрузке гетом %s" % (time.time() - start_time))

for item in templates_str:
    client.delete(item['name'])
# -----------------------------------------------------
start_time = time.time()

for item in templates_str:
    client.lpush(item['name'], item['age'])
    # print("---%s---" % (time.time() - prev_time))

print("общее время загрузки данных при загрузке в лист %s" % (time.time() - start_time))
start_time = time.time()
for item in templates_str:
    client.lpop(item['name'])
    # print("---%s---" % (time.time() - prev_time))

print("общее время получения данных из листа %s" % (time.time() - start_time))

# -----------------------------------------------------
start_time = time.time()
with open('hset_test.json') as f_hset:
    templates_hset = json.load(f_hset)

for item in templates_hset:
    client.hset(item['name'], 'age', item['age'])
    client.hset(item['name'], 'class', item['class'])
    # print("---%s---" % (time.time() - prev_time))


print("общее время загрузки данных в hset %s" % (time.time() - start_time))
start_time = time.time()
for item in templates_hset:
    client.hgetall(item['name'])
    # print("---%s---" % (time.time() - prev_time))

print("общее время получения данных из hset %s" % (time.time() - start_time))

for item in templates_hset:
    client.delete(item['name'])

# -----------------------------------------------------
start_time = time.time()

for item in templates_str:
    client.zadd('persons', {item['name']: item['age']})
    # print("---%s---" % (time.time() - prev_time))

print("общее время загрузки данных в сортированный список %s" % (time.time() - start_time))

start_time = time.time()
client.zrange('persons', 0, len(templates_str))

print("общее время получения данных из zset %s" % (time.time() - start_time))
client.delete('persons')
client.close()
