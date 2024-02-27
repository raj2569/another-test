from statsd import statsd
from random import random

statsd.connect(host="localhost", port=8125)
import time

while True:
    random_number = random.randint(1000, 1200)
    statsd.timing("nm.time.deprov", random_number, tags=["country:india"])
    statsd.gauge("login.gauge", random_number, tags=["country:india"])
    statsd.increment("nm.count.deprov", 1, tags=["country:india"])
    print(f"sent {random_number}")
    sleep_time = random.randint(1, 2)
    time.sleep(sleep_time)
