def max_sum(a,n):
    cum_sum=0
    for i in range(0,n):
        cum_sum=cum_sum+a[i]
    initial_value=0
    mx=0
    for i in range(0,n):
        initial_value+=i*a[i]
        mx=initial_value
    for i in range(1,n):
        temp=initial_value-(cum_sum-a[i-1])+a[i-1]*(n-1)
        initial_value=temp
        if(temp>mx):
            mx=temp
    return mx

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr,n))