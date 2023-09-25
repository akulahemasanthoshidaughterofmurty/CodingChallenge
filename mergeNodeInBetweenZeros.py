# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=ListNode()
        cur=head
        temp=head.next
        lastcheck=None
        
        while cur.next:
            sum=0
            while temp.val!=0:
                sum+=temp.val
                temp=temp.next
            cur.val=sum
            cur.next=temp
            lastcheck=cur
            cur=cur.next
            temp=cur.next
        lastcheck.next=None
        return head

      1.we are not creating any other linked list
2.curreventvalue will be at first zero and the temp variable moves foraward and values untill itfounds another zero.
3.once it founds another zero ----->it updates cur.val to sum and cur.next to temp to escape inbetween nodes and to for example if it is 0->3->1->0->4->5->0 now curr.val=4 ,curr.next=0
4.then now curr=curr.next which is zero
and temp=curr.next which is 4
        
            
