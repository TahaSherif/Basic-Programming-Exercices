# Write a function that returns the longest sequence of 0-s in the binary representation of a number. For example: 9=1001 => 2

def MaxZeros(n):
    
    # the binary representation of n
    print(bin(n)[2:]) 
    
    # variable to store the length  
    # of longest consecutive 0's 
    maxi = -1
  
    # to temporary store the  
    # consecutive 0's 
    cnt = 0
    while(n): 
        print(n)
        if(not(n & 1)): #f a number AND 1 is 0  (using the mask 1)
            cnt += 1
            n >>= 1
            maxi = max(maxi,cnt)
            print(n)
        else: 
            maxi = max(maxi,cnt) 
            cnt = 0
            n >>= 1
  
    return maxi
