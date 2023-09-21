# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        c=0
        res=0
        temp=head
        while head:
                c=c+1
                head=head.next
        c=c-1
        while temp:
            if temp.val==1:
                res=res+2**c
                c=c-1
                temp=temp.next

            else:
                c=c-1
                temp=temp.next
        return res

#another way of doing
ans=0
        while head:
            ans=ans*2+head.val
            head=head.next
        return ans
101
ans=0
0*2
0+1  --->1st

1*2
2+0 ---->2ndpos

2*2
4+1 ----->3rdpos

5
