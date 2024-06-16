def rev(x):
    x = [*str(x)]
    x.reverse()
    return int("".join(x))


def nicePairs(nums):
    dict = {}
    count = 0
    for i, num in enumerate(nums):
        val = num - rev(num)
        if val not in dict.keys():
            dict[val] = 1
        else:
            count += dict[val]
            dict[val] += 1
        print(dict)
    return count


modulo = 10**9 + 7
nums = [42,11,1,97]
print(nicePairs(nums))