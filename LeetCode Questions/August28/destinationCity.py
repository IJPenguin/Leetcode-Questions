from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dest = []
        d = {}

        for path in paths:
            if path[0] in d.keys():
                d[path[0]].append(path[1])
            else:
                d[path[0]] = [path[1]]
            dest.append(path[1])

        for des in dest:
            for out in d.keys():
                if des in out:
                    break
            else:
                return des
            
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        in_city, out_city = set(), set()

        for path in paths:
            in_city.add(path[0])
            out_city.add(path[1])

        return (out_city - in_city).pop()        

paths1 = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
paths2 = [["B", "C"], ["D", "B"], ["C", "A"]]
paths3 = [["A", "Z"]]
s = Solution()
print(s.destCity(paths1))
print(s.destCity(paths2))
print(s.destCity(paths3))
