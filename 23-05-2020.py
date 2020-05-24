#remove ith element
def remove(string, i):  
  
    for j in range(len(string)): 
        if j == i: 
            string = string.replace(string[i], "", 1) 
    return string 
      

if __name__ == '__main__': 
      
    string = "geeksFORgeeks"
    i = 5 
    print(remove(string, i)) 
