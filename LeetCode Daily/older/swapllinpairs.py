# class Solution:
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next: 
#             return head
#         new_head = ListNode(-1)
#         new_head.next = head
#         prev = new_head
#         while prev.next and prev.next.next:
#             first = prev.next
#             second = prev.next.next
#             first.next = second.next
#             second.next = first
#             prev.next = second
#             prev = first

#         head = new_head.next
#         return head
        