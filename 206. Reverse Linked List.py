# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        result = None
        if not head or head == None:
            return result
        pre = head
        while pre:
            tmp = pre.next
            pre.next = result
            result = pre
            pre = tmp
        return result

#递归
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def rever(p):
            if p == None or p.next == None :
                return p
            newP = rever(p.next)
            p.next.next = p
            p.next = None
            return newP
        return rever(head)