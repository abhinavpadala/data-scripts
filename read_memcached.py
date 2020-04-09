import time
import threading
import subprocess

class ReadMemcached:
    def __init__(self):
        self.timer = 10

    def read_memcached(self):
        threading.Timer(self.timer, self.read_memcached).start()
        proc = subprocess.run("sudo docker logs --tail 15 dc-client".split(), encoding='utf-8', stdout=subprocess.PIPE)
        for line in proc.stdout.split('\n'):
            with open('memcached_logs.csv', 'a') as f:
                f.write(line + '\n')
        subprocess.call("bash ./logs_lat.bash".split())
obj = ReadMemcached()
obj.read_memcached()
