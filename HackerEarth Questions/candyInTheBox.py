def find_box_for_kth_candy(N, K):
    cur = 1
    candy = 1
    val = 1
    while candy < K:
        cur += val
        if cur == N:
            val = -1
        if cur == 1:
            val = 1
        candy += 1
    return cur

n = 5
k = 2
print(find_box_for_kth_candy(n, k))