import threading
def hello(name):
    for i in range(5):
        print(name,i)

t1=threading.Thread(target=hello, args=('anant',))
t2=threading.Thread(target=hello, args=('anant2',))

t1.start()
t2.start()