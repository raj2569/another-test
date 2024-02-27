from statsd import statsd
from random import random
statsd.connect(host='localhost', port=8125)
import time, random

while True:
    random_number = random.randint(1000, 1200)
    statsd.timing("nm.time.deprov", random_number, tags=["country:india"])
    statsd.gauge("login.gauge", random_number, tags=["country:india"])
    statsd.increment("nm.count.deprov", 1, tags=["country:india"])
    # statsd.timing("login_time_1", 1, tags=["country:india"])
    # statsd.timing("login_time_10", 10, tags=["country:india"])
    # statsd.timing("login_time_100", 100, tags=["country:india"])
    # statsd.timing("login_time_1000", 1000, tags=["country:india"])
    # statsd.timing("login_time_10000", 10000, tags=["country:india"])
    # statsd.timing("name.with.dot", 10000, tags=["country:india"])
    print (f"sent {random_number}")
    sleep_time = random.randint(1, 2)
    time.sleep(sleep_time)
