def subStringIndex(str1, str2):
    if len(str2) > len(str1):
        return -1
    next_arr = _gen_next_arr(str2)
    i = 0
    j = 0
    while i < len(str1) and j < len(str2):
        if str2[j] == str1[i]:
            i += 1
            j += 1
        elif next_arr[j] == -1:
            i += 1
        else:
            j = next_arr[j]
    if j == len(str2):
        return i - j
    return -1


def _gen_next_arr(str):
    next = [0] * len(str)
    next[0] = -1
    cn = 0
    for i in range(2, len(str)):
        if str[i - 1] == str[cn]:
            cn += 1
            next[i] = cn
            i += 1
        elif cn > 0:
            cn = next[cn]
        else:
            next[i] = 0
            i += 1
    return next


if __name__ == "__main__":
    print(_gen_next_arr("aabaabc"))
    print(subStringIndex("aabaabc", "aabc"))
