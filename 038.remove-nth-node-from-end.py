class Lnode:
    def __init__(self,val):
        self.val = val
        self.next = None

llist = Lnode(0)
llist.next = Lnode(1)
llist.next.next = Lnode(2)
llist.next.next.next = Lnode(3)
llist.next.next.next.next = Lnode(4)
llist.next.next.next.next.next = Lnode(5)
llist.next.next.next.next.next.next = Lnode(6)
llist.next.next.next.next.next.next.next = Lnode(7)
llist.next.next.next.next.next.next.next.next = Lnode(8)
llist.next.next.next.next.next.next.next.next.next = Lnode(9)

def removeNthFromEnd(head, n):
    fast = slow = head
    while(n+1):
        if not fast:
            return head.next
        fast = fast.next
        n-=1
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head

def printList(head):
    temp = head
    while temp.next:
        print(temp.val,end="->")
        temp = temp.next
    print(temp.val)

printList(llist)
llist = removeNthFromEnd(llist,1)
printList(llist)