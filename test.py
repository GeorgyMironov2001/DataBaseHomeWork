import json
import redis
import time
with open('string_test.json') as f_str:
    templates_str = json.load(f_str)

client = redis.Redis(host='127.0.0.1')

start_time = time.time()
counter = 0
for item in templates_str:
    client.zadd('persons', {item['name']:item['age']})
    counter += 1
    if counter == 10:
        break
    # print("---%s---" % (time.time() - prev_time))

prev_time = (time.time() - start_time)
print("общее время загрузки данных %s" % (prev_time))
counter = 0
print(client.zrange('persons', 0, len(templates_str)))

print("%s" %(time.time() - start_time))


client.close()