class DLLNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class DLL:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertAtHead(self,val):
        if not self.head:
            self.head = DLLNode(val)
            self.tail = self.head
        else:
            temp = DLLNode(val)
            temp.next = self.head
            self.head.prev = temp
            self.head = temp

    def insertAtTail(self,val):
        if not self.tail:
            self.tail = DLLNode(val)
            self.head = self.tail
        else:
            temp = DLLNode(val)
            temp.prev = self.tail
            self.tail.next = temp
            self.tail = temp

    def insertBefore(self,nodeVal,val):
        curr = self.head
        found = False
        while curr:
            if curr.val == nodeVal:
                found = True
                temp = DLLNode(val) 
                temp.prev = curr.prev
                curr.prev.next = temp
                temp.next = curr
                curr.prev = temp
            curr = curr.next
        return found



    def insertAfter(self,nodeVal,val):
        curr = self.head
        found = False
        while curr:
            if curr.val == nodeVal:
                found = True
                temp = DLLNode(val)
                temp.next = curr.next
                curr.next.prev = temp
                temp.prev = curr
                curr.next = temp
                curr = temp
            curr = curr.next
        return found

    def deleteAll(self,nodeVal):
        temp = self.head
        while temp:
            if temp.val == nodeVal:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
            temp = temp.next
            


    def printList(self):
        ans = []
        temp = self.head
        while temp:
            ans.append(temp.val)
            temp = temp.next
        print(*ans)

ll = DLL()

ll.insertAtHead(10)
ll.insertAtHead(20)
ll.insertAtHead(30)
ll.insertAtHead(40)
ll.insertAtHead(50)
ll.insertAtTail(60)
ll.deleteAll(20)
ll.insertBefore(30,20)
ll.insertAfter(20,70)

ll.printList()