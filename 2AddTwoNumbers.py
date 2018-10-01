# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = l3 = ListNode(0)
        
        
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            
            l3.next = ListNode(carry % 10)
            l3 = l3.next
            carry //= 10
        
        return head.next

def compareLinkedList(l1, l2):
    while l1 or l2:
        if not (l1 and l2) or l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    return True


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    lsum = ListNode(7)
    lsum.next = ListNode(0)
    lsum.next.next = ListNode(8)
    print(compareLinkedList(Solution().addTwoNumbers(l1, l2), lsum))
