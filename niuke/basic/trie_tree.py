# 前缀树

# 前缀树 数组实现
class Node:
    def __init__(self):
        size = 26
        self.e = 0
        self.next = [None for _ in range(size)]


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        n = len(word)
        cur = self.root
        for i in range(n):
            ind = ord(word[i]) - ord('a')
            if cur.next[ind] == None:
                cur.next[ind] = Node()
            cur = cur.next[ind]
            if i == n - 1:
                cur.e += 1

    def search(self, word: str) -> bool:
        n = len(word)
        cur = self.root
        for i in range(n):
            ind = ord(word[i]) - ord('a')
            if cur.next[ind] == None:
                return False
            else:
                cur = cur.next[ind]
                if i == n - 1 and cur.e == 0:
                    return False
        return True

    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        cur = self.root
        for i in range(n):
            ind = ord(prefix[i]) - ord('a')
            if cur.next[ind] == None:
                return False
            else:
                cur = cur.next[ind]
        return True


class Node:
    def __init__(self, g):
        self.g = g
        self.p = 0
        self.e = 0
        self.next = set()

    def __repr__(self):
        next_a = set()
        for nd in self.next:
            next_a.add(nd.g)
        return '{}(p:{} e:{} next:{})'.format(self.g, self.p, self.e, next_a)


class Trie:

    def __init__(self):
        self.root = Node('')

    def insert(self, word: str) -> None:
        n = len(word)
        cur = self.root
        i = 0
        while i < n:
            found = False
            for nd in cur.next:
                if nd.g == word[i]:
                    if i == 0:
                        nd.p += 1
                    if i == n - 1:
                        nd.e += 1
                    cur = nd
                    i += 1
                    found = True
                    break
            if not found:
                nd = Node(word[i])
                if i == 0:
                    nd.p += 1
                if i == n - 1:
                    nd.e += 1
                cur.next.add(nd)
                i += 1
                cur = nd

    def search(self, word: str) -> bool:
        n = len(word)
        cur = self.root
        i = 0
        while i < n:
            if not cur.next:
                return False
            found = False
            for nd in cur.next:
                if nd.g == word[i]:
                    print(nd)
                    if (i == 0 and nd.p == 0) or (i == n - 1 and nd.e == 0):
                        return False
                    cur = nd
                    i += 1
                    found = True
                    break
            if not found:
                return False
        return True

    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        cur = self.root
        i = 0
        while i < n:
            if not cur.next:
                return False
            found = False
            for nd in cur.next:
                if nd.g == prefix[i]:
                    if i == 0 and nd.p == 0:
                        return False
                    cur = nd
                    i += 1
                    found = True
                    break
            if not found:
                return False
        return True


trie = Trie()
print(trie.search('a'))
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))
