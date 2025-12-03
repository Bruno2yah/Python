# count é um iterador sem fim (itertools)
from itertools import count

c1 = count() # conta infinitamente
r1 = range(10) # tem um fim

for i in c1:
    print(i)