
def binarySearch(nums,num):
    start=0
    end=len(nums)-1
    while start<end:
        mid=start+((end-start)>>1)
        if nums[mid]>=num:
            end=mid
        else:
            start=mid+1
    return start

def rightMost(nums,num):
    start=0
    end=len(nums)-1
    while start<end:
        mid=start+((end-start)>>1)+1
        if nums[mid]>num:
            end=mid-1
        else:
            start=mid
    return start

if __name__=="__main__":
    nums=[1,2,3,4,4,4,5,7,8,9]
    print(binarySearch(nums,6))
    print(rightMost(nums,4))