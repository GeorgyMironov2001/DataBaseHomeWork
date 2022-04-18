import redis
import json
import time

start_time = time.time()



with open('string_test.json') as f:
    templates = json.load(f)

prev_time = start_time
for item in templates:

    print("---%s---" % (time.time() - prev_time))
    prev_time = time.time()

for item in templates:

    print("---%s---" % (time.time() - prev_time))
    prev_time = time.time()
print("\n")
print("---%s---" % (time.time() - start_time))

