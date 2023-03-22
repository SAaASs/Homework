import array
import time
import numpy as np
import matplotlib.pyplot as plt
import collections
start = time.time()
ddd = collections.deque(range(1,101))
end = time.time()
print(ddd)
print(end)
start = time.time()
aaa = array.array("i")
for i in range(1,101):
    aaa.append(i)
end = time.time()
print(aaa)
print(end)
start = time.time()
sss = []
for i in range(1,101):
    sss.append(i)
end = time.time()
print(sss)
print(end)
start = time.time()
www = np.array([])
for i in range(1,101):
    www = np.append(www, i)
end = time.time()


print(www)
print(end)

