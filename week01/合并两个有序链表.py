# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        mn = ListNode(0)
        m = mn
        while (list1 != None and list2 != None ):
            if list1.val <= list2.val:
                m.next = list1
                list1 = list1.next
            else:
                m.next = list2
                list2 = list2.next
            m = m.next
            # print(m)
        if list1 == None:
            m.next = list2
        if list2 == None:
            m.next = list1
        return mn.next