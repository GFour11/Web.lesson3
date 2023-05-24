import logging
from time import time
import concurrent.futures

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def factorize(num):
    result=[]
    for j in range (1,int(num)):
        if not num%j:
            result.append(j)
    result.append(num)
    return result


if __name__ == '__main__':
    a,b,c,d = (128, 255, 99999, 10651060)
    tup = (a,b,c,d)
    time1=time()
    for i in map(lambda x:factorize(x), tup):
        print(i)
    time2 = time()
    print(time2 - time1)
    arguments = [a,b,c,d]
    time1 = time()
    with concurrent.futures.ProcessPoolExecutor(4) as executor:
        for result in zip(executor.map(factorize, arguments)):
            print(result)
    time2 = time()
    print(time2 - time1)
