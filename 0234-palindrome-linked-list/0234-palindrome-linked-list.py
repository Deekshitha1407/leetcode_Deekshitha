# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.first=head
        def palindrome(head):
            if not head:
                return True 
            res=palindrome(head.next) and head.val==self.first.val
            self.first=self.first.next
            return res
        return palindrome(head)