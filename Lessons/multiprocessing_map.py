import multiprocessing
import urllib.request

def f(url):
    r=urlib.request(url)
    return len(r.read())

p=multiprocessing.Pool(5)
print(p.map(f,['http://mail.ru']*20))

#функция создается до пула, пул готовое решение использование процессов с возвратом значений, но он вернет когдавсе посчитается
#не надо использовать очереди
