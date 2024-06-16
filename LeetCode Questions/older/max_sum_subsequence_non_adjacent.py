def sum_subseq(arr):
    max_so_far = float('-inf')
    max_ending_here = 0
    prev = True

    for num in arr:
        if prev:
            prev = False
            