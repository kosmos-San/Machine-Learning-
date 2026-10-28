# # #class:-A class is a blueprint for creating a objects

# # #objects:-Object are instances of classes

# # class car:
# #     a=12 #attribute
# #     def hello(): #Method
# #         print("Hello how are you")


# # print(car.a) # you can access attribute and methods after accessing the class
# # car.hello()  # Accessing method

# # a=car
# # a.hello()
# # a.a=23
# # b=car
# # print(b.a)
# # print(a.a)


# # class Clothes:
# #     name ="Rika & Co."
# #     def details(self):
# #         print("Hello this is a company that creates clothes")



# # shiya=Clothes()
# # print(shiya.name)
# # shiya.details()


# # class bags:
# #     material=""
# #     def __init__(self,material,zips,pockets):
# #         self.material=material
# #         self.zips=zips
# #         self.pockets=pockets


# # rebook=bags("leather",3,2)
# # print(rebook.material)

# # a=bags("polyester",4,6)

# # print(a.material)



# # class Animal:
# #     a=12 #class attribute

# #     def __init__(self,name):
# #         self.name=name #instance/object attribute
    
# #     def hello(self):  #instance method/object method
# #         print("How are you")
    
# #     @classmethod   #class method
# #     def deatils(self):
# #         print("Moshiiii moshiiiii")
# #         self.ayu=12

# #     @staticmethod  #This is a static method and it will not target any location
# #     def speak():
# #         print("HEllpppppooo")




# # obj=Animal("Lion")
# # obj.hello()
# # Animal.deatils()
# # obj.deatils()
# # Animal.ayu=13
# # obj.ayu=15
# # print(obj.ayu)
# # print(Animal.ayu)
# # obj.speak()

        

# #Inheritence

# # class Animal:  #parent class
# #     def __init__(self,name):
# #         self.name=name

# #     def details(self):
# #         print(f"Hello your name is {self.name}")

# # class humans(Animal):  #child class
# #     pass


# # obj=Animal("Lion")

# # obj2=humans("jai")

# # obj2.details()

# #your child class object has all the power to access the attribute and methods of parents class


# # class BagFactory:
# #     def __init__(self,material,zips,pockets):
# #         self.material=material
# #         self.zips=zips
# #         self.pockets=pockets

# #     def details(self):
# #         print(f"Your bag details are: ")
# #         print(self.material)
# #         print(self.zips)
# #         print(self.pockets)

# # class Reebok(BagFactory):
# #     def __init__(self, material, zips, pockets,color):
# #         super().__init__(material, zips, pockets)
# #         self.color=color
# #     def details(self):
# #         super().details()
# #         print(self.color)
       
# # bag1=BagFactory("Leather",3,4)

# # bag2=Reebok("polyster",5,6,"red")

# # bag2.details()

# # class campus(Reebok):
# #     def __init__(self, material, zips, pockets, color,CustomName):
# #         super().__init__(material, zips, pockets, color)
# #         self.Custom=CustomName
# #     def details(self):
# #          super().details()
# #          print(self.Custom)

# # obj3=campus("obsidian",4,2,"pitch black","Aman chan") #this is multilevel inheritence
# # obj3.details()


# #polymorphism:

# # def hello(): #1st hello function
# #     print("How are you")


# # def hello(name): #2nd Hello function
# #     print(f"What are you doing Mr.{name}")


# # hello() #2nd hello function overrides 1st hello function as phyton is interpreted line by line even when the perameter pass inside the function are different

# #so how can we achive function overriding in phyton like other compile time languages ans:-By using class a

# # class Animal:
# #     b=15
# #     def __init__(self,name):
# #         self.name=name
    
# #     def details(self):
# #         print(f"Your name is {self.name}")
        

# # class human(Animal):
# #     a=12
# #     def __init__(self, name):
# #         super().__init__(name)

# #     def details(self):
# #         print("This is human function and your name is ",self.name)
# #         print(super().b)


# # obj=human("Aman")

# # obj.details()
# # # Method overloading is not allowed in phyton


# #Encapsulation:
# class factory:
#     # name="Kia"  #public class attribute
#     _old=12 #protected if we use underscore,but in phyton protected does not exist this variable can still be access by object.....so using underscore is just a naming convection that is use to show developer that this is a protected variable even thought it is not so yes wtf 

#     __name="Kia" #private attribute now no one can access this variable
#     def __init__(self,type,tyre,color):
#         self.color=color  #public object attribute
#         self.type=type
#         self.tyre=tyre


# obj=factory("sedan","MRF","black")

# obj.name="Maruti"
# # print(obj.name)  #problem any one can access name if object is made so how to keep it safe by using __ and make it private
# # print(factory.__name)


    

    
#Abstraction:
# python does not have abstraction so we have to import an library to achieve it

# from abc import ABC,abstractmethod #this library help to achive abstraction

# class enforce(ABC):
#     @abstractmethod
#     def enginestart():
#         pass

# class bike(enforce):
#     pass
# class car(enforce):
#     pass


# obj=bike() #error will be shown as it is important to define engine function in bike as it has inherit enforce which is abstract class



#Dunder Method
#Dunder method are special type of method that are started with double underscore and end with double underscore just like __init__ function we dont have to call these function they automatically get called when certain action are applied on object

# class Animal:
#     def __init__(self,name): #dunder method that get invoke automatically when object is created
#         self.name=name

    
#     def __str__(self): #dunder method that automatically is invoke when obj is called
#         return f"My name is {self.name}"
    


# obj=Animal("Lion") 
# print(obj)

