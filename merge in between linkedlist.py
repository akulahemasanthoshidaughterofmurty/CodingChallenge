# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        l1ptr, l2ptr, i = list1, list2, 0
        while True:
            if i == a - 1:
                athptr = l1ptr
            if i == b + 1:
                bthptr = l1ptr
                break
            i += 1
            l1ptr = l1ptr.next
        while True:
            if l2ptr.next == None:
                break
            else:
                l2ptr = l2ptr.next
        athptr.next = list2
        l2ptr.next = bthptr
        return list1

1.so we need to rremove elements from a to b so that we are storing the connections as athptr and bthptr and as we need to connect bthptr to the end of list2 .
2.we need end point of list2 so, this second while will find us that last end and will help us to connect
