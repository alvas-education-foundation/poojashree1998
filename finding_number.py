def getMissingNo(A): 
    n = len(A) 
    tot = (n + 1)*(n + 2)/2
    sum1 = sum(A) 
    return tot - sum1
  
A = [1, 2, 4, 5, 6] 
miss = getMissingNo(A) 
print(miss)
