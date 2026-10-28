# def reverse(num):
#     rev=0
#     while num>0:
#         a=num%10
#         num//=10
#         rev=rev*10+a
        
#     return rev

# print(reverse(1234))

#postional argument
def multiply(a,b,c,d):
    print(f"{a}*{b}*{c}*{d}={a*b*c*d}")

multiply(2,3,4,5) # 2 goes to a 3 goes to b 4 goes to c 5 goes to d

#default arguments
def addition(a,b,c=12):
    print(a+b+c)


addition(5,4)  # if c not given its default value is 12

#Keyword arguments
addition(b=5,a=6,c=7) #giving both variable name in argument and values so position doesnt matter