def search(word: str) -> bool:
    n = len(word)
    i = 0
    cur = word[0]
    while i < n:
        for nd in ['a', 'b', 'c']:
            if nd == word[i]:
                cur = nd
                i += 1
                break
        return False
    return True

print(search('abcd'))