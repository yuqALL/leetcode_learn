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


class SmallHeap:
    def __init__(self, nums):
        self.nums = nums

    # 小端
    def heapifyS(self, start, size):
        root = 0
        left = (root << 1) + 1
        right = left + 1
        print(self.nums[start:start + size])
        while left < size:
            smallind = right if right < size and self.nums[start + right] < self.nums[start + left] else left
            smallind = smallind if self.nums[start + smallind] < self.nums[start + root] else root
            if smallind == root:
                break
            utils.swap(self.nums, start + smallind, start + root)
            root = smallind
            left = (root << 1) + 1
            right = left + 1

    # 大端
    def heapifyB(self, start, size):
        left = (start << 1) + 1
        right = left + 1
        while left < start + size:
            bigger = right if right < start + size and self.nums[right] > self.nums[left] else left
            bigger = bigger if self.nums[bigger] > self.nums[start] else start
            if bigger == start:
                break
            utils.swap(self.nums, bigger, start)
            start = bigger
            left = (start << 1) + 1
            right = left + 1


def sortArray(nums, num):
    if not nums or len(nums) < 2:
        return nums
    p = -1
    for i in range(len(nums)):
        if nums[i] <= num:
            utils.swap(nums, i, p + 1)
            p += 1
    return nums


def sortArrayDistanceLessK(nums, k):
    if not nums or len(nums) < 2:
        return nums
    smallHeap = SmallHeap(nums)
    for i in range(len(nums) - k):
        smallHeap.heapifyS(i, k + 1)
    i = len(nums) - k
    while i < len(nums) and k > 0:
        smallHeap.heapifyS(i, k)
        k -= 1
        i += 1
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


class Node:
    def __init__(self, n):
        self.value = n
        self.next = None


class SmallerEqualBigger:

    def listPartition1(self, head, pivot):
        if head is None or not isinstance(head, Node):
            return head
        cur = head
        i = 0
        # 记录链表长度
        while cur is not None:
            i += 1
            cur = cur.next
        # 生成结果保存链表，复制原始链表的值
        nodeArr = [Node() for _ in range(i)]
        cur = head
        for i in range(len(nodeArr)):
            nodeArr[i] = cur
            cur = cur.next

        self.arrPartition(nodeArr, pivot)

        # 建立链接
        for i in range(1, len(nodeArr) - 1):
            nodeArr[i - 1].next = nodeArr[i]
        nodeArr[-1].next = None
        return nodeArr[0]

    def arrPartition(self, nodeArr, pivot):
        small = -1
        big = len(nodeArr)
        index = 0
        while index != big:
            if nodeArr[index].value < pivot:
                small += 1
                self.swap(nodeArr, small, index)
                index += 1
            elif nodeArr[index].value == pivot:
                index += 1
            else:
                big -= 1
                self.swap(nodeArr, big, index)

    def swap(self, nodeArr, a, b):
        tmp = nodeArr[a]
        nodeArr[a] = nodeArr[b]
        nodeArr[b] = nodeArr[a]

    def listPartition2(self, head, pivot):
        sH = None
        sT = None
        eH = None
        eT = None
        bH = None
        bT = None
        nextNode = None
        while head is not None:
            nextNode = head.next
            head.next = None
            if head.value < pivot:
                if sH == None:
                    sH = head
                    sT = head
                else:
                    sT.next = head
                    sT = head
            elif head.value == pivot:
                if eH == None:
                    eH = head
                    eT = head
                else:
                    eT.next = head
                    eT = head
            else:
                if bH == None:
                    bH = head
                    bT = head
                else:
                    bT.next = head
                    bT = head
            head = nextNode

        if sT is not None:
            sT.next = eH
            eT = sT if eT == None else eT

        if eT is not None:
            eT.next = bH

        res = sH if sH is not None else (eH if eH is not None else bH)
        return res

    def printLinkedList(self, node):
        s = ''
        while node is not None:
            s += str(node.value) + ' '
            node = node.next
        print('Linked List: ', s)

    def test(self):
        head1 = Node(7)
        head1.next = Node(9)
        head1.next.next = Node(1)
        head1.next.next.next = Node(8)
        head1.next.next.next.next = Node(5)
        head1.next.next.next.next.next = Node(2)
        head1.next.next.next.next.next.next = Node(5)
        self.printLinkedList(head1)
        # // head1 = listPartition1(head1, 4);
        head1 = self.listPartition2(head1, 5)
        self.printLinkedList(head1)


if __name__ == "__main__":
    # print(printOddTimesNums2([1, 1, 3, 3, 4, 4, 4, 2, 5, 5]))
    # print(smallSum([1, 3, 4, 4, 4, 2, 5]))
    # print(reversePair([1, 3, 4, 4, 4, 2, 5]))
    # print(sortArray([1, 3, 4, 3, 4, 4, 6, 5], 2))
    # print(NetherLandsFlag([1, 3, 4, 4, 4, 2, 5], 3))
    # print(sortArrayDistanceLessK([1, 3, 4, 3, 4, 4, 6, 5], 2))
    SmallerEqualBigger().test()
