#lesson 16 lambda functions
#short way to define function
def fun1(varA=5):
	return varA * varA
print("fun1 is ", fun1())
#simulate this in lambda
fun2 = lambda varB = 4 : varB * varB
print("fun2", fun2())
#same for parameters
print("fun1(9) is ", fun1(9))
print("fun2(9) is ", fun2(9))
#functions can be passed as parametee to functions, use lambda then.
dictA = [{"id":"p1", "age":29},
               {"id":"p2", "age":26},
               {"id":"p3", "age":24}]
print("dictionary is", dictA)
#there is sorted function to sort the data but it fails with dictionaries. it requires a key.
dictB = sorted(dictA, key= lambda item : item["age"])
print("Sorted dictionary by age is", dictB)




