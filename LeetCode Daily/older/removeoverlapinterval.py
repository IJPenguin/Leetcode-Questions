intervals = [[1,2],[2,3],[3,4],[1,3]]

def removeoverlapinterval(intervals):
    intervals.sort(key=lambda x: x[1])
    print(intervals)
    count = 0
    end = float('-inf')
    for i in intervals:
        if i[0] >= end:
            end = i[1]
        else:
            count += 1
    return count

print(removeoverlapinterval(intervals))