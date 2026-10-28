# #List

# a=[12,23,33,4,56,77,98]
# print(a)
# print(type(a))
# print(a[3])
# #list are ordered means it is stored contineously in RAM
# #list are mutable
# #list can have duplicate values
# #Accesed by index


# #list methods
# a.append(20)
# print(a)
# print(dir(list))
# print(a.index(20))
# print(a.count(23))
# print(a.pop(2))
# #append
# # insert
# # remove
# # pop
# # copy 
# # extend
# # Sort 
# # clear
# # reverse
# #count



# lst=[3,-1,4,-5,9]
# lstPositive=[]
# lstNegative=[]
# for i in lst:
#     if i<0:
#         lstNegative.append(i)
#     else:
#         lstPositive.append(i)


# print(f"positive= {lstPositive}")
# print(f"Negative = {lstNegative}")


# lst=[10,20,30,40]
# sum=0
# for i in lst:
#     sum+=i


# print(f"Average of element in list is: {sum/len(lst)}")

# lst=[4,8,2,9,1,9]
# max=lst[0]

# # for i in range(len(lst)):
# #     if(max<=lst[i]):
# #         secMax=max
# #         max=lst[i]
#     elif i>secMax:
#          secMax=i
         
    
# print(f"Greatest element in list is: {max,secMax}")

# def checkSort(lst):
#     for i in range(len(lst)-1):
#         if(lst[i]>lst[i+1]):
#             return False
    
#     return True

# a=checkSort([1,9,5,7])
# print(a)        