matrix = [[1],[3]]
target = 1

r1 = 0
r2 = len(matrix)-1
rmid = 0

while r1 <= r2:
    rmid = (r1+r2)//2
    if target >= matrix[rmid][0]:
        r1 = rmid + 1        
    elif target <= matrix[rmid][0]:
        r2 = rmid - 1

c1 = 0
c2 = len(matrix[rmid]) - 1 
cmid = 0
found = False
while not found and c1 <= c2:
    cmid = (c1 + c2)// 2
    if target == matrix[rmid][cmid]:
        found = True
        print("penguin")
        break
    elif target > matrix[rmid][cmid]:
        c1 = cmid + 1
    elif target < matrix[rmid][cmid]:
        c2 = cmid - 1

if not found:
    print(False)


