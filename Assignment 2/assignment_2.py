class Stack():
    def __init__(self):
        self.stack = []
        self.top = -1 #empty stack
        
    def Push(self, x):
        self.top += 1
        self.stack.append(x)
        return 0
    
    def IsEmpty(self):
        if self.top == -1:
            return 1 #empty
        return 0 #not empty
    
    def Pop(self):
        if self.IsEmpty():
            return
        self.top -= 1
        return self.stack.pop(self.top + 1) #delete and return
    
    def Top(self):
        if self.IsEmpty():
            return
        return self.stack[self.top] #return

class MergeTuple():
    #objects of class MergeTuple are pushed onto the stack
    def __init__(self, start, end, flag):
        self.start = start
        self.end = end
        self.flag = flag #if True, then 1st and 2nd halves of A[start, end] are sorted - ready for merge

def merge(A, start, end):
    #A[start, mid] and A[mid+1, end] are sorted
    B = [0]*len(A) #temporary array
    mid = (start + end)//2
    p = start
    q = mid + 1
    r = start

    while p <= mid and q <= end:
        if A[p] <= A[q]:
            B[r] = A[p]
            p += 1
            r += 1
        else:
            B[r] = A[q]
            q += 1
            r += 1

    while p <= mid: #right subarray exhausted
        B[r] = A[p]
        r += 1
        p += 1

    while q <= end: #left subarray exhausted
        B[r] = A[q]
        r += 1
        q += 1

    for x in range(start, end+1):
        A[x] = B[x]

def mergesort(A, n):
    S = Stack()
    m = MergeTuple(0, n-1, False)
    S.Push(m)
    while not S.IsEmpty():
        m = S.Pop()
        if m.flag:
            merge(A, m.start, m.end)
        else:
            if(m.start < m.end):
                mid = (m.start + m.end)//2 #integer division
                S.Push(MergeTuple(m.start, m.end, True))
                S.Push(MergeTuple(m.start, mid, False))
                S.Push(MergeTuple(mid+1, m.end, False))
    return
        
    
T = int(input())
for _ in range(T):
    n = int(input())
    A = list(map(int, input().split())) #read input, typecast to int
    mergesort(A, n)
    print(*A) #print a space-separated list
    