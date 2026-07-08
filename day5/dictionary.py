# mydict={ 
#   101:"prashant",
#   102:"ashish",
#   "103":"mahini",
#   "104":"triveni",
#    101 :"ashish",
#    104:"ashish" 
# }
# print(mydict)
# print(type(mydict))
#with the help of key wew have to print values
# a=mydict[102]
# print(a)

##we will replace old value by new value
# mydict[102]="peter"
# print(mydict)


#by deafaliy looping statement access key
#only print key x=0,1
# for x in mydict:
#     print(x)

##only print values x=0
# for x in mydict.values():
#     print(x)

#printing key and values both
# for x,y in mydict.items():
#     print(x,y)

#if i have to ad new key and values pair in my dictionary
# mydict["mobile_no"]=464646438
# print(mydict)
#------------------------------------------------------------------------------
#imp:if we wnat to represent binary date like images ,vedio

# mydict={
#     101:"praashant",
#     "professional":"developer",
#     "empid":1001}
# mydict.pop(101)
# print(mydict)

#-------------------------
#copy fuction

# mydict={
#     101:"praashant",
#     "professional":"developer",
#     "empid":1001}
# newdict=mydict.copy()
# print(newdict)

#=================================================================
#task1
#check if a dictionay is empty

# mydict={}
# if mydict is not len(mydict):
#     print("empty")
# else:
#     print("not emptey")    


#------------------------------------------
#task2
#find the key with the maximun value in dictionay 

# mydict = {"A": 50, "B": 30, "C": 70}

# result=max(mydict)
# print(result)

#--------------------------------------------------
#reverse
# mydict = {"A": 50, "B": 30, "C": 70}
# rev={}
# for i in mydict:
#     rev[mydict[i]]=i
#     print(rev)

#-----------------------
#find common key-values pairs in two dictionaries
# mydict={"A":1,"B":2,"C":3}
# def mydict():
#     if i in mydict:
#         if mydict==mydict.values():
#             print()