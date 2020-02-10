class Node:
    def __init__(self):
        self.len = 0
        self.link = 0
        # self.next = [i for i in range(26)]
        self.next = {}


# https://oi-wiki.org/string/sam/#_8
class SAM:

    def __init__(self, size):
        self.st = [Node() for _ in range(size)]
        self.st[0].len = 0
        self.st[0].link = -1
        self.size = 1
        self.last = 0

    def extend(self, ch):
        cur = self.size
        self.size += 1
        self.st[cur].len = self.st[self.last].len + 1
        p = self.last
        while p != -1 and ch not in self.st[p].next:
            self.st[p].next[ch] = cur
            p = self.st[p].link
        if p == -1:
            self.st[cur].link = 0
        else:
            q = self.st[p].next[ch]
            if self.st[p].len + 1 == self.st[q].len:
                self.st[cur].link = q
            else:
                clone = self.size
                self.size += 1
                self.st[clone].len = self.st[p].len + 1
                self.st[clone].next = self.st[q].next
                self.st[clone].link = self.st[q].link
                while p != -1 and self.st[p].next[ch] == q:
                    self.st[p].next[ch] = clone
                    p = self.st[p].link
                self.st[q].link = self.st[cur].link = clone
        self.last = cur
