class  BubbleSort:
    def __init__(self,arr,data):
        self.arr = arr
        self.data = data
        self.size = len(arr)
        for i in self.arr:
            if type(i) != self.data:
                print('list is not valid')
                exit()
    def Display(self):
        print(self.arr)
    def bubbleSort (self):
        
        for i in range(1,self.size):
            for j in range(0,self.size-1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]

    def Insert(self,n):
        self.arr.append(n)
        self.size += 1
        print('One element is Insert')
        
    def Delete(self,d):
        self.arr.remove(d)
        self.size -= 1
        print(f'{d} element is Deleted')
        
l = [4,10,60,8,9,16,18]
ob = BubbleSort(l,int)
ob.Display()
ob.bubbleSort()
ob.Insert(2)
ob.bubbleSort()
ob.Display()
ob.Delete(10)
ob.Display()


