import subprocess
import time
import threading

class ReadLlc:
    def __init__(self):
        self.timer = 1

    def read_llc(self):
        threading.Timer(self.timer, self.read_llc).start()
        llc = []
        proc =subprocess.run('sudo pqos -s'.split(), encoding='utf-8', stdout=subprocess.PIPE)
        for line in proc.stdout.split('\n'):
            if "L3CA COS1 =>" in line:
                keyword = 'MASK '
                before, keyword, after = line.partition(keyword)
                llc.append(after)
        csvdata = str(round(time.time())) + ',' + str(llc[0]) + '\n'
        with open('out_llc.csv', 'a') as fw:
            fw.write(csvdata)


obj = ReadLlc()
obj.read_llc()
