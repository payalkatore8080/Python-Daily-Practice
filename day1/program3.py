# init_tuple_a='a','b'
# init_tuple_b=('a','b')
# print(init_tuple_a == init_tuple_b)#true

# #-------------------------------------------------------

# l=[1,2,3]
# init_tuple =('Python',)*(l.__len__()-l[::-1][0])
# print(init_tuple)

# #------------------------------------------------------------


# my_dict ={}
# my_dict[(1,2,4)]=8
# my_dict[(4,2,1)]=10
# my_dict[(1,2)]=12
# sum=0
# for k in my_dict:  #(1,2,4)
#     sum+=my_dict[k]
# print(sum)
# print(my_dict)    
#--------------------------------------------------------------------
#a={(1,2):1,(2,3):2,(4,5):3}
#print(a[4,5])


#a={'a':1,'b':2,'c':3}
#print(a['a','b'])#two keys not assign at a time




# fruit={}
# def addone(index):
#    if index in fruit:#this condition to stsisfied because key is not present
#       fruit[index] +=1
#    else:
#      fruit[index] =1  #{'Apple':1,'Banana':1,'apple':1}case sensetive that why apple is different 
# addone('Apple')
# addone('Banana')
# addone('apple')
# print(len(fruit))


#------------------------------------------------------------------------------------------
# arr={}#dictionary  default access  key{1:2,'1':2}
# arr[1]=1
# arr['1']=2
# arr[1]+=1
# sum =0 #2
# for k in arr: #1 
#      sum +=arr[k]
#      print(sum)    

#----------------------------------------------------------------------------------------------------


# my_dict ={}  #yaha per key value update hogi 1 se 4{1:4,'1':2}

# my_dict[1]=1
# my_dict['1']=2
# my_dict[1.0]=4
# print(my_dict)
# sum=0
# for k in my_dict:
#     sum +=my_dict[k]
# print(sum)    