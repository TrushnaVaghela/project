import sys

class QueueDemo:

    top = 0
    
    queueData = []

    size = 0



    def __init__(self,size):

        self.size = size

    def isFull(self):

        if(self.top==self.size):

            return 0

        else:

            return 1

    def isEmpty(self):

        if(self.top==0):

            return 0

        else:

            return 1

    def enqueue(self,x):

        t = self.isFull()

        

        if(t==0):

            print("queue is Overflow")

        else:

            self.queueData.append(x)

            self.top = self.top + 1

            print("One Element is enqueued")

            print(self.top)

    def dequeue(self):

        t = self.isEmpty()

        

        if(t==0):

            print("queue is Underflow")

        else:

            self.top = self.queueData.pop(0)

            print("One Element is dequeued")

            print(self.top)

    def display(self):

        if(self.top == 0):

            print("queue is Underflow")

        else:

            for n in range(len(self.queueData)):

                print("Element -> ",self.queueData[n]) 

            

queue1 = QueueDemo(5)

choice = 0

print("Welcome to the NUV\n")

print("1: enqueue \n2: dequeue  \n4: Display \n5: Exit")

while(5==5):

    choice = int(input("Enter Your Choice : "))

    if(choice==1):

        t = input("Enter Value : ")

        queue1.enqueue(t)

    elif(choice==2):

        queue1.dequeue()

    elif(choice==4):

        queue1.display()

    elif(choice==5):

        sys.exit() 

    else:

        print("Invalid Data")



                               
                                