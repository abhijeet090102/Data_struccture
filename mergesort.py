class merge:
    def __init__(self,arr):
        self.arr = arr
        self.c = [0 for i in range(len(arr)+4)]
        
    def merge1(self,lb,mid,ub):
        print(lb,mid,ub)
        i = lb
        j = mid +1
        k = 0
        while i<=mid and j<=ub:
            if self.arr[i] <= self.arr[j]:
                print(i,j)
                self.c[k] = self.arr[i]
                i+=1
                k += 1
            print(i,j)
            print('\n')
            if self.arr[j] < self.arr[i]:
                print(i,j)
                self.c[k] = self.arr[j]
                j += 1
                k+=1
        while i<= mid:
            self.c[k] = self.arr[i]
            k+=1
            i+= 1
        while j<= ub:
            self.c[k] = self.arr[j]
            k+= 1
            j+=1
        k = 0
        i = lb
        while i<=ub:
            self.arr[i] = self.c[k]
            i+=1
            k+=1
    def mergesort(self,lb,ub):
        if lb< ub:
            mid = (lb+ub)//2
            self.mergesort(lb,mid)
            self.mergesort(mid+1,ub)
            self.merge1(lb,mid,ub)
    def display(self):
        print(self.arr)
        
l = [20,10,30,12,15,25,40,36,48,18]
ob = merge(l)
ob.mergesort(0,len(l)-1)
ob.display()


        
