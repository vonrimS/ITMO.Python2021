import math
from statistics import mean
from statistics import median
from statistics import stdev
from random import randint

x = range(1, 11)
array = []
for i in x:
    array.append(i)

print(array)

#print(dir(math))
#help(math)

sumnums = sum(x)
print(sumnums)

avgnums = mean(x)
print(avgnums)

mediannums = median(x)
print(mediannums)

stdevnums = stdev(x)
print(stdevnums)

x = int(randint(1, 100))
print(x)