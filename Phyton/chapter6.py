# """age=int(input("Enter your age:- "))
# if age>=18 :
#     print("you are eligible for voting")
# else:
#     print("You are not eligible for voting")
# """

# num1=int(input("Enter first number:- "))
# num2=int(input("Enter second number:- "))
# if num1>num2:
#     print(num1,"is greater")
# elif num2>num1:
#     print(f"{num2} is greater")
# else:
#     print("Both the numbers are equal ")

# gender=input("Enter your gender:- ")
# if gender=='M' or gender=='m':
#     print("Good morning sir")
# elif gender=='F' or gender=='f':
#     print("good morning mam")


# num1=int(input("Enter the number:- "))
# if num1%2==0:
#     print(f"{num1} is even")
# else:
#     print(f"{num1} is odd")


year=int(input("Enter year: "))

if (year%4==0 and year%100!=0) or year%400==0:
    print(year," is leap")
else:
    print(year," is not leap")