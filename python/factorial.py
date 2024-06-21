# factorial and trailing zeroes

def number(a,c=1):
    while True:
        if(a==1 or a == 0):
            break
        else:
            c *= a
            a = a-1
    return c 

def trailnumber(a,c=0):
    n=e=0
    j=5
    while True:
        if(a==1 or a == 0):
            break  
        if(a%10==0):
            n = n + 1 

        if(a%10==5): 
            while True:
                if(a==10):
                    print("ok")


        
    return n+e
print(number(6))  
print(trailnumber(25))  
print("hello")     
