'''username = input("Enter your username : ")
password = input("Enter your password : ")
if username=="admin" and password=="admin123":
    print("Login Successful")
else:
    print("Login Failed")
    
products = ['Laptop', 'Mobile', 'Tablet', 'Mouse', 'Keyboard']
search = input("Enter the product to search : ")
if search in products:
    print("Product Found")
else:
    print("Product Not Found")'''
    
bill = int(input("Enter the bill amount : "))
if bill <= 99:
    print("Final Bill:", bill)
else:
    print("Final Bill:", bill + 10)