class MinStack:

    def __init__(self):
        #initiate a list 
        self.s = []
        #indicates the minimum value found
        self.minval = None

    def push(self, val: int) -> None:
        if not self.s: 
            #if list doesnt have any element
            self.minval = val
            self.s.append(val)
            #append value in the list

        #else if the minimum vale is higher than the value
        elif self.minval > val:
            #append val times 2 - minimum value
            self.s.append(val* 2 - self.minval)
            #sets minimum value to value since its higher
            self.minval = val
            print(self.minval)
        else:
            #else, just append value
            self.s.append(val)
        

    def pop(self) -> None:
        if self.s:
            if self.s[-1] < self.minval:
                #FORMULA THAT GETS THE MINOR VALUE AFTER POPPING THE VALUE THAT WAS THE MINOR
                self.minval = self.minval * 2 - self.s[-1]
            self.s.pop()

    def top(self) -> int:
        if self.s:
            if self.s[-1] < self.minval:
                return self.minval
            return self.s[-1]

    def getMin(self) -> int:
        return self.minval
 



# Your MinStack object will be instantiated and called as such:
obj = MinStack()

# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()
minStack.pop()
minStack.top()   
minStack.getMin() 