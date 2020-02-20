import random as rand
def generateArray(max_size,max_value):
    size=rand.randint(0,max_size)
    arr=[]
    for i in range(size):
        arr.append(rand.randint(0,max_value))
    return arr


if __name__=="__main__":
    arr=generateArray(100,10000)
    print(arr)