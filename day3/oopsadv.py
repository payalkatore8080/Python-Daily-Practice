# #from engineering.first_year.first_sem import f2_sem
# #from Engineering.MCA.first_sem import first_subj
# #from engineering.MCA.second_sem import second_subj
# # importing modules from packages like subject name
# choice =0 # global variable
# class Exam(object):
#     def __init__(self):
#         self.sname=None
#         self.collegename=0
#         self.classname = 0
#         self.rollno =0
#         self.login()# calling function
        
#     def login(self):# constructor part (called function)
#             print("=========================")

#             username=input("Enter username")
#             password=input("Enter password")

#             print("=========================")
#             print()
#             # Login section
#             if username==password:
#                 print("Login successfully")
#                 self.getdata() # calling function
#             else:
#                 print("Login fail try again")
#  #=============================================================
#     print()
#     #Enter Your Profile Detail
#     def getdata(self):
#         self.sname      = input("Enter Your Name")
#         self.collegename= input("Enter Your College Name")
#         self.classname  = input("Enter Your Class Name")
#         self.rollno     = input("Enter Your Roll Number")
#         print()
#         #====================End Of Profile Section========================
#         # static subject declartion
#         print(" choose any branch for giving exam")
#         print("1. Mechanical Egineering")
#         print("2. Information Technology")
#         print("3. Computer Science")
#         print("4. Civil Engineering")
#         print()

#         choice = int(input("Enter your choice")) # subject selection logic part
#         if choice==1:
#             self.mechanical() # calling function
#         elif choice==2:
#             pass
#         elif choice==3:
#             pass
#         elif choice==4:
#             pass
#         else:
#             print("you have entered wrong choice")

#         # called function part
#     def mechanical(self):
#         print("1. First Semester")
#         print("2. Second Semester")
#         print("Enter your Semester Number")
#         # logical part
#         choice =int(input("Enter your choice"))
#         if choice == 1:
#             #first_subj()  # calling function
#             print("Math")
#         elif choice== 2:
#             pass #second_subj()

#     def information(self):
#         print("1. First Semester")
#         print("2. Second Semester")
#         choice =int(input("Enter your choice"))
#         if choice == 1:
#             pass
#         elif choice== 2:
#             pass

#     def computer(self):
#         print("1. First Semester")
#         print("2. Second Semester")
#         choice =input("Enter your choice")
#         if choice == 1:
#             pass
#         elif choice== 2:
#             pass

#     def civil(self):
#         print("1. First Semister")
#         print("2. Second Semister")
#         choice =input("Enter your choice")
#         if choice == 1:
#             pass
#         elif choice== 2:
#             pass

# #object creation of class
# #obj = Exam()
# #obj.login()
# #==================================================end=========================
# # Examination Calculation part
# class Calculation(object):
#     def __init__(self):
#         self.stat=0
#         self.dmgt=0
#         self.cg =0
#         self.toc =0
#         self.math=0
#         self.total=0
#         self.percentage=0
#         self.ps = 0
#         print()
#         print("Do You Want To Put Examination Marks Enter Yes/No")
#         print()
#         Yes = input("Enter yes/no")
#         if Yes == "yes":
#             self.calculatemarks() # calling function
#         else:
#             print("Thank You For Visiting Here")
#         print()
# # taking a marks for subject
#     def calculatemarks(self):                 
#         self.stat = int(input("Enter Marks Of Statistics:"))
#         self.dmgt = int(input("Enter Marks Of DMGT :"))
#         self.cg   = int(input("Enter Marks Of CG   :"))
#         self.toc  = int(input("Enter Marks Of TOC  :"))
#         self.math = int(input("Enter Marks Of Math1:"))
#         print()

#         if self.stat >=40 and self.dmgt>=40 and self.cg>=40 and self.toc>=40 and self.math>=40:
#             self.ps="pass"
#             print("You are pass")
#         else:
#             self.ps="Fail"
#             print("You are fail")
            
#         self.total = self.stat+self.dmgt+self.cg+self.toc+self.math
#         self.percentage = self.total/5.0


# #obj1 = Calculation()    
# #================================================================================

# #Assesment class

# class Assesment(Exam, Calculation): # multiple inheritance

#     def __init__(self):    # child class constructor
#         Exam.__init__(self)     # calling parent class constructor
#         Calculation.__init__(self)

#     def result(self):
        
#         print("===============================================================")
#         print("                                                               ")
#         print("         College Name: ",self.collegename ,"                   ")
#         print("                                                               ")
#         print("===============================================================")

#         print("|        Student Name: ",self.sname,  "                       |")
#         print("|        Class Name  : ",self.classname,"                     |")
#         print("|        Roll No     : ",self.rollno,      "                  |")
#         print("===============================================================")
#         print("                                                               ")
#         print(" Subject Name     :     Total Marks    :  Obtained Marks :     ")                
#         print("                                                               ")
#         print(" Statistic        :",   "   100   "   "      :",  self.stat,  ":")
#         print(" DMGT             :",   "   100   "   "      :",  self.dmgt,  ":")
#         print(" CG               :",   "   100   "   "      :",  self.cg,    ":")
#         print(" TOC              :",   "   100   "   "      :",  self.toc,   ":")
#         print(" Math             :",   "   100   "   "      :",  self.math , ":")
#         print("===============================================================")
#         print("                                                               ")
#         print("Result Status     :",                              self.ps,"   ")
#         print("Total Marks       :",      "500",                           "  ")
#         print("Obtained Marks    :",                          self.total,      )
#         print("Percentage        :",      self.percentage,               "    ")
#         print("===============================================================")

# obj2 = Assesment()
# obj2.result()


# #===========================================================================================================
# #exception handling in runtime error
#1

# try:
#     a=int(input("Enter value of A:"))
#     b=int(input("Enter the value od  B:"))
#     print(a/b)
# except ZeroDivisionError:
#     print("Can't divide by zero") 
# except ValueError:
#     print("Enter only integer value")    
# print("continue")       

#-----------------------
#exception handling 2
# try:
#     a=int(input("Enter value of A:"))
#     b=int(input("Enter the value od  B:"))
#     print(a/b)
# except ZeroDivisionError as message:
#     print(" Please ensure that you Can't divide by zero",message) 
# except ValueError as message:
#     print("Enter only integer value",message)    
# print("continue")
# ----------------------------------------  
#exception handling 3(single except block)
#handling multiple differnt kinds of exception with single block
# try:
#     a=int(input("Enter value of A:"))
#     b=int(input("Enter the value od  B:"))
#     print(a/b)
# except ( ValueError,ZeroDivisionError) as message:
#     print(message) 
#-------------------------------------------
#4
#i we havve requirement of multiple exception then  #
# in the situation default except block #
# should be in last other wise syntax error will encounter
# try:
#     a=int(input("Enter value of A:"))
#     b=int(input("Enter the value od  B:"))
#     print(a/b)
# except:
#     print("This is default part block")    
# except ( ValueError,ZeroDivisionError) as message:
#     print("enter a correct number":message)
#-------------------------------------------
#5 we  can use else block if no error will generate it is depend on our own need and neccessity 
# try:
#     a=int(input("Enter value of A:"))
#     b=int(input("Enter the value od  B:"))
#     print(a/b)
 
# except ( ValueError,ZeroDivisionError) as message:
#     print("enter a correct number",message)
# else:
#     print("Everything is ok")
#-----------------------------
# 6#used finally block
# try:
#     a=int(input("Enter value of A:"))
#     b=int(input("Enter the value of  B:"))
#     print(a/b)
 
# except ( ValueError,ZeroDivisionError) as message:
#     print("enter a correct number",message)
# finally:
#     print("I will always execute")
#------------------------------------------------
#7 nested try except block
#  
# try:
#     a=int(input("Enter value of A:"))
#     b=int(input("Enter the value of  B:"))
#     try:
#          print(a/b)
#     except ZeroDivisionError as msg: 
#          print(msg)    
 
# except  ValueError as message:
#     print(message)
#--------------
# try:
#     a=int(input("Enter value of A:"))
#     b=int(input("Enter the value of  B:"))
#     print(a/b)
 
# except ( ValueError,ZeroDivisionError) as message:
#     print("enter a correct number",message)
# else:
#     print("there are no eror in try block")    
# finally:
#     print("I will always execute")



#------------------------------------------
#types of exception handling
#user defined exception by raise keyword

# bank_bal=500
# if bank_bal<2000:
#     raise Exception("your account balance is below a access:")
# else:
#     print("your amount has withdrawl")

#==============================
#logging of python used to store application or exception exception file we should use logging of python


# import logging 

# logging.basicConfig(filename="newfile.txt",level=logging.DEBUG)
# logging.debug("this indicate the debugging information")
# logging.info("this indicate a improtant information")
# logging.error("this indicate a error information ")
# logging.warning("this indicate a warining information ")
# logging.critical("this indicate a critical information ")

#-----------------------------------------------------------------

# import logging
# logging.basicConfig(filename="secondfile.txt",level=logging.DEBUG)
# try:
#     a=int(input("Enter value of A:"))
#     b=int(input("Enter the value od  B:"))
#     print(a/b)
# except ( ZeroDivisionError ,ValueError) as message:
#     print(message)
#     logging.exception(message)
# print("Logging level is set up.check 'secondfile.txt',for log details")    
#=======================================================================================

#task write a program to three paper marks like phy,chem,math and calculate total,percentage and display total marks ,percentage and condition:
# if user is passed in all subject then print pass else print fail and passing marks is 40
# if percentage is greater then equal to 65 and gender is male the print you eligible for placement else not eligible for placement
# phy=int(input("enter the phusics marks"))
# chem=int(input("enter the marks of chem"))
# math=int(input("Enter the marks of math"))
# total =phy+chem+math
# percentage =total/3.0
# print("Total Marks:",total)
# print("Percentage :",percentage)
# if phy>=40 and chem>=40 and math>=40:
#     print("pass")
# else:
#     print("Fail")

# gender = input("Enter your gender M/F")
# if percentage>=65 and gender=='M':
#     print("you elligible for placement")
# else:
#     print("you are not elligible for placement")    
#-------------------------------------------------------------------
    
         