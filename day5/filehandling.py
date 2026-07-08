# #whenever we wnat to store the data for future purpose so we used the file handling concepts

# f=open("myfile.txt","w")
# print("name of file:",f.name)
# print("file mode: ",f.mode)
# print("readable",f.readable())
# print("writable",f.writable())
# print("file closed:",f.closed)
# f.close()
# print("file closed:",f.closed)


##performing write operation
# f=open("myfile.txt","w")
# f.write("\n Pune is a smart city")
# f.write("\n Nashik is a smart city")
# f.write("\n Nagpur is a smart city")
# f.write("\n Banglore is a smart city")
# f.write("\n Indore is a smart city")
# f.close()
# print("file operation is done")


## inserting list 
# f=open("newfile.txt","w")
# mylist=["prashant","mahesh","suresh"]
# f.writelines(mylist)
# f.close()
# print("writen work has done successfully")


##reading data from a file
# f=open("myfile.txt","r")
# print(f.read())
# f.close()


##using with block

# with open("myfile.txt","w") as f:
#     f.write("amit\n")
#     f.write("prashant\n")
#     f.write("ashish\n")
#     print("file closed:",f.closed)
# print("file closed :",f.closed)    


#reading and writh
# f1=open("screen.jpg","rb")
# f2=open("Rossam.jpg","wb")
# data=f1.read()
# f2.write(data)


##operration with CSV file
# import csv
# f=open("student.csv","a",newline="")
# a=csv.writer(f)#here it will return csvwriter object
# #a.writerow(["studentId","rollno","name","mobileno"])#if they ask to store in col then it store in string

# studentid=int(input("enter student id:"))
# rollno =int(input("enter your roll no"))
# name=(input("enter your name"))
# mobileno=int(input("enter your mobile no"))
# a.writerow([studentid,rollno,name,mobileno])
# print("student record has save")


# task 
# import csv
# f=open("stud.csv","a",newline="")
# a=csv.writer(f)#here it will return csvwriter object
# #a.writerow(["rollno","name","mobileno","p1","p2","p3","total","persentage","email","result"])#if they ask to store in col then it store in string

# rollno =int(input("enter your roll no"))
# name=(input("enter your name"))
# mobileno=int(input("enter your mobile no"))
# p1=int(input("enter your marks of p1"))
# p2=int(input("enter your marks of p2"))
# p3=int(input("enter your marks of p3"))
# email=input("enter your email")

# if p1>=40 and p2>=40 and p3>=40:
#     result="pass"
# else:
#     result="fail"

# total=p1+p2+p3
# percentage=total/3.0    

# a.writerow(["rollno","name","mobileno","p1","p2","p3","total","persentage","email","result"])
# print("student recored is save")



#-----------------------------------------------------------------------------
