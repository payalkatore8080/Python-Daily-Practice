# import sys

# def add():
#     a=int(input("Enter value of A:"))
#     b=int(input("Enter value of B:"))
#     print(a+b)

# def sub():
#     a=int(input("Enter value of A:"))
#     b=int(input("Enter value of B:"))
#     print(a-b)

# def div():
#     a=int(input("Enter value of A:"))
#     b=int(input("Enter value of B:"))
#     print(a/b)

# def mul():
#     a=int(input("Enter value of A:"))
#     b=int(input("Enter value of B:"))
#     print(a*b)

# while True:
#     print("1.Addition")
#     print("2.subtraction")
#     print("3.Division")
#     print("4.Multiplication")
#     print("5.Exit")
#     choice=int(input("Enter your choice:"))
#     if choice==1:
#         add()#calling fuc
#     elif choice ==2:
#         sub()#calling func    
#     elif choice ==3:
#         div()#calling func
#     elif choice ==4:
#         mul()            
#     elif choice==5:
#         sys.exit()    

#==============================================================================
#code Product of Array Except self 
#stack implementation with size limit
# import sys
# class Stack:
#     def __init__(self,stackSize):
#         self.stackSize=stackSize #stack size define
#         self.myStack=[] #list rep stack

#     def isFull(self):
#         if len(self.myStack)==self.stackSize:
#             return True
#         else:
#             return False

#     def isEmpty(self):
#         if self.myStack==[]:
#             return True
#         else:
#             return False
         

#     def push(self,value):
#         if self.isFull():
#             print("Stack is full")
#         else:
#             self.myStack.append(value)

#     def display(self):
#         if self.isEmpty():
#             print("stack is empty")
#         else:
#             print("stack=",self.myStack)          

#     def pop(self):
#         if self.isEmpty():
#             print("stack is empty") 
#         else:
#             print(self.myStack[-1])
    
#     def peek(self):
#         if self.isEmpty():
#             print("stack is empty")
#         else:
#             print(self.myStack[-1])
#     def delete(self):
#         self.myStack=None            

# size=int(input("Enter the size of stack"))
# obj=Stack(size)
# while True:
#     print("1.Push")
#     print("2.display")
#     print("3.Pop")
#     print("4.peek")
#     print("5.delete")
#     print("6.Exit")
#     choice=int(input("Enter your choice"))
#     if choice == 1:
#         value=int(input("enter the value to push in stack"))
#         obj.push(value)
#     elif choice ==2:
#         obj.display()    
#     elif choice ==3:
#         obj.pop()    
#     elif choice ==4:
#         obj.peek() 
#     elif choice ==5:
#         obj.delete()        
#     elif choice ==6:
#         sys.exit()        

#=======================================================================================

# print('payalkatore7777'.isalnum())#true
# print('payalkatore'.isalpha())#true
# print('777f'.isdigit())
# print('sdsdsdsd'.islower())
# print(''.islower())
# print('PRASHANtj'.isupper())
# print('My Name Is Prashant') \
