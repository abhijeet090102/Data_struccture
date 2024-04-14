class merge:
    def __init__(self,arr,lb,ub):
        self.arr = arr
        self.c = []
        self.lb = lb
        self.ub = ub
    def merge(self,lb,mid,ub):
        i = self.lb
        j = self.mid +1
        k = 0
        while i<=self.mid and j<=self.ub:
            while self.arr[i] <= self.arr[j]:
                self.c[k] = self.arr[i]
                i+=1
                k += 1
            while self.arr[j] <= self.arr[i]:
                self.c[k] = self.arr[j]
                j += 1
                k+=1
        while i< self.mid:
            self.c[k] = self.arr[i]
            k+=1
            i+= 1
        while j< self.ub:
            self.c[k] = self.arr[j]
            k+= 1
            j+=1
        k = 0
        i = lb
        while i<=self.ub:
            self.arr[i] = self.c[k]
            i+=1
            k+=1
    def mergesort(self,lb,ub):
        while self.lb< self.ub:
            self.mid = (self.lb+self.ub)//2
            self.mergesort(self.lb,self.mid)
            self.mergesort(self.mid+1,self.ub)
            self.merge(self.lb,self.mid,self.ub)
    def display(self):
        print(self.arr)
        
l = [20,10,30,12,15,25,40,36,48,18]
ob = merge(l,0,len(l)-1)
ob.mergesort(0,len(l)-1)
ob.display()


        
