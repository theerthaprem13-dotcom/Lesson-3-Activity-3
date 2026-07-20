#Create a tuples with different data types

tuplex=("tuples",False,3,2,1)
print(tuplex)

#Create a tuple

tuplex=(4,6,7,5,3,2,1,6)
print(tuplex)

#Tuples are immutable,so u cannot add new 

tuplex=tuplex+(9,)
print(tuplex)

print(tuplex.count(3))

#Slicing

_slice=tuplex[3:5]
print("the value of slice is",_slice)

