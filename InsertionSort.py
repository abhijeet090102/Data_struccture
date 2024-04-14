class  InsertionSort:
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
    def insertionSort (self):
        for i in range(1,self.size):
            item = self.arr[i]
            pos = i-1
            while item < self.arr[pos] and pos >= 0:
                self.arr[pos+1] = self.arr[pos]
                pos -= 1
            self.arr[pos+1] = item
    def Insert(self,n):
        self.arr.append( n)
        print('One element is Insert')
        self.size += 1
    def Delete(self,d):
        self.arr.remove(d)
        print('One element is Deleted')
        self.size -= 1
l = [4,20,60,8,9,16,18]
obj= InsertionSort(l,int)
obj.Display()
obj.insertionSort()
obj.Display()
obj.Insert(8)
obj.insertionSort()
obj.Delete(20)
obj.Display()
