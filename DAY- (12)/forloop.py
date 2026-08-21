#str list tuple set dict range
#syntax
'''for var in seq:
     #stmts
   
s = "python programming"
for i in s:
    print(i) 
    

l=[1,2,3,4,5]
for list in l:
    print(list)



t = (1589,8754,5487,77)
for i in t :
    print(i)
  


names = {"Sai Kiran","Nikhil","prasad","Tarun"}
for name in names:
    print(name)
    

d = {1:2,2:4,3:6,4:8,5:10}
for key in d:
    print(key,d[key])


#syntax of range
range(start,end+1,step):(0,,1)

for i in range(1,11):
    print(i)

for i in range(2,21,2):
    print(i)

for i in range(5,101,5):
    print(i)

for i in range(19,0,-2):
    print(i)

s="python programming language"
for i in range(len(s)):
    print(i,s[i])

s=[12,34,43,53,54]
for i in range(len(s)):
    print(i,s[i])

s = (12,23,32,43,54)
for i in range(len(s)):
    print(i,s[i])

#enumarate function

s="python programming"
for i in enumerate(s):
    print(i)

s=[12,23,45,31,85]
for i in enumerate(s):
    print(i)

s=(78,89,65,46,90)
for i in enumerate(s):
    print(i)

s={78,89,65,46,90}    
for i in enumerate(s):
    print(i)
       
d={1:2,2:4,3:6,4:8,5:10}
for i in enumerate(d):
    print(i[0],i[1],d[i[1]])

#break and continue 

for i in range(1,11):
    if i==5:
        break
    print(i)

for i in range(1,11):
    if i==5:
        continue
    print(i)

for i in range(1,11):
    if i==9:
        break
    print(i)
else:
    print("End of the loop")


l=[12,13,14,15,16,17,18,19]
n=45
for i in l:
    if i==n:
        print(n,"found")
        break
else:
    print(n,"not found")


pin = 1234
for i in range(5):
    epin = int(input("Enter your pin:"))
    if epin==pin:
        print("Phone has been Unlocked")
        break
    else:
        print("Invalid Pin")
else:
    print("Try after 30secs")
#prime 

n= int(input("Enter a number:"))
for i in range(2,n//2+1):
    if n%i==0:
        print("Not a Prime number") 
        break
else:
     print(f"{n} is a Prime number")
'''        