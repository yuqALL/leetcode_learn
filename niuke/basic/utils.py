import random as rand
import time, timeit


def generateArray(max_size, max_value):
    size = rand.randint(0, max_size)
    arr = []
    for i in range(size):
        arr.append(rand.randint(0, max_value))
    return arr


def generatePostiveArray(max_size, max_value):
    size = rand.randint(0, max_size)
    arr = []
    for i in range(size):
        arr.append(rand.randint(1, max_value))
    return arr


def swap(nums, i, j):
    if i == j or i >= len(nums) or j >= len(nums):
        return
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp
    return


def swap_xor(nums, i, j):
    if i == j or i >= len(nums) or j >= len(nums):
        return
    nums[i] = nums[i] ^ nums[j]
    nums[j] = nums[i] ^ nums[j]
    nums[i] = nums[i] ^ nums[j]
    return


def clock(func):
    def clocked(*args, **kwargs):
        t0 = timeit.default_timer()
        result = func(*args, **kwargs)
        elapsed = timeit.default_timer() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked


def isEqual(arr1, arr2):
    if not arr1 and not arr2:
        return True

    if len(arr1) != len(arr2):
        return False

    for a, b in zip(arr1, arr2):
        if a != b:
            return False
    return True


def comparator(func1, func2, input1, input2):
    func1(input1)
    func2(input2)
    return isEqual(input1, input2)
