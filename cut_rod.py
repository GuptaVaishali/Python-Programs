import array as arr
import math

def cut_rod(p,length):
    
    maxProfit = arr.array('i',[])
    maxProfit.append(0)
    
    for i in range(1,length+1):
        
        max_price = -math.inf
        
        for j in range(1,i+1):
            price = p[j-1] + maxProfit[i-j]
            if price > max_price:
                max_price = price
                
        maxProfit.append(max_price)
        
    return maxProfit[length]

def main():
    length = int(input("Enter the length of rod "))
    p = arr.array('i',[])
    for i in range(length):
        p.append(int(input("Enter the prices of each length of rod ")))
    max_profit = cut_rod(p,length)
    print(max_profit)

main()
