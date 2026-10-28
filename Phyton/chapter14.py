#unique values only
a={1,2,3} #use curely brackets
l=[1,1,1,1,1,2,2,2,3,3,3,3]
c=set(l)#Removed all duplicate values cool
print(c)
#set can only store hashable values means immutable data types like int,String,Truple but it cannot store list

print(dir(set))
s1={10,20,30,40}
s2={30,40,50,60}

print(s1.difference(s2)) 
print(s1-s2)
print(s1.union(s2))
print(s1|s2) 
print(s1.intersection(s2))
print(s1&s2)

print(s1.symmetric_difference(s2))
print(s1^s2)
