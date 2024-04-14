class QuickSort:
    def __init__(self,a,da):
        self.arr = a
        self.data = da
        self.size = len(self.arr)
        for i in self.arr:
            if type(i) != self.data:
                print('List is not valid')
                exit()
                
    def Display(self):
        print(self.arr)
        
    def Quick(self,s,e):
        piv = s
        lef = s+1
        right = e
        while 1:
            while  lef <= right and self.arr[piv]< self.arr[right] :
                right = right -1
            if self.arr[piv] > self.arr[right]:
                self.arr[piv],self.arr[right] = self.arr[right],self.arr[piv]
                piv = right
                right = right-1
            if lef > right :
                return piv
            while lef <= right and self.arr[piv] >= self.arr[lef]  :
                lef +=1
            
            if self.arr[piv] < self.arr[lef] :
                self.arr[piv], self.arr[lef] = self.arr[lef], self.arr[piv]
                piv = lef
                lef += 1
            if lef > right :
                return piv
            
    def Quick_Sort(self,s,e):
    #s = 0
    #e = self.size-1
        if s<e :
            p = self.Quick(s,e)
            self.Quick_Sort(s,p-1)
            self.Quick_Sort(p+1,e)
    def Insert (self,n):
        self.arr.append(n)
        self.size += 1
        return print('Item is inserted')
    def Delete (self,d):
        self.arr.remove(d)
        self.size -= 1
        return print('one item is deleted')

l= [20,50,46,70,8,9,16,18]
obj = QuickSort(l,int)
obj.Display()
obj.Quick_Sort(0,7)
obj.Display()
obj.Insert(2)
obj.Quick_Sort(0,len(l)-1)
obj.Display()
obj.Delete(8)
obj.Display()
                
