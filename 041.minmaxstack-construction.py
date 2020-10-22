class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.minmaxstack = []

    def push(self,val):
        self.stack.append(val)
        if not self.minmaxstack:
            self.minmaxstack.append((val,val))
        else:
            x = self.minmaxstack[-1]
            self.minmaxstack.append((min(val,x[0]),max(val,x[1])))
    
    def pop(self):
        if not self.stack:
            raise Exception('Unable to pop from empty stack')
        self.minmaxstack.pop()
        value = self.stack[-1]
        self.stack.pop()
        return value

    def getMin(self):
        if not self.minmaxstack:
            raise Exception('Unable to get Min from empty stack')
        else:
            return self.minmaxstack[-1][0]

    def getMax(self):
        if not self.minmaxstack:
            raise Exception('Unable to get Max from empty stack')
        else:
            return self.minmaxstack[-1][1]

    def peek(self):
        if not self.stack:
            raise Exception('Unable to peek from empty stack')
        else:
            return self.stack[-1]


stack = MinMaxStack()
stack.push(10)
stack.push(-1)
stack.push(10)
print(stack.getMin())
stack.pop()
stack.pop()
print(stack.getMax())
print(stack.getMin())