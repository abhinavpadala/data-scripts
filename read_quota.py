import time
import threading

class ReadQuota:
    def __init__(self):
        self.timer = 1

    def read_quota(self):
        threading.Timer(self.timer, self.read_quota).start()
        path = "/sys/fs/cgroup/cpu/docker/f62a80b9d49c033b4a93ac95f9d5e497c43b998ce2bf2be6df8f7519c7489879/cpu.cfs_quota_us"
        with open(path, 'r') as fr:
            self.value = fr.read()
        csvdata = str(round(time.time())) + ',' + str(self.value)
        with open('out_quota.csv', 'a') as fw:
            fw.write(csvdata)

obj = ReadQuota()
obj.read_quota()

