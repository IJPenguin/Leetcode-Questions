# hand = [1,2,3,6,2,3,4,7,8]
# groupSize = 3
# hand = [1,2,3,4,5]
# groupSize = 4
hand = [1]
groupSize = 1
hand.sort()
while hand:
    c = 0
    el = hand[0]
    t = hand
    while c < groupSize:
        if el in t:
            t.remove(el)
            el += 1
            c += 1
        else:
            print(False)
            exit()
    hand = t
print(True)


# if len(hand) % groupSize != 0:
#             return False

#         count = Counter(hand)
#         for num in sorted(count):
#             if count[num] > 0:
#                 start = count[num]
#                 for i in range(groupSize):
#                     if count[num + i] < start:
#                         return False
#                     count[num + i] -= start
#         return True