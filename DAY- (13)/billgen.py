'''data ={
    'English willow bat' : 9000,
    'Kashmir willow bat' : 4000,
    'Grace ball': 450,
    'Tennis ball' : 100,
    'Tigh pad' : 500,
    'Gloves': 900,
    'Guard': 250,
    'Spikes Shoes': 5000,
    'Shoes': 2000,
    
}
for i in data :
    print(i.ljust(20),data[i])
products = input("Enter the products:",).split(",")
print("Bill-------------------")
bill = 0
for i in products:
    print(i.ljust(20),data[i])
    bill += data[i]
print("Total Bill :".ljust(20),bill)

s='Python programming'
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)


s='sssddddfffffeeeeessssgggg'
c=1
res = ''
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        res+=s[i]+str(c)
        c=1
print(res+s[i]+str(c))
'''





