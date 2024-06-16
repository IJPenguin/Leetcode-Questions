questions = [[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]]


def iter(q, index):
    pts = 0
    if index >= len(q):
        return pts
    pts += q[index][0]
    index += q[index][1] + 1
    return pts + iter(q, index)

def solve_it(q, index):
    arr = []
    idx = q[index][1] + 1 + index
    if(idx < len(q)):
        for i in range(idx, len(q)):
            pts = q[index][0]
            pts += iter(q, i)
            arr.append(pts)
    else:
        pts = 0
        pts += iter(q, index)
        arr.append(pts)
    return arr

arr_main = []        
max_digit = 0


for i in range(0, len(questions)):
    arr_i = []
    arr_i = solve_it(questions, i)
    arr_main.append(arr_i)

for row in arr_main:
    for digit in row:
        if digit > max_digit:
            max_digit = digit

print(arr_main)
print(max_digit)


questions = [[21,2],[1,2],[12,5],[7,2],[35,3],[32,2],[80,2],[91,5],[92,3],[27,3],[19,1],[37,3],[85,2],[33,4],[25,1],[91,4],[44,3],[93,3],[65,4],[82,3],[85,5],[81,3],[29,2],[25,1],[74,2],[58,1],[85,1],[84,2],[27,2],[47,5],[48,4],[3,2],[44,3],[60,5],[19,2],[9,4],[29,5],[15,3],[1,3],[60,2],[63,3],[79,3],[19,1],[7,1],[35,1],[55,4],[1,4],[41,1],[58,5]]