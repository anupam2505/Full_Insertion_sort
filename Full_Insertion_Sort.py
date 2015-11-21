#!/bin/python
def insertionSort(ar):    
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]

def insertionSort(arr):
            n = len(arr)-1	
            a = arr[n]
            for y in range(n,0,-1):
                if (a < arr[y-1] ):
                    ar[y] = ar[y-1]
                    arvalue = ' '.join(str(v) for v in ar)
                    #print arvalue
                elif (a >= arr[y-1]):
                    ar[y]= a
                    arvalue = ' '.join(str(v) for v in ar)
                    print arvalue
                    return;

            if (a <= ar[0]):
                ar[0]= a
                arvalue = ' '.join(str(v) for v in ar)
                print arvalue

for i in range(2,m+1):
        #print i
        insertionSort(ar[0:i])