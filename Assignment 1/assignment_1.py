def InversionCount(A, B, start, end):
    count = 0
    if start < end:
        mid = (start + end)//2

        count += InversionCount(A, B, start, mid)
        count += InversionCount(A, B, mid+1, end)
        count += MergeAndCount(A, B, start, mid, end)

    return count

def MergeAndCount(A, B, start, mid, end):
    p = start
    q = mid + 1
    r = start
    count = 0

    while p <= mid and q <= end:
        if A[p] <= A[q]:
            B[r] = A[p]
            p += 1
            r += 1
        else:
            B[r] = A[q]
            count += (mid - p + 1)
            q += 1
            r += 1

    while p <= mid:
        B[r] = A[p]
        r += 1
        p += 1

    while q <= end:
        B[r] = A[q]
        r += 1
        q += 1

    for x in range(start, end+1):
        A[x] = B[x]

    return count

k = int(input())
for _ in range(k):
    n = int(input())
    A = list(map(int, input().split())) #read input array
    B = [0]*n #create output array
    print(InversionCount(A, B, start=0, end=n-1))
    
    
    