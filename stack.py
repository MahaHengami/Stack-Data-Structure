class Stack:
    def __init__(self,s=None,top=None,x=None):
        if s==None:
            s=[]
        self.x=x
        self.s= s
        self.top= len(s)

    def Stack_Empty(self):
        if self.top==0:
            return True
        else:
            return False
        
    def Push(self,x):
        self.top+=1
        self.s.append(x)
        return(self.s,self.top)

    def Pop(self):
        if self.Stack_Empty():
            print("Stack underflow: Can't pop from an empty stack")
        else:
            self.s.pop()
            self.top-=1
            return(self.s)
        
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)


    




            



        
    
    





    




            



        
    
    


