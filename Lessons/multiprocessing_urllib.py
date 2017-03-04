import multiprocessing
import urlib.request

a=0
quant_process=2
q=multiprocessing.Queue()


def f():
    r=urlib.request("http://mail.ru")
    print(len(r.read()))

for i in range(quant_process):
    p=multiprocessing.Process(target=f)
    p.start()

print(a)
#get<=put must have
