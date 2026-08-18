'''fa = eval(input("Follows Account: "))
if fa:
    cf = eval(input("Close Friend: "))
    if cf:
        print("You can see the story")
    else :
        print("Not in the close friend List")
else:
    print("Follow the Account First")



reg = eval(input("Registered : "))
if reg:
    fee = eval(input("Fee Paid : "))
    if fee:
        print("Tournament Entry Confirmed")
    else:
        print("Entry Fee Pending")
else:
    print("Register Required")
    
link= eval(input("Link Active: "))
if link:
    access = eval(input("Access Granted: "))
    if access:
        print("File Open Successfully")
    else:
        print("Access Denied")
else:
    print("Invalid File Link")'''
    
    
    
data = {
        'Saikiran':{'status':True,'python':90,'java':95,'mysql':98},        
        'Bunny':{'status':False,'python':None,'java':None,'mysql':None},
        'Prasad':{'status':True,'python':85,'java':80,'mysql':75},
        'Nikhil':{'status':True,'python':60,'java':65,'mysql':65},
        'Tarun':{'status':True,'python':35,'java':30,'mysql':38},
    }
    
name = input("Enter the name: ")
if name in data :
        if data[name]['status']:
            sum = data[name]['python'] + data[name]['java'] + data[name]['mysql']
            avg = sum/3
            print(f"Hello {name}!!!")
            print(f"Your Average Score is : {avg}")
            if avg >=  90 :
                print("Good Performance")
            elif avg >= 80:
                print("Good")
            elif avg >= 70:
                print("Good,Work Hard")
            elif avg >=35:
                print("Poor Performance, Work Hard")
            else:
                print("You are Failed,Work Hard")
        else:
              print(f"{name} Did not attend the Exam")
else:
    print(f"{name} is not a valid name")
        