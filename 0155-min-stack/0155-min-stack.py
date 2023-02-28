class MinStack:

    def __init__(self):
        self.stk=[]
        self.mini=float("inf")
        

    def push(self, val: int) -> None:
        if self.stk:
            self.mini=min(val,self.stk[-1][1])
            self.stk.append((val,self.mini))
        else:
            self.stk.append((val,val))
        
        

    def pop(self) -> None:
        if self.stk:
            del self.stk[-1]
        

    def top(self) -> int:
        if self.stk:
            return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()