import multiprocessing


a=0
quant_process=2
q=multiprocessing.Queue()


def f():
    global a
    for i in range(1000):
        a+=1
    q.put(a)

for i in range(quant_process):
    p=multiprocessing.Process(target=f)
    p.start()


for p in range(quant_process):
    a+=q.get()

print(a)
#get<=put must have
