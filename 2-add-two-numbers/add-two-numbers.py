# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Dummy node to simplify code
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Traverse both lists
        while l1 or l2 or carry:
            # Calculate the sum of digits and carry
            sum_val = carry
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            
            # Update carry and create a new node for the result
            carry = sum_val // 10
            current.next = ListNode(sum_val % 10)
            current = current.next
        
        # Return the next node of the dummy node (the actual result)
        return dummy.next
