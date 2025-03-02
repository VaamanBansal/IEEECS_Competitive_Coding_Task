class Stack:
    def __init__(self):
        self.stack=[]
        self.stackmin=[]
        self.stackmax=[]
    def push(self,n):
        self.stack.append(n)
        if not self.stackmin or n<=self.stackmin[-1]:
            self.stackmin.append(n)
        else:
            self.stackmin.append(self.stackmin[-1])
        if not self.stackmax or n>=self.stackmax[-1]:
            self.stackmax.append(n)
        else:
            self.stackmax.append(self.stackmax[-1])
        
    def pop(self):
        if self.stack:
            self.stack.pop()
            self.stackmin.pop()
            self.stackmax.pop()
            print("Operation Executed")
        else:
            print("Stack is Empty")
    def top(self):
        if self.stack:
            t=self.stack[-1]
            print("The Top Element is:",t)
        else:
            print("Stack is empty")
    def getMin(self):
        if self.stack:
            print("The Smallest element is:",self.stackmin[-1])
        else:
            print("Stack is empty")
    def getMax(self):
        if self.stack:
            print("The Largest element is:",self.stackmax[-1])
        else:
            print("Stack is empty")
    def getStack(self): #Extra feature to check if it the logic works as intended
        print(self.stack)
def add(s1):
    t=int(input("Enter number of elements:"))
    for i in range (t):
        o=int(input("Enter term:"))
        s1.push(o)
s1=Stack()
add(s1)
s1.getStack()
s1.top()
s1.pop()
s1.getStack()
s1.top()
s1.getMax()
s1.getMin()