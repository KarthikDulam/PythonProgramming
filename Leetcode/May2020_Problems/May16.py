""" Odd Even Linked List """
from typing import List

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
            if head == None:
                return None    
    
            odd_list = []
            even_list = []

            pos = 1

            while(head != None):
                if pos % 2 != 0:
                    odd_list.append(head)
                else:
                    even_list.append(head)        
                pos += 1
                head = head.next

            final_list = odd_list + even_list

            head = final_list[0]
            final = head

            for i in final_list[1:len(final_list)]:
                i.next = None
                head.next = i
                head = head.next

            return final