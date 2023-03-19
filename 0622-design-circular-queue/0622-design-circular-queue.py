class MyCircularQueue:

    def __init__(self, k: int):
        self.max_size=k
        self.size=0
        self.q=[-1]*k
        self.front=-1
        self.rear=-1
        

    def enQueue(self, value: int) -> bool:
        if self.front==-1:
            self.front=0
        if self.size<self.max_size:
            self.rear=(self.rear+1)%self.max_size
            self.q[self.rear]=value
            self.size+=1
            return True
            
        else:
            return False
            

    def deQueue(self) -> bool:
        if self.size>0:
            self.front=(self.front+1)%self.max_size
            self.size-=1
            return True
        else:
            return False
        

    def Front(self) -> int:
        if self.size>0:
            return self.q[self.front]
        else:
            return -1
        

    def Rear(self) -> int:
        if self.size>0:
            return self.q[self.rear]
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.size==0:
            return True
        return False

    def isFull(self) -> bool:
        if self.size==self.max_size:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()