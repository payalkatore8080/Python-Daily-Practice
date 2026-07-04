#List#  #for last position always last-1 like(5-1)


# mylist=["prashant","Ashish","Komal","ankush","Anhish",77,"sandip",60.52,"prashant"]

# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])#"Ankush","Ankush",77,60.52   in this position last element to increament by 2 if negative decreament
# print(mylist[:])
# print(mylist[::-1])

# mylist[2]="Akshay"  # modification
# print(mylist)

# if "ankush" in mylist:# check 
#     print("yes ankush is available")
# else:
#     print('not avilable')

# mylist.append('harsh')  # add at last in list
# mylist.append("laxman")
# print(mylist)


# mylist.insert(1,"sanket")  #insert at list always remmber two position require one is index another is name to insert
# print(mylist)


# mylist.remove("sandip")  #remove 
# print(mylist)


# newlist=mylist.copy()  #cloning
# print(newlist)

#-------------------------
#multidimensional list

# mylist=[['prashnt','jha'] ,['85.56'],[440022,"yyy"]]
# print("example of multidimentional list:")
# print(mylist)
# #print(mylist[row][col])
# print(mylist[0][0]) #prashant
# print(mylist[0][1]) #'jha'
# print(mylist[1][0]) #'85.56
# print(mylist[2][0]) #40022
# print(mylist[2][1]) #'yyy'
#--------------------------------------


# list1=["prahant","jha"]
#  print(list1*2)   #it will print two times
# list2=[50,25.50]
# print(list1+list2)
#----------------------

# list2=[50,25.50,'prashant']
# del list2[2] usint del we can delelte te index value
# del list2
# print(list2)
#-----------------------

#clear method list 
# list2=[50,25.50,'prashnt'] #[]
# list2.clear()
# print(list2)

#-----------------------
#string convert into list

# name="prashant" #str
# print(name)
# myname=list(name)#typecastinng
# print(myname)
#we have used list costructor

#------------------------------------------------
#reverse method

# mylist=[40,50,20,30]
# mylist.reverse()
# print(mylist)

#---------------------------------
#sorting example

# mylist=[44,22,77,0,88]
# mylist.sort(reverse=True)#reverse=True if we want to reverse string but write insting braket
# print(mylist)
 #defalut sorting order for number is acending order
#default sorting order for sting is alphabbatical
#we should lnnow  that llst should contIN HOMOGEneos
#data otherwisse we will get typeerroe
#python 2 first sort number then string follow
#-----------------------------------------
#Alising**********************
#alising means assining one variable reference to another
#variable
# mylist=[44,22,77,0,9,88]
# newlist=mylist
# print(id(mylist))
# print(id(newlist))
# mylist[0]="prshant"
# print(mylist)
# print(newlist)

#----------------------------------------------------------
#membership operator
#1.in  2. not in
#example
# name="heplp4code"
# print("h" in name) #check it present or not
# print("z" not in name)
#------------------------------------------------------------
#for(initialization:condition:inc/dec)
# for i in range(5): #i=0 start from 0 and chect 0is less thant 5
#     print(i) 

# for i in range(1,5): #i=1
#     print(i)    

# for i in range(1,10,2): #i=1 to 10 and increament by 2
#     print(i)    

# for i in range(5,0,-1):#i=5
#   print(i)

# for i in range(1,11):#i=1 #2 table
#     print(2*i)

# for i in range(1,11):
#      print(2*i, " ", 3*i ," ",4*i," " ,5*i," " ,6*i," " ,7*i," " ,8*i," " ,9*i," " ,10*i," ")
# print("------------------------------------------------")
# for j in range(1,11):    
#      print(11*j, " " ,12*j, " ",13*j, " ",14*j," " ,15*j ," ",16*j, " " ,17*j, " " ,18*j," " ,19*j," " ,20*j," ")



#----------------------------------------------------
# list3=[10,20,30,40,50]

# for i in list3: #i=0:10
#     print(i)

#------------------------------------------------------

# list =[1,2,3,4,5,6,7,8,9,10]
# sum=0 #sum=0
# for x in list: #x=1
#     sum=sum+x
#     print("the sum =",sum)
#-------------------------------------------
# mycart=[10,20,200,300,800,60,700]
# for i in mycart:#i=0:10
#     if i>400:
#         print("this is my purchase cart item")
#         break
#     print(i)
#----------------------------------
# count=0
# for i in range(9):#i=0
#     if i%2==0:
#         print(i)
#     else:
#         print(i)
#         count+=1
# print("count=",count)       
#----------------------------------

# rollno=[3,5,7,1,11,4,5,2]
# for x in rollno:#x=0:3
#     if x==2 or x==4 or x==6 or x==8 or x==10:
#         print("even no is found",x)
#         break

#-----------------------------------------------------
#WaP to accept any one day and check it is weeked or working day
#mon-friday(Working )
#sat,sun(weekend)

# day=(input("enter the day"))

# if day== "sturday or day==SUNDAY" or day=='SATURDAY' or day=='sunday':
#     print("Weekend")
# else:
#     print("working day")
#------------------------------------------
#reverse


# num=123#321
# a=num%10#3
# num=num//10#12
# b=num%10#2
# c=num//10#1
# rev=a*100+b*10+c*1  #300+20+1
# print("reverse =",rev)




# num=1234567
# a=num%10#7
# num=num//10 #123456

# b=num%10#6
# num=num//10 #12345

# c=num%10#5
# num=num//10 #1234

# d=num%10#4
# num=num//10 #123

# e=num%10#3
# num=num//10 #12

# f=num%10 #2
#num=num//10
# g=num%10 #1
# rev=a*1000000+b*100000+c*1000+d*100+e*10+f*10+g
# print("reverse =",rev)


#-------------------------------
#wap for change calculation with respect to total 

# Amount=int(input("please enter the amount for withdarow :"))#789
# print("100 notes=",Amount//100)
# print("50 notes=",(Amount%100)//50)
# print("20 notes=",((Amount%100)%50)//20)
# print("10 notes=",(((Amount%100)%50)%20)//10)
# print("5 notes =",((((Amount%100)%50)%20)%10)//5)
#------------------------------------------------------------------
#WAP to accept three age and check maximum age and print

# age1=int(input("enter the age1="))
# age2=int(input("enter the age2="))
# age3=int(input("enter the age3="))

# if age1 > age2:
#     if age1>age3:
#         print("age1 is greater",age1)
#     else:
#         print("age3 is greater",age3)   
# else:
#     if age2> age3:
#         print("age2 is greater",age2)
#     else:
#         print("age3 is greater",age3)             


#WAP  to accept any one character and check the enter character is UPPER CASE,LOWER CASE,DIGIT ,SPECIAL SYMBOL so print meg with respect to the entered charater

#using mehod
# a=input("enter the character=")

# if a.isupper():
#     print(" character is uppercase")
# elif a.islower():
#     print(" character is lowercase") 
# elif a.isdigit():
#     print("digit")
# else:
#     print("special symbol")           


#-------------------------------------------another method using asscii
# ch=ord(input("enter any chracter"))#0=48

# #ord fuction used to convert in ASSCII code
# if ch>=65 and ch<=91:
#     print("your enter charcter is in uppercase")
# elif ch>97 and ch<122: #a=97
#     print("your enterd chracter is in lowercase")
# elif ch>=48 and ch>=57:
#     print("your entered chracter is digit")        
# else:
#     print("your entered chracter is special symbol")        


#--------------------

# username=input("Enter Username:")#prashant
# passward=input("Enter Passward ")#prashant
# if username==passward:
#     print("login successful")
# else:
#     print("Invalid passward") 

#------------------
# while  True:
#     username=input("Enter Username:")#prashant
#     passward=input("Enter Passward ")#prasha
#     if username==passward:
#         print("login successful")
#     else:
#         print("Invalid passward") 


#---------------
#note =find() return starting index number of string if it is found else if string does'nt exit then it return -1
# s="help4code is a best platform for practicing programming"

# print(s.find("help4code"))
# print(s.find("python"))
# print(s.find("programming"))
#-----------------------
#use of join fuction

# s="prashant","ashish","sandip"
# m='|'.join(s)
# print(m)
#--------------------------

# s="Python is High level programming language"

# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())


#-----------------------------------------------------------
# format fuction

# print('Subject Marks:')
# phy=50
# chem=60
# math=70
# print("physics={} chemistry={} Math={}".format(phy,chem,math))
# print("physics={0} chemistry={1} Math={2}".format(phy,chem,math))
# print("physics={x} chemistry={y} Math={z}".format(x=phy,y=chem,z=math))
# total=phy=chem+math
# print("Total Marks", f"{total}")
# print("Roll No=","7".zfill(4))
      

#----------------------------------------------------------
#example of traversing
# name="hepl4code"
# for i in name:
#     print(i)
#--------------------------------------------

# name="prashant"
# i=0 #0:p
# for x  in name:
#     if x=='n':
#         print("Chracter present at index no ",i,"value=:",x)
#         break
#     i=i+1 #update by one

#--------------------------------------------
#logical reasoning 
# a='shiwaleew'
# for i in a:
#     if i=='w':
#      print(i)
#----------------------------
# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x!=z)


#BODMAS
# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d)#160
# print((a-b)*(c/d))#40
# print(a+(b*c)/d)#110

#--------------------------------
#Removing spaces from the string
#1.rstrip()=====> To remove spaces at right hand side 
#2.lstrip()=====> to remove spaces at left hand side
#3strip()========>to remove spaces both side

# city=input("Enter our city name:")
# scity=city.strip()
# if scity=='Hederabad':
#     print("Helloe Hydrabadi...Adab")
# elif scity=='Chennai':
#     print("Hello Madrasi..Vanakkam")
# elif scity=="Bangalore":
#     print("Hello Kannadiga..Shubhodaya")
# else:
#     print("your entered city is invalid") 
#--------------------------------------------------------
#Replaciing a string with another string

#s.replace(oldstring.newstring)
#inside s,every occurance of old string is replace with new string

# s=""
# s1=s.replace("difficult","easy")
# print(s1)

#all accurance will be replaced
# s="ababababababa"
# a1=s.replace("a","b")
# print(s1)


#---------------------------------------------
