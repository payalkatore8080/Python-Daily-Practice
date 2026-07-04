# class Student:
#     #data member
#     rollno = 101

#     def msg(self):#member function
#         print("hello world")

# obj= Student()  #can't print object direct first in convert into hexadecimal then assign to object
# print(obj.rollno)
# obj.msg() 

#==================================================================================================
# class Demo: #for one object only one constructor call
#     def __init__(self):#self is default argument used instead od this to show current property,input and output purpose
#        print("i am a constructor and i always called first ")

#     #instance method
#     def info(self):
#         print("one object")
# obj = Demo()
# obj.info()
# obj2=Demo()    

#==============================================================================================

# class Hod:
#     def __init__(self): #constructor
#         self.name='payal'
#         self.age=53
#         self.empid=1001
#     def info(self): # instance method
#         print("My name is:",self.name)
#         print("My age is:",self.age)
#         print("My emp id:",self.empid)    
# obj = Hod()#object create
# obj.info()


#============================================================================================================

# class Hod:
#     def __init__(self,name,age,rollno):#parametric constructor
#         self.name=name
#         self.age=age
#         self.rollno=rollno

#     def show(self):
#         print('name =',self.name)
#         print('age=',self.age)
#         print('rollno=',self.rollno)    
# obj=Hod('payal',45,102)     
# obj.show()   

#=================================================================================================================


#instance variable depend on object example student record
# class New:
#     def __init__(self):
#         self.a=10
# obj1=New()
# obj2=New()
# obj3=New()
# obj1.a=20 #modification
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

# ============================================================================================== 

#static variable not depend on variable ,example clg name if change it change for all

# class New:
#     a=10
#     def  __init__(self):
#         self.name='payal'

        
# obj1=New()
# obj2=New()
# obj3=New() 
# New.a=50
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)       

#=====================================================================================


# class College:
#     collegename ="Modern College"#static variable
#     def __init__(self):
#         self.studentname="payal" #inatce variable

# principal=College()
# teacher=College()   
# accountant= College() 

# print("principle=",principal.collegename )
# print("teacher=",teacher.collegename )
# print("accountant="accountant.colletname)
# print("principle=",principal.studentname)
# print("teacher=",teacher.studentname)
# print("accountant="accountant.studentname)

# College.collegename="HBD"
#code incomplete


#=========================================================================================

# class Student:
#     def __init__(self):
#         self.s_name =input("Enter your name")
#         self.s_rollno=101#instance var

#     def getdata(self):
#         self.s_mb=2828282828282    
# obj=Student()        
# obj.getdata()
# obj.s_branch="CS" # adding instsnce variable using obj
# del obj.s_rollno  #delete a instsnce variable
# print(obj.__dict__)

#=========================================================================================

#static method

# class Student:
#     #by using class name we can access static method
#     @staticmethod 
#     def get_personal_detail(firstname,lastname):
#         print("your personal detail=",firstname,lastname)

#     @staticmethod 
#     def contact_detail(mobileno,rollno):
#         print("your contact detail=",mobileno,rollno ) 

# Student.get_personal_detail("payal","katore")
# Student.contact_detail(7664644,1010)


#========================================================

#Single level inheritance(used for reusbility)

# class College:#parent class
#     def college_name(self):
#         print("Modern college")

# class Student(College):#child class
#     def student_info(self):#member fuction
#         print("Name: payal")
#         print("Branch:it")

# obj=Student()#object create child class
# obj.college_name()
# obj.student_info()        



#-----------------------------------------------------------
#multiple inheitance

# class College:#first class-class
#     def college_name(self):
#         print("Modern college")

# class Student(College):#second class secon-level
#     def student_info(self):
#         print("Name: payal")
#         print("Branch:it")

# class Exam(Student):#child class
#     def subject(self):
#         print("subject1: Design engineering")
#         print("subject2: Math")
#         print("Subject3: c language")        

# obj=Exam()#object create child class
# obj.college_name()
# obj.student_info()  
# obj.subject()      

#-------------------------------------------------------

#multiple inheritance



# class SubMarks:#class-1
#     math=int(input("enter paper marks of math"))
#     DE=int(input("enter the paper marks of DE"))
#     c=int(input("enter the paper marks of c"))
#     english=int(input("enter te paper mmarks of english"))

# class PracMarks:
#     cpract=int(input("enter practical marks of c language:"))

# class Result(SubMarks,PracMarks):
#     #print("if student pass in both =subject and practical then pass")
#     def total(self):
#         if self.math>=40 and self.DE>=40 and self.c>=40 and self.english>=40 and self.cpract>=20:
#             print("pass")
#         else:
#             print("fail")
# obj=Result()
# obj.total()            

#----------------------------------------------------------------------------
#Abtraction method
# from abc import ABC, abstractmethod
# class Help4code(ABC): #abstract class  
#     @abstractmethod #decorator
#     def training(self):#abstract method
#         pass

#     @abstractmethod  #abstract method
#     def placement(self):
#         pass

# class Ashish(Help4code):#SLH
#     def training(self):
#         print('c,c++,Java')
#     def placement(self):
#         print("Java placement")

# class Ankush(Help4code):#SLH
#     def training(self):
#         print('Python |dijango')
#     def placement(self):
#         print("Python placement student")                

# class Prashant(Help4code):#SLH
#     def training(self):
#         print('Machine learning')
#     def placement(self):
#         print("Data science placement")

# obj1=Ashish()
# obj1.training()
# obj1.placement()

# obj2=Ankush()
# obj2.training()
# obj2.placement()

# obj3=Prashant()        
# obj3.training()
# obj3.placement()

#-----------------------------------------
# from abc import ABC, abstractmethod
# class Irctc(ABC):#abtrct class
     
#      @abstractmethod
#      def bookmytiket(self):#abtract method
#           pass
     
# class Makemytrip(Irctc): 
#      def bookmytiket(self):
#        print("============")
#        print("Welcome to makemy trip.com")
#        self.source =input("enter a source station")  
#        self.destination=input("enter a destination")
#        self.date =input("enter the date")

# class Yatra(Irctc): 
#      def bookmytiket(self):
#        print("============")
#        print("Welcome to makemy trip.com")
#        self.source =input("enter a source station")  
#        self.destination=input("enter a destination")
#        self.date =input("enter the date")

# class GoIbibo(Irctc): 
#      def bookmytiket(self):
#        print("============")
#        print("Welcome to makemy trip.com")
#        self.source =input("enter a source station")  
#        self.destination=input("enter a destination")
#        self.date =input("enter the date")

# m=Makemytrip()
# m.bookmytiket()
# g=Yatra()
# g.bookmytiket()
# y=GoIbibo()
# y.bookmytiket()
#========================================================
#in this code show overloading
# class Arithmatic:
#     def add(self,a):
#         print(a)
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c) 

# obj=Arithmatic() 
# obj.add(10)
# obj.add(10,20)
# obj.add(10,20,30)              
#=======================================================
#overloading python ex
# class Arithmatic:
#     def __init__(self):
#         print("therre is no argument")
#     def __init(self,a):
#         print("passing one argument")
#     def __init__(self,a,b):
#         print("passing two argument")        

# obj=Arithmatic()
# obj=Arithmatic(10)
# obj=Arithmatic(2,2)
#=============================================================

#runtime polymorphism=execute usinng overriding
# class Rbi:#parent class
#     def homeloan(self):
#         print("Home loan rate of innternet 8%")

#     def carloan(self):
#         print("Car rate of interesr 7%")  

# class Sbi(Rbi):#child class
#     def homeloan(self):
#         print("Home loan rate of interest 10.5%")
#         super().homeloan()  #we can access rbi class in child class using this  

# sbiobj=Sbi()
# sbiobj.homeloan() 
#======================================================
#constructor overriding
# class Father:
#     def __init__(self):
#         print("father:=i am on time at breakfast table")

# class Child(Father):
#     def __init__(self):
#         print("child:=i will be late for breakfast")
#         #super().__init__()
# obj=Child()#in this it will print only child class message but using super we print or call parent class
#===============================================================

# class Base:
#     def __init__(self):
#         print("Parent class constructor called")
#         self.a="prashant"#public data member
#         self.__c="Ashish" #private member
#  #creating a derived class\child class
# class Derived(Base): #child class 
#     def __init__(self):
#         #calling constructor of base class
#         Base.__init__(self)
#         #print("calling private member of base class:")
#         # print(self.a)
#         # print(self.__c)
# # obj1=Derived()
# # print(obj1.a)
# # print(obj1.__c)
# obj2 =Base()
# print(obj2.a) #Accessible 
# print(obj2.__c) #not accessible      

#                


#===============================================================================

# class Base:
#     def __init__(self):
#         print("Parent class constructor called")
#         self.a="prashant"#public data member
#         self._c="Ashish" #protected member
#  #creating a derived class\child class
# class Derived(Base): #child class 
#     def __init__(self):
#         #calling constructor of base class
#         Base.__init__(self)
#         #print("calling protected member of base class:")
#         # print(self.a)
#         # print(self.__c)
# # obj1=Derived()
# # print(obj1.a)
# # print(obj1.__c)
# obj2 =Base()
# print(obj2.a) #Accessible 
# print(obj2._c) #not accessible      
                
#===================================================


# class Rbi:
#     #declaring public method 
#     def publicPolicy(self):
#         print("Check the public of Rbi")

#     #declaring private method
#     def __privatePolicy(self):
#         print("There is some privte policy which is not accessible for public")

# class Sbi(Rbi):
#     def __init__(self):#first sbi class cannot called
#        Rbi.__init__(self)#seconf parent class constuctor

#     def callingPublicMethod(self):#child class public method
#         print("\inside child class") 
#         self.publicPolicy() #calliing parent class public method 

#     def callingPrivteMethod(self):#child class public method
#         self.__privtePolicy() #calling parent class privte method

# obj1=Sbi()
# obj1.callingPublicMethod()
# obj1.callingPrivteMethod()
# obj1.publicPolicy()
# obj1.__privatePolicy()

# obj2=Rbi()
# obj2.publicPolicy()
# obj2.__privatePolicy()
# obj2=Rbi()
# obj2.publicPolicy()
# obj2._Rbi__privatePolicy()          
               
#================================
#encapsulation
# class Person:
#     def __init__(self):
#        self.__name ="Geeks"
#        self.__age=10
        
#     def get_name(self):
#         return self.__name
        
#     def get_age(self):
#         return self.__age

#     def set_name(self, name):
#         self.__name=name
        
#     def set_age(self, age):
#         self.__age=age


# obj=Person()
# print(obj.get_name())
# obj.set_name("jhon")
# obj.set_age(30)
# print(obj.get_name())
# print(obj.get_age())

