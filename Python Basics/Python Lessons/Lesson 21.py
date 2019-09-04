#Lesson 21: Iterator as Ip of functions
#using *args and *kwargs, we can provide flexible number of params to func. same.
print(range(5))
print(*range(5))

varA = map(lambda varX: varX * varX, range(5))
print(*varA)
#Lets use Zip and unzip func
varL1 = (3,7,6,6,0)
varL2 = ("a","B", "CR","hd","lol")
print(varL1, varL2)
varZ = zip(varL1,varL2)
print(*varZ)
#unzip Z, have to assign varZ again else error.lets assign in reverse.
varZ = zip(varL2,varL1)
varX, varY = zip(*varZ)
print(varX,varY)

#Specialized iterators: itertools
#permutations, combinations & product. we have used count already in last lesson
from itertools import permutations
p = permutations(range(3))
print("permutation of 0-2:", *p)
from itertools import combinations
c = combinations(range(3), 2)
print("combinations of 0-1 & 2:", *c)
from itertools import product
po = product(range(3), 'ao')
print("product of 0-2 & ao :", *po)
