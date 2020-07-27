from threading import Thread
from Queue import Queue

def add(a,b):
    return a + b
def sub(c,d):
    return c - d
def mul(e,f):
    return e * f
    
def CommanThread(FunctionName, QueueName, *var):
    QueueName.put(FunctionName(*var))
    
AddQueue, subQueue, mulQueue = Queue(), Queue(), Queue()
    
AddThread = (Thread(target = CommanThread, args = (add, AddQueue, 50,50))).start()
SubThread = (Thread(target = CommanThread, args = (add, subQueue, 200,100))).start()
MulThread = (Thread(target = CommanThread, args = (add, mulQueue, 10,10))).start()

print AddQueue.get()
print subQueue.get()
print mulQueue.get() 