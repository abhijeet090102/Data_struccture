def Quick(arr,s,e):
        piv = s
        lef = s+1
        righ = e
        while 1:
            while lef <= righ and  arr[piv]<= arr[righ]  :
                #print(righ)    
                righ = righ -1
            if arr[piv] > arr[righ]:
                arr[piv], arr[righ]=arr[righ],arr[piv]
                piv = righ
                righ = righ-1
            if lef > righ :
                return piv
            while lef <= righ and arr[piv] >= arr[lef] :
                lef +=1
            
            if arr[piv] < arr[lef] :
                arr[piv], arr[lef]=arr[lef],arr[piv]
                piv = lef
                lef += 1
            if lef > righ :
                return piv
        
def Quicksort(arr,s,e):
    #s = 0
    #e = len(arr)-1
    if s<e :
        p = Quick(arr,s,e)
        print(p)
        Quicksort(arr,s,p-1)
        Quicksort(arr,p+1,e)

                
arr= [17,15,6,7,28,9,16,18]
Quicksort(arr,0,len(arr)-1)
print(arr)
