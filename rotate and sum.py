def rotate_right(a):
    for i in range(1):
        last=arr[(len(a))-1]
        for j in range(n-1,-1,-1):
            arr[j]=arr[j-1]
        a[0]=last
    return a
def max_sum(a,n):
    #code here
    temp=[]
    maxs=0
    for i in range(n):
        s=0
        temp=rotate_right(a)
        for j in range(n):
            s=s+(temp[j]*j)
        if s>maxs:
            maxs=s
    return maxs



#  Driver Code Starts
#Initial Template for Python 3


    
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr,n))
# } Driver Code Ends