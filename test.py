#User function Template for python3
def max_sum(a,n):
    #code here
    s=0
    maxs=0
    v=0
    for i in range(n):
        s+=a[i]
    for i in range(n):
        v+=(a[i]*i)
    maxs=v
    print(maxs)
    print(s)
    for i in range(1,n):
        print(v)
        x=v-(s-a[i-1])+a[i-1]*(n-1)
        print(a[i-1])
        print(v)
        v=x
        print(v)
        if x>maxs:
            maxs=x
    return maxs
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3


    
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr,n))
# } Driver Code Ends