n = int(input())
odd = n%2 
if(odd==1):
    print("Weird")
else:  
    if n >= 2 and n <= 5:
        print ("Not Weird")
if n >= 6 and n <= 20:
    print ("Weird")
if n >20:
    print ("Not Weird")
    