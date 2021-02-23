# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dict1 = {}
        res = False
        begin = head
        while head:
            if head in dict1:
                res = True
                p = head
                break
            dict1[head] = head.val
            head = head.next
        return res
                
#FFFFFFFFFFFFFAST
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p = head
        q = head
        res = False
        while p and q:
            if p!=None and p.next != None and q.next!= None and q.next.next!=None:
                p = p.next
                q = q.next.next
                if p == q:
                    res = True
                    break
            else:
                break
        return res
                
