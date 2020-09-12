from array import *
import random as rand
import time

def quickSort(a,low,high):
    if low<high:
        p = partition(a,low,high)
        quickSort(a,low,p-1)
        quickSort(a,p+1,high)
    
def partition(a,low,high):
    start = low
    end = high
    pp = low
    pe = a[low]
    while(start<end):
        while start<end and a[start] <= pe:
            start+=1
        while a[end] > pe :
            end-=1
        if start<end:
            a[start],a[end] = a[end],a[start]
            
    if pp!=end:
        a[pp], a[end] = a[end],a[pp]
        
    return end

def mergeSort(a,low,high):
    if low<high:
        mid = int( (low + high)/2 )
        mergeSort(a,low,mid)
        mergeSort(a,mid+1,high)
        merge(a,low,mid,high)

def merge(a,low,mid,high):
    i=low
    j=mid+1
    k=0
    c = array('i' , [])
    while i<=mid and j<=high:
        if a[i] <= a[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(a[j])
            j+=1
    while i<=mid:
        c.append(a[i])
        i+=1
    while j<=high:
        c.append(a[j])
        j+=1
    
    for k in range(len(c)):
        a[low+k] = c[k]
    
    
def main():
    n = int(input("Enter the size of array"))
    a = array('i' , [])
    for i in range(n):
        a.append(rand.randrange(1,9000))
 #       a.append(int(input("Enter the element")))
    start_time = time.time()
    quickSort(a,0,n-1)
    end_time = time.time()
    time1 = end_time - start_time
    print(time1)
  
    start_time1 = time.time()
    mergeSort(a,0,n-1)
    end_time1 = time.time()
    time2 = end_time1 - start_time1
    print(time2)
    
    rd=time1 - time2
    print(rd)
 #   for i in range(n):
 #       print(a[i])
main()
