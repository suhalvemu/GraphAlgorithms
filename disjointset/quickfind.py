# quick find for the disjoint set


class UnionFind:

    def __init__(self, size):
        self.parent = [i for i in range(size)]

    def find(self, x):
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            for i in range(len(self.parent)):
                if self.parent[i] == root_y:
                    self.parent[i] = root_x

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


if __name__ == '__main__':
    uf = UnionFind(10)
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(2, 4)
    uf.union(1, 3)
    uf.union(5, 6)
    uf.union(7, 8)
    uf.union(8, 9)

    print(uf.is_connected(0, 1))
