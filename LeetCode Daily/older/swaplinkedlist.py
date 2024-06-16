#APPROACH 1

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def swap(arr, k , n):
#     first = k-1
#     second = n-k
#     temp = arr[first]
#     arr[first] = arr[second]
#     arr[second] = temp

# def createList(head, data):
#     new_node = ListNode(data)
#     current = head
#     while current.next is not None:
#         current = current.next
#     current.next = new_node
#     return

# class Solution:
#     def swapNodes(self, head, k: int):
#         current = head
#         arr = []
#         n = 0
#         while current is not None:
#             arr.append(current.val)
#             current = current.next
#             n += 1
        
#         swap(arr, k , n)
#         for i , data in enumerate(arr):
#             if i == 0:
#                 head1 = ListNode(data)
#             else:
#                 createList(head1, data)
#         return head1
    
# APPROACH 2

class Solution:
    def swapNodes(self, head, k: int):
        n , counter, val1, val2 = 0
        current = head

        while current:
            n += 1
            current = current.next

        current = head

        if n==2:
            temp = current.val
            current.val = current.next.val
            current.next.val = temp
            return head
        
        while current:
            counter += 1
            if k > n/2+1:
                if counter == n-k+1:
                    val1 = current.val
                if counter == k:
                    val2 = current.val
                    current.val = val1
            else:
                if counter == k:
                    val1 = current.val
                if counter == n-k+1:
                    val2 = current.val
                    current.val = val1
                    break
            current = current.next

        counter = 0
        current = head
        while current:
            counter += 1
            if k > n/2+1:
                if counter == n - k + 1:
                    current.val = val2
                    break
            else:
                if counter == k:
                    current.val = val2
                    break
            current = current.next
        
        return head