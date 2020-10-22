class MinHeap:
    def __init__(self):
        self.heapArray = []
        self.heapLength = 0

    def insert(self,val):
        self.heapArray.append(val)
        self.heapifyup(self.getLen()-1)
        self.setLen()

    def remove(self):
        val = self.heapArray[0]
        self.heapArray[0] = self.heapArray[-1]
        self.heapArray.pop()
        self.setLen()
        self.heapifyDown(0)
        return val

    def setLen(self):
        self.heapLength = len(self.heapArray)

    def getLen(self):
        return self.heapLength

    def parent(self,idx):
        return (idx-1)//2

    def leftChild(self,idx):
        return 2*idx+1

    def rightChild(self,idx):
        return 2*idx+2

    def heapifyup(self,lastIndex):
        parentIdx = self.parent(lastIndex)
        if(lastIndex>0 and self.heapArray[lastIndex] < self.heapArray[parentIdx]):
            # print(lastIndex,parentIdx,self.heapArray[lastIndex],self.heapArray[parentIdx])
            self.heapArray[lastIndex],self.heapArray[parentIdx] = self.heapArray[parentIdx],self.heapArray[lastIndex]
            self.heapifyup(parentIdx)

    def heapifyDown(self,currIdx):
        leftidx = self.leftChild(currIdx)
        rightidx = self.rightChild(currIdx)
        smallest = currIdx
        if leftidx < self.getLen() and self.heapArray[smallest] > self.heapArray[leftidx]:
            smallest = leftidx
        if rightidx < self.getLen() and self.heapArray[smallest] > self.heapArray[rightidx]:
            smallest = rightidx
        # print(leftidx,rightidx,smallest,self.heapArray[smallest])
        if smallest != currIdx:
            self.heapArray[smallest],self.heapArray[currIdx] = self.heapArray[currIdx],self.heapArray[smallest]
            print(self.heapArray)
            self.heapifyDown(smallest)
        
    def printHeap(self):
        print(self.heapArray)


minheap = MinHeap()
minheap.insert(3)
minheap.insert(18)
minheap.insert(5)
minheap.insert(24)
minheap.insert(19)
minheap.insert(14)
minheap.insert(15)
minheap.insert(25)
minheap.insert(22)
minheap.insert(32)
minheap.insert(20)
print(minheap.remove())
minheap.printHeap()
