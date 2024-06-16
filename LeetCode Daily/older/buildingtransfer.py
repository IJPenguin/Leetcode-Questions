from collections import defaultdict

n = 5
requests = [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]
    

def update_requests(n, requests):
    left = defaultdict(int)
    right = defaultdict(int)
    count = 0

    for request in requests:
        left[request[0]] -= 1
        right[request[1]] += 1

    pass

