import threading
import time
import random
from queue import Queue

BUF_SIZE = 10
q = Queue(BUF_SIZE)

class produce_item(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(produce_item,self).__init__()
        self.target = target
        self.name = name

    def run(self):
        while True:
            if not q.full():
                item = random.randint(1,10)
                q.put(item)
                print('Inseret ' + str(item)  + ' : On a ' + str(q.qsize()) + ' element dans queue')
                self.wait()
        return

    def wait(self):
        time.sleep(random.random())
        return

class consum_item(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(consum_item,self).__init__()
        self.target = target
        self.name = name
        return

    def run(self):
        while True:
            if not q.empty():
                item = q.get()
                print('Récupérer ' + str(item) + ' : On a ' + str(q.qsize()) + ' element dans queue')
                self.wait()
        return
	
    def wait(self):
        time.sleep(random.random())
        return

if __name__ == '__main__':
    
    p = produce_item(name='producer')
    c = consum_item(name='consumer')

    p.start()
    time.sleep(2)
    c.start()
    time.sleep(2)
