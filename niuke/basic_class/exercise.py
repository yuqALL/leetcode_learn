import sys

sys.path.append('..')
from basic import utils


def printOddTimesNums2(nums):
    if not nums:
        return
    eor = 0
    for num in nums:
        eor ^= num
    right_one = eor & (~eor + 1)
    onenum = 0
    for num in nums:
        if right_one & num == 0:
            onenum ^= num
    othernum = eor ^ onenum
    return onenum, othernum


def smallSum(nums):
    if not nums or len(nums) < 2:
        return 0

    def merge(nums, le, mid, ri):
        t = [0] * (ri - le + 1)
        i = 0
        p1 = le
        p2 = mid + 1
        res = 0
        while p1 <= mid and p2 <= ri:
            if nums[p1] < nums[p2]:
                t[i] = nums[p1]
                res += nums[p1] * (ri - p2 + 1)
                p1 += 1
            else:
                t[i] = nums[p2]
                p2 += 1
            i += 1
        while p1 <= mid:
            t[i] = nums[p1]
            i += 1
            p1 += 1
        while p2 <= ri:
            t[i] = nums[p2]
            i += 1
            p2 += 1

        for i, j in enumerate(range(le, ri + 1)):
            nums[j] = t[i]
        return res

    def process(nums, le, ri):
        if le == ri:
            return 0

        mid = le + ((ri - le) >> 1)
        return process(nums, le, mid) + process(nums, mid + 1, ri) + merge(nums, le, mid, ri)

    return process(nums, 0, len(nums) - 1)


def reversePair(nums):
    if not nums or len(nums) < 2:
        return []
    res = []

    def merge(nums, le, mid, ri, res):
        p1 = le
        p2 = mid + 1
        i = 0
        t = [0] * (ri - le + 1)
        while p1 <= mid and p2 <= ri:
            if nums[p2] >= nums[p1]:
                t[i] = nums[p1]
                p1 += 1
            else:
                t[i] = nums[p2]
                res.append((nums[p1], nums[p2]))
                p2 += 1
            i += 1

        while p1 <= mid:
            t[i] = nums[p1]
            p1 += 1
            i += 1

        while p2 <= ri:
            t[i] = nums[p2]
            p2 += 1
            i += 1

        for i, j in enumerate(range(le, ri + 1)):
            nums[j] = t[i]

        return

    def process(nums, le, ri, res):
        if le == ri:
            return
        mid = le + ((ri - le) >> 1)
        left = process(nums, le, mid, res)
        right = process(nums, mid + 1, ri, res)
        merge(nums, le, mid, ri, res)

        return

    process(nums, 0, len(nums) - 1, res)

    return res


def sortArrayDistanceLessK(nums, num):
    if not nums or len(nums) < 2:
        return nums
    p = -1
    for i in range(len(nums)):
        if nums[i] <= num:
            utils.swap(nums, i, p + 1)
            p += 1
    return nums


def NetherLandsFlag(nums, a):
    if not nums or len(nums) < 2:
        return nums

    ple = -1
    pri = len(nums)

    # for i in range(len(nums)):
    #     if nums[i] < a:
    #         utils.swap(nums, i, ple + 1)
    #         ple += 1
    # for j in range(len(nums) - 1, -1, -1):
    #     if nums[j] > a:
    #         utils.swap(nums, j, pri - 1)
    #         pri -= 1
    i = 0
    while i < pri:
        if nums[i] < a:
            utils.swap(nums, i, ple + 1)
            ple += 1
            i += 1
        elif nums[i] > a:
            utils.swap(nums, i, pri - 1)
            pri -= 1
        else:
            i += 1
    return nums


if __name__ == "__main__":
    print(printOddTimesNums2([1, 1, 3, 3, 4, 4, 4, 2, 5, 5]))
    print(smallSum([1, 3, 4, 4, 4, 2, 5]))
    print(reversePair([1, 3, 4, 4, 4, 2, 5]))
    print(sortArrayDistanceLessK([1, 3, 4, 4, 4, 2, 5], 3))
    print(NetherLandsFlag([1, 3, 4, 4, 4, 2, 5], 3))
