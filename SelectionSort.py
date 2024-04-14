class  SelectionSort:
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
    def SelectionSort (self):
        for i in range(0,self.size-1):
            for j in range(i+1,self.size):
                if self.arr[i] > self.arr[j]:
                    self.arr[i] ,self.arr[j] = self.arr[j], self.arr[i]
    def Insert(self,n):
        self.arr.append( n)
        print('One element is Insert')
    def Delete(self,d):
        self.arr.remove(d)
        print('One element is Deleted')
l = [4,10,60,8,9,16,18]
obj= SelectionSort(l,int)
obj.Display()
obj.SelectionSort()
obj.Display()
obj.Insert(8)
obj.Delete(8)
obj.Display()
