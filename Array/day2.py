def ProductExceptSelf(nums):
    length=len(nums)
    L=[0]*length
    R=[0]*length
    answer=[0]*length
    L[0]=1
    for i in range(1,length):
        L[i]=nums[i-1]*L[i-1]
    R[length-1]=1
    for i in range(length-2,-1,-1):
        R[i]=nums[i+1]*R[i+1]
    for i in range(length):
        answer[i]=L[i]*R[i]
    return answer
nums=[1,2,3,4]
print("output:",ProductExceptSelf(nums))
