class BubbleSort:
    def __init__(self,arr,data):
        self.arr = arr
        self.data = data
        self.size = len(self.arr)
        for i in self.arr:
            if type(i) != self.data:
                print("The array is valid ")
                exit()
    def Bubblesort(self):
        for i in range(1,self.size):
            c = 0
            for j in range(0,self.size-1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j],self.arr[j+1] = self.arr[j+1],self.arr[j]
                    c += 1
            if c == 0:
                break
    def display(self):
        print('the sorted array ',self.arr)

l = [20,4,50,26,9,16,18]
am = BubbleSort(l,int)
am.Bubblesort()
am.display()
