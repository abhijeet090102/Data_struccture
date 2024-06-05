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
        piv = s # passed by user what is pivot positon 
        lef = s+1 # left will choose to pivots next position if pivot will chooses to 0 index
        right = e # size of the array -1 is right position 
        while 1:
            '''Checking if left end is smaller and equal than right and array element of pivot position is smaller than
            array element of right position than only changing the right to its before position'''
            while  lef <= right and self.arr[piv]< self.arr[right] :
                right = right -1
            if self.arr[piv] > self.arr[right]: # checking if array of pivot position is grater than its right position than swap 
                self.arr[piv],self.arr[right] = self.arr[right],self.arr[piv]
                piv = right     # if condition true than pivot will change to its swaping position 
                right = right-1     # and right posititon will shift to its before position

            if lef > right : # if left position is greater than right than stoping all the condition and return pivot index
                return piv
            while lef <= right and self.arr[piv] >= self.arr[lef]  :    
# checking again and again until it false the condition if array of pivot position is grater than array of left position than left will change to its next position 
                lef +=1
            
            if self.arr[piv] < self.arr[lef] : # if array element of pivot posititon is less than its left position element than swap 
                self.arr[piv], self.arr[lef] = self.arr[lef], self.arr[piv]
                piv = lef # if true than pivot will change to its left position 
                lef += 1 # and left will shift to its next position 
            if lef > right : # if left is greater than right than loop will stop and return pivot positon 
                return piv
            
    def Quick_Sort(self,s,e):
    #s = 0
    #e = self.size-1
        if s<e : # True when start is smaller than end position 
            p = self.Quick(s,e) # calling the Quick function if start is smaller than end position and storing return value

            self.Quick_Sort(s,p-1) # calling itself with (start and return value -1 )for left hand side element sorting

            # calling itself again and again when condition is true until when find one sorted element
            self.Quick_Sort(p+1,e) # pivot's right hand side sorting calling itself untill all element is sorted 
    def Insert (self,n):
        self.arr.append(n) # insert element at last end 
        self.size += 1 # size will increased when element is inserted 
        return print('Item is inserted')
    def Delete (self,d):
        self.arr.remove(d) # when element is called and found it will remove it from array 
        self.size -= 1 # and size OF array will be decreased 
        return print('one item is deleted')

l= [20,50,46,70,8,9,16,18]
obj = QuickSort(l,int)
obj.Display()
obj.Quick_Sort(0,len(l)-1)
obj.Display()
obj.Insert(2)
obj.Display()
obj.Quick_Sort(0,len(l)-1)
obj.Display()
obj.Delete(8)
obj.Display()
                
