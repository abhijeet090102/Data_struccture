class LinearList :
    def __init__ (self,arr,data):
        self.arr = arr
        self.size = len(arr)
        self.data = data
        for i in self.arr: 
            if type(i) != data:
                print("list is  not valid",type(i))
            
                exit()
    def Display(self):
        print(self.arr)
                
    def LinearSearch (self,item):
        for i in range(self.size):
            if item == self.arr[i]:
                #print(f'Match found ')
                return i
                
        #else:
                #print('Match not found')
        return -1  
    def Insert (self,a):
        self.arr.append(a)
    def Delete(self,m):
        self.arr.remove(m)

l= LinearList([4,5,6,8,9,4.2],int)
l.Display()
print(l.LinearSearch(10))
l.Insert(8)
l.Display()
l.Delete(8)
l.Display()
