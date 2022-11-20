import time
lst=(100)
lst1=[]
def fun():
    start=time.time()
    for i in range(lst):
        lst1.append(i*i)
    end=time.time()
    print("The time is ",end-start)
    print(lst1)
fun()
        
    
