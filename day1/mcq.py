#MCQ base quetion

#1
# a=[1,2,3,4,5,6,7,8,9]
# print(a[::2])
#---------------------
#2
# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60 #::means starting ,ending increament 2 
# print(a)  # syntatical issue 
#===========================================
#3
# a=[1,2,3,4,5]
# print(a[3:0:-1])
#---------------------------------------
#4
# def func(value,values):
#     var =1
#     values[0]=44
#     t=3
#     v=[1,2,3]
#     func(t,v)
#     print(t,v[0])
#-----------------------------------------------------
#5
# arr=[[1,2,3,4],[4,5,6,7],
#      [8,9,10,11],[12,13,14,15]]
# for i in range(0,4): #i=0,i=1,i=2 likewise
#     print(arr[i].pop())
    #pop in stack remove the last element 
    #value of row and column i start from 0
#-------------------------------------------------------
#6
# def f(i,values =[]):
#     values.append(i) #[1][1,2][1,2,3]
#     print(values)

#     f(1)#calling func
#     f(2)
#     f(3)
#------------------------------------------------------
#7
# arr =[1,2,3,4,5,6]
# for i in range(1,6):#i=1
#     arr[i-1]=arr[i]#[2,3,4,5,6]
# for i in range(0,6):#index starting from 0 
#   print(arr[i],end=" ")    
#---------------------------------------------------
#8
# fruit_list1 = ['Apple','Berry','cherry','Papaya']
# fruit_list2 = fruit_list1
# fruit_list3= fruit_list1[:]#:means all element from starting
# fruit_list2[0]='Guava'
# fruit_list3[1]='Kiwi'

#------------------------------------------------------------------------------------------------------
#9
#math=50  #find address
#chem=50
#print(id(math))
#print(id(chem))
#--------------------------------------------------------------------------------------------------------------
#10

#rec ={"Name":"Python","Age":"20"}
#r =rec.copy()
#print(id(r) == id(rec))


# rec ={"Name":"Python","Age":"20","Addr":"NJ","Country":"USA"}
# id1 = id(rec)
# del rec
# rec ={"Name":"Python","Age":"20","Addr":"NJ","Country":"USA"}
# id2 = id(rec)
# print(id1==id2)



# print(int(3.14))#execute
# print(int(True))
# print(int(False))
# print(int("4"))

#print(int(10+5j)) #not execute
#print(int("4.22"))#not both at same time



# print(float(3)) execute
# print(float(True))
# print(float(4.22))
# print(float("4")


# print(bool(0)) #false
# print(bool(False)) #false
# print(bool())
#for other booolean is true

#-----------------------------------------------------------------------------------                                                                                                                                                                                                    

