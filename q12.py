num= int(input("enter number"))

def obtainSum(num): 

    sum = 0
    for digit in str(num):  
      sum += int(digit)       
    return sum
   
answer=obtainSum(num)
print(answer)
