class Solution:
    def __init__(self) -> None:
        self.ans = 0
    
    def minimum_fuel_cost(self, roads, seats):
        adj = [[] for _ in range(len(roads) + 1)]
        self.ans = 0
        for a in roads:
            adj[a[0]].append(a[1])
            adj[a[1]].append(a[0])
        self.solve(adj,seats,0, -1)
        return self.ans
    
    def solve(self, adj, seats, src, parent):
        people = 1
        for i in adj[src]:
            if i != parent:
                people += self.solve(adj, seats, i, src)
                if src!= 0:
                    self.ans += (people + seats - 1) // seats
        return people

if __name__ == "__main__":
    solution = Solution()
    roads = [[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]]
    seats = 2
    result = solution.minimum_fuel_cost(roads, seats)
    print(result)
