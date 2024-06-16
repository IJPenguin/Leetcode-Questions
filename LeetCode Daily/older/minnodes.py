class Solution:
    def findSmallestSetOfVertices(self, n: int, edges):
        result = []
        # number = [_ for _ in range(n)]
        indegree = [0 for _ in range(n)]
        for i in edges:
            indegree[i[1]] += 1

        for i in range(n):
            if indegree[i] == 0:
                result.append(i)
        return result