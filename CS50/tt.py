
list= ["a", "a", "b", "c", "d", "e", "f"] 

 
for x in range(0, len(list)-1):
    if(list[x]==list[x+1]):
        print("Duplicate found!")
        print(x)
    
    

print(list) 