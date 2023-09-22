class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool: #123321
        slow=fast=head
        while fast and fast.next:    #this while allow us to find the middle node in which slow move one node ahead and  fast move two nodes ahead
            slow=slow.next
            fast=fast.next.next      #now here the slow will be 3
        temp1=self.reverseList(slow) #once the fast node reaches to end then it is known as slow is at the middle node
                                      #then we calling the reverse function to reverse the linked list from the middle  # it will reverse 321 as 123 ,,, temp1 we have reversedlist and temp2 we have original list
        temp2=head

        while temp1 and temp2:
            if temp1.val!=temp2.val:
                return False
            temp1=temp1.next
            temp2=temp2.next
        return True

    def reverseList(Self,head:Optional[ListNode])->Optional[ListNode]:
        previous=None
        while head:
                next_node=head.next
                head.next=previous
                previous=head
                head=next_node
        return previous
