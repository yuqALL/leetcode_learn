from typing import List


class UnionFindWithRank:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.ranks = [1 for _ in range(size)]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if self.ranks[node1] <= self.ranks[node2]:
            self.parents[root1] = root2
        else:
            self.parents[root2] = root1
        if self.ranks[node1] == self.ranks[node2]:
            self.ranks[root2] += 1

    def find(self, node):
        if node == self.parents[node]:
            return node
        else:
            self.parents[node] = self.find(self.parents[node])
            return self.parents[node]

    def isConnected(self, node1, node2):
        return self.find(node1) == self.find(node2)


class UnionFind:
    def __init__(self, size):
        self.parents = [i for i in range(size)]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if self.parents[node1] != self.parents[node2]:
            self.parents[root1] = root2
            # print(node1,node2,root1,root2,self.parents)

    def find(self, node):
        if node == self.parents[node]:
            return node
        else:
            self.parents[node] = self.find(self.parents[node])
            return self.parents[node]

    def isConnected(self, node1, node2):
        return self.find(node1) == self.find(node2)
