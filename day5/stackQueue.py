import sys 
class Queue:
    def __init__(self,queueSize):#parameter constructor
        self.queueSize = queueSize
        self.myQueue=[] #empty lis
    
    def isFull(self):
        if len(self.myQueue)==self.queueSize:
            return True
        else:
            return False

    def  isEmpty(self):
        if self.myQueue==[]:
           return True
        else:
            return False
        
    def enQueue(self,value):
        if self.isFull():
            print("queue is Full")
        else:
            self.myQueue.append(value)

    def display(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(self.myQueue)  
    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(self.myQueue.pop(0))   
    def frontPeek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(self.myQueue[0])      
    
    def deleteQueue(self):
        self.myQueue =None



size=int(input("Enter the size of Queue:"))
queObj = Queue(size)
while True:
    print("1.enQueue")
    print("2.display")
    print("3.deQueue")
    print("4.frontPeek")
    print("5.Delete Queue")
    print("6.Exit")
    choice=int(input("Enter your choice:"))
    if choice == 1:
        value=int(input("enter a value to enter a queue"))
        queObj.enQueue(value)
    elif choice == 2:
        queObj.display()    
    elif choice ==3:
         queObj.deQueue()  
    elif choice==4:
          queObj.frontPeek()
    elif choice==5:
        queObj.myQueue
    elif choice==6:
        queObj.exit()               