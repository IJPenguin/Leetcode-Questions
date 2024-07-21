strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

def groupAnagrams(strs):
    dic = {}
    for string in strs:
        arr = [0] * 26
        for char in string:
            arr[ord(char)-97] += 1
        arr = tuple(arr)
        if dic.get(arr, False):
            dic[arr].append(string)
        else:
            dic[arr] = [string]

    return list(dic.values())

print(groupAnagrams(strs))

