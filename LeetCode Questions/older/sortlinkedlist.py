if not list1:
    return list2

if not list2:
    return list1

curr = list1 
temp = list2
    
while list1 and list2:
    if curr.val <= temp.val:
        curr.next = list1
        list1 = list1.next  
    else:
        curr.next = list2
        list2 = list2.next
    curr = curr.next

curr = list1 or list2
