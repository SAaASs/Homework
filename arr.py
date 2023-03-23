import array
import time
import numpy as np
import collections
start = time.time()
ddd = collections.deque(range(1,101))
for i in range(1,100):
    ddd[i] = ddd[i] *10
end = time.time()
print(ddd)
print(end)
start = time.time()
aaa = array.array("i")
for i in range(1,101):
    aaa.append(i)
for i in range(1,100):
    aaa[i] = aaa[i] *10
end = time.time()
print(aaa)
print(end)
start = time.time()
sss = []
for i in range(1,101):
    sss.append(i)
for i in range(1,100):
    sss[i] = sss[i] *10
end = time.time()
print(sss)
print(end)
start = time.time()
www = np.array([])
for i in range(1,101):
    www = np.append(www, i)
for i in range(1,100):
    www[i] = www[i] *10
end = time.time()

print(www)
print(end)


hh = np.arange(2,101,1).reshape(33,3)
print(hh)
hh2 = np.ones((8,8))
for i in range(0,8,2):
    for u in range(1, 8, 2):
        hh2[i][u] = 0
for i in range(1,8,2):
    for u in range(0, 8, 2):
        hh2[i][u] = 0
print(hh2)
hh3 = np.ones((8,8))
for i in range(0, 8):
    for u in range(i, 8):
        hh3[i][u] = 0
print(hh3)
hh4 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
hh44_1 = np.array([[],[]])
for i in range(0,4):
    for u in range(0,2):
        np.append(hh44_1[u],hh4[i][0:2])

print(hh44_1)
