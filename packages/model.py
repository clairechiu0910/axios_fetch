import time

class Model():
    def __init__(self, sec=5):
        self.sec = sec
    def call(self):
        print(f'waiting for {self.sec} sec')
        time.sleep(self.sec)