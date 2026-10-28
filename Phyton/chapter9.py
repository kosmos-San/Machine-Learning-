#while loop
#Question 1:

# num=int(input("Enter a number:-"))
# while num>0:
#     a=num%10
#     num=int(num/10)
#     print(a)


# num=int(input("Enter a number: "))
# rev=0
# count=0
# while num>0:
#     a=num%10
#     num=num//10
#     rev=rev*10+a
#     count=count+1


# print(rev)


# number guessing game:

import random
tries=0
num=random.randint(1,100)
while True:
    tries=tries+1
    a=int(input("Try guessing the number: "))
    if a==num:
        print("Yheaaaa you gussed right")
        print("number of tries ",tries)
        break
    elif a>num:
        print("Try guessing low")
    else:
        print("Try guessing higher")