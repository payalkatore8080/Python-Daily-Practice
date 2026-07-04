init_tuple =()
print(init_tuple.__len__())

#----------------------------------------------

box={}
jars ={}
create ={}
box['biscuit']=1
box['cake']=3
jars['jam']=4
create['box']=box
create['jars']=jars
print(len(create[box]))