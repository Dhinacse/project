import random,time
database={}
c=0
u=0
print("---------------------WELCOME TO OUR E-BANK------------------------")
time.sleep(1)
print()
print("--------------------by Hari Balaji et Dhina-----------------------")
time.sleep(1)
print()
while True:     #HariBalaji module
    SelectUser=input("Create Account(CA)/Admin Login(AL)/User Login(L) :").upper()                                       
    if(SelectUser=="CA"):
        while True:
            import time
            print("please wait your account number is generating")
            time.sleep(2)
            l=[]
            x=random.randint(1000,2000)
            print("Your Account number is:",x)
            name=input("Your Name :")
            pas=input("Your Password :")
            while True:
                try:
                    bal=int(input("please deposit 5000Rs to activate your Account:"))
                    if(bal>=5000):
                        print("Creating your account please wait")                                                    
                        time.sleep(2)
                        print("Your account created successfully")
                        time.sleep(1)
                        print("Your current balance :",bal)

                        time.sleep(1)
                        import datetime
                        xdatetime=datetime.datetime.now()
                        date=xdatetime.strftime("%d %B %y")
                        time=xdatetime.strftime("%I:%M:%S %p")
                        l.append(x)
                        l.append(name)
                        l.append(pas)
                        l.append(bal)
                        l.append(date)
                        l.append(time)
                        database[x]=l
                        c=1
                        break
                    else:
                        print("Deposit should be more than 5000...")
                        time.sleep(2)
                    if(c==1):
                        break
                except ValueError:
                    print("Deposit Should be numerical")
                if(c==1):
                    break
            if(c==1):
                break
    elif(SelectUser=="L"):      #dhina module
        while True:
            import time
            try:
                acc=int(input("Enter your Account number:"))
                while True:
                    try:
                        username=input("Enter your username :")
                        passw=input("Enter your password :")
                        while True:
                            y=database[acc]
                            if(y[1]==username and y[2]==passw):
                                choice=input("Enter your choice(Deposit(D),Withdraw(W),Balance(B) :").upper()       
                                if(choice=="D"):
                                    try:
                                        deposit=int(input("How much do you like to deposit :"))
                                        y[3]=y[3]+deposit
                                        print("please wait...")
                                        time.sleep(1)
                                        print(deposit,"rs credited in your Account...your balance is  :",y[3])
                                        time.sleep(1)
                                        ce=input("Do you like to continue(C) or exit(E):").upper()
                                        if(ce=="E"):
                                            c=0
                                            break
                                        else:
                                            continue
                                    except ValueError:
                                        print("Deposit Should be numerical")
                                    if(c==0):
                                        break
                                if(choice=="W"):
                                    try:
                                        withdraw=int(input("How much do you like to withdraw :"))
                                        y[3]=y[3]-withdraw
                                        print("please wait...")
                                        time.sleep(1)
                                        if(y[3]>=5000):
                                            print(withdraw,"rs debited in your Account...your balance is  :",y[3])
                                            time.sleep(1)
                                            ce=input("Do you like to continue(C) or exit(E):").upper()
                                            if(ce=="E"):
                                                c=0
                                                break
                                            else:
                                                continue
                                        else:
                                            print("minimum balance should be atleast 5000rs")
                                            print("please try again")
                                            y[3]=y[3]+withdraw
                                            continue
                                    except ValueError:
                                        print("Deposit Should be numerical")
                                    if(c==0):
                                        break
                                if(choice=="B"):
                                    print("please wait...")
                                    time.sleep(1)
                                    print("your balance is :",y[3])
                                    time.sleep(1)
                                    ce=input("Do you like to continue(C) or exit(E) :").upper()
                                    if(ce=="E"):
                                        c=0
                                        break
                                    else:
                                        continue
                                if(c==0):
                                    break
                            else:
                                print("invalid login")
                                c=1
                                break
                    
                            if(c==0):
                                break
                        if(c==0):
                            break
                    except KeyError:
                        print("invalid account number")
                        break
                    if(c==0):
                        break
                else:
                    print("invalid login")
                    c=1
                    break
                if(c==0):
                    break
            except ValueError:
                print("Enter valid Account number...")
    elif(SelectUser=='AL'):         #HariBalaji module
        import time
        while True:
            ap=input("Password:")
            if(ap=='admin'):
                while True:
                    if(ap=="admin" and bool(database)==True):
                        print("1.View all stakeholders")
                        print("2.view specific stakeholder")
                        print("3.exit")
                        checkuser=input("Choose option :")
                        if(checkuser=='1'):
                            cnt=1
                            for i in database.values():
                                if(cnt==1):
                                    print("Account Number      :",i[0])
                                    cnt=cnt+1
                                if(cnt==2):
                                    print("Name                :",i[1])
                                    cnt=cnt+1
                                if(cnt==3):
                                    print("Password            :",i[2])
                                    cnt=cnt+1
                                if(cnt==4):
                                    print("Balance             :",i[3])
                                    cnt=cnt+1
                                if(cnt==5):
                                    print("Creation of Account :",i[4],i[5])                        
                                    cnt=1
                                
                                print("-------------------------------------------------")
                                time.sleep(0.5)
                            ce=input("Do you like to continue(C) or exit(E):").upper()
                            if(ce=="E"):
                                c=0
                                break
                            else:
                                continue
                    
                        elif(checkuser=='2'):
                            while True:
                                try:
                                    specific=int(input("Enter Account number:"))
                                    lis=list(database[specific])
                                    cnt=1
                                    for kl in lis:
                                        if(cnt==1):
                                            print("Account Number      :",kl)
                                            cnt=cnt+1
                                            continue
                                        if(cnt==2):
                                            print("Name                :",kl)
                                            cnt=cnt+1
                                            continue
                                        if(cnt==3):
                                            print("Password            :",kl)
                                            cnt=cnt+1
                                            continue
                                        if(cnt==4):
                                            print("Balance             :",kl)
                                            cnt=cnt+1
                                            continue
                                        if(cnt==5):
                                            print("Creation of Account :",i[4],i[5])
                                            cnt=1
                                            break
                                    print("-------------------------------------------------")
                                    time.sleep(1)
                                    ce=input("Do you like to continue(C) or exit(E):").upper()
                                    if(ce=="E"):
                                        c=0
                                        break
                                    elif(ce=='C'):
                                        c=1
                                        break
                                except KeyError:
                                    print("invalid account number")
                                    c=1
                                except ValueError:
                                    print("invalid account number")
                                    c=1
                                    
                                if(c==0):
                                    break
                                if(c==1):
                                    break
                            if(c==0):
                                break
                            if(c==1):
                                continue
                        elif(checkuser=='3'):
                            u=0
                            break
                        else:
                            print("Please choose the given field...")
                    if(c==1):
                        continue
                    else:
                        print("no stakeholder currently ....redirect to home")
                        time.sleep(2)
                    if(u==0):
                        break
                if(u==0):
                    break
            else:
                print("invalid password")
                continue
                    
    else:
        print("please choose the given criteria....")
