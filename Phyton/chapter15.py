# # # # # #Dictionary
# # # # # d={1:10,2:20,3:30,4:50}#LHS become key and RHS become value key becomes index here
# # # # # # so dictionary are list with custom indexes
# # # # # print(type(d))
# # # # # #Vanilla python
# # # # # print(d[3])
# # # # # d[50]=500  #creating a new key value pair
# # # # # print(d[50])
# # # # # d[1]="Ayushman" #Updating a key value

# # # # # #Methods Approach

# # # # d={1:10,2:20,3:30,4:50}
# # # # # d.clear()
# # # # print(d)

# # # # q=d.fromkeys([10,20],50)
# # # # print(q)

# # # # print(d.get(2))

# # # # print(d.items())

# # # # print(d.keys())

# # # # print(d.values())

# # # # # print(d.pop(2))

# # # # print(len(d))

# # # d1={"a":1}
# # # d2={"b":2}

# # # for i in d2:
# # #     d1[i]=d2[i]

# # # print(d1)

# # d1={"a":10,"b":20,"c":30}

# # sum=0
# # for i in d1:
# #     sum+=d1[i]

# # print(sum)


# li=["a","b","a","c","b","a"]
# d1={}
# for i in li:
#     if i in d1.keys():
#         d1[i]=d1[i]+1
#     else:
#         d1[i]=1


# print(d1)