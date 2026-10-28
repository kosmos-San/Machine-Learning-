# # # # # # #range function
# # # # # # # range(10,51,1)

# # # # # # # for i in range(1,10000,1):
# # # # # # #     print(i,":- Rittu no baka")



# # # # # # # num=int(input("Enter the number: "))
# # # # # # # for i in range(1,11,1):
# # # # # # #     print(f"{num}*{i}={num*i}")

# # # # # # #for loops in string 

# # # # # # # name="Ayushman barthwal"
# # # # # # # for i in range(len(name)):
# # # # # # #     print(name[i])


# # # # # # # #second method

# # # # # # # for char in name:
# # # # # # #     print(char)


# # # # # # # question 1:
# # # # # # n=int(input("Enter a number: "))
# # # # # # for i in range(n):
# # # # # #     print(f"{i}: Radhe Radhe")


# # # # # # num=int(input("Enter the number: "))
# # # # # # for i in range(1,num+1):
# # # # # #     print(f"{i}")

# # # # # num=int(input("Enter a number: "))
# # # # # for i in range(num,0,-1):
# # # # #     print(i)


# # # # num=int(input("Enter a number: "))
# # # # for i in range(1,11,1):
# # # #     print(f"{num}*{i}={num*i}")


# # # num=int(input("Enter a number: "))
# # # sum=0
# # # for i in range(1,num+1):
# # #     sum+=i

# # # print(f"The sum of {num} natural number is: {sum} ")

# # num=int(input("Enter a number: "))
# # fact=1
# # for i in range(num,0,-1):
# #     fact*=i

# # print("Factorial of ",num,"is: ",fact)

# # sum1=0
# # sum2=0
# # n=int(input("Enter the number: "))
# # for i in range(0,n+1,1):
# #     if i%2==0:
# #         sum2+=i
# #     else:
# #         sum1+=i

# # print(f"The sum of even natural number is: {sum2}")
# # print(f"The sum of odd natural number is: {sum1}")


# # num=int(input("Enter the number :"))
# # for i in range(1,num+1,1):
# #     if num%i==0:
# #         print(f"{i} is factor of {num}")

# # num=int(input("Enter a number:-"))
# # sum=0
# # for i in range(1,int(num/2+1),1):
# #     if num%i==0:
# #         sum+=i


# # if sum==num:
# #     print(f"{num} is a prefect number")
# # else:
# #     print(f"{num} is not a prefect number")


# # num=int(input("Enter a number:- "))
# # flag=False

# # for i in range(2,int(num/2+1),1):
# #     if(num%i==0):
# #         flag=True
# #         break
# # else:
# #     print("Number is prime")


# # if flag==True:
# #     print("number is not prime")


# # str=list(input("Enter a String: "))

# # for i in range(int(len(str)/2)):
# #     temp=str[i]
# #     str[i]=str[len(str)-i-1]
# #     str[len(str)-i-1]=temp


# # print(str)

# str=input("Enter a string: ")

# for i in range(len(str)):
#     if str[i]!=str[len(str)-i-1]:
#         print("not palindrome")
#         break

# else:
#     print("plaindrome")

a="P@#yn26at^&i5ve"
char=0
spchar=0
digit=0

for i in a:
    if i.isdigit():
        digit=digit+1
    elif i.isalpha():
        char=char+1
    else:
        spchar+=1


print(f"char {char}, special character {spchar}, digit {digit}")
