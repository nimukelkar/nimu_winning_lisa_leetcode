class MyQueue:

    def __init__(self):
        self.stk1=[]
        self.stk2=[]

    def push(self, x: int) -> None:
        self.stk1.append(x)
        

    def pop(self) -> int:
        #print("self.stk2=",self.stk2)
        if self.stk2:
            idx=self.stk2[-1]
            self.stk2.remove(idx)
            return idx
        else:
            self.stk2=self.stk1[::-1]
            self.stk1=[]
            idx=self.stk2[-1]
            #print("Top of stack=",idx)
            self.stk2.remove(idx)
            return idx
            
    def peek(self) -> int:
        if self.stk2:
            return self.stk2[-1]
        return self.stk1[0]
        

    def empty(self) -> bool:
        if not self.stk1 and not self.stk2:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()