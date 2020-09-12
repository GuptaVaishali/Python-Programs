from array import *
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
    
def main():
    n = int(input("Enter the size of array "))
    a = array('i' , [])
    for i in range(n):
        a.append(int(input("Enter the element ")))
    quickSort(a,0,n-1)
    for i in range(n):
        print(a[i])
main()
