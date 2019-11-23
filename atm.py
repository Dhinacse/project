import random,time
dic={}
c=0
u=0
print("---------------------WELCOME TO OUR E-BANK------------------------")
time.sleep(1)
print()
print("--------------------by Hari Balaji et Dhina-----------------------")
time.sleep(1)
print()
while True:
    createAcc=input("Create Account(CA)/Admin Login(AL)/User Login(L) :").upper()
    if(createAcc=="CA"):
        while True:
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
                        l.append(x)
                        l.append(name)
                        l.append(pas)
                        l.append(bal)
                        dic[x]=l
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
    elif(createAcc=="L"):
        while True:
            acc=int(input("Enter your Account number:"))
            while True:
                try:
                    username=input("Enter your username :")
                    passw=input("Enter your password :")
                    while True:
                        y=dic[acc]
                        if(y[1]==username and y[2]==passw):
                            choice=input("Enter your choice(Deposit(D),Withdraw(W),Balance(B) :").upper()
                            if(choice=="D"):
                                deposit=int(input("How much do you like to deposit :"))
                                y[3]=y[3]+deposit
                                print("please wait...")
                                time.sleep(1)
                                print(deposit,"rs credited in your Account...your balance is  :",y[3])
                                time.sleep(1)
                                ce=input("Do you like to continue(C) or exit(E):")
                                if(ce=="E"):
                                    c=0
                                    break
                                else:
                                    continue
                            if(choice=="W"):
                                withdraw=int(input("How much do you like to withdraw :"))
                                y[3]=y[3]-withdraw
                                print("please wait...")
                                time.sleep(1)
                                print(withdraw,"rs debited in your Account...your balance is  :",y[3])
                                time.sleep(1)
                                ce=input("Do you like to continue(C) or exit(E):")
                                if(ce=="E"):
                                    c=0
                                    break
                                else:
                                    continue
                            if(choice=="B"):
                                print("please wait...")
                                time.sleep(1)
                                print("your balance is :",y[3])
                                time.sleep(1)
                                ce=input("Do you like to continue(C) or exit(E) :")
                                if(ce=="E"):
                                    c=0
                                    break
                                else:
                                    continue
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
            else:
                print("invalid login")
                c=1
                break
            if(c==0):
                break
    elif(createAcc=='AL'):
        while True:
            ap=input("Password:")
            if(ap=='admin'):
                while True:
                    if(ap=="admin" and bool(dic)==True):
                        print("1.View all stakeholders")
                        print("2.view specific stakeholder")
                        print("3.exit")
                        checkuser=int(input("Choose option :"))
                        if(checkuser==1):
                            cnt=1
                            for i in dic.values():
                                if(cnt==1):
                                    print("Account Number :",i[0])
                                    cnt=cnt+1
                                if(cnt==2):
                                    print("Name           :",i[1])
                                    cnt=cnt+1
                                if(cnt==3):
                                    print("Password       :",i[2])
                                    cnt=cnt+1
                                if(cnt==4):
                                    print("Balance        :",i[3])
                                    cnt=1
                                print("------------------------------")
                                time.sleep(0.500)
                            ce=input("Do you like to continue(C) or exit(E):")
                            if(ce=="E"):
                                c=0
                                break
                            else:
                                continue
                    
                        elif(checkuser==2):
                            while True:
                                try:
                                    specific=int(input("Enter Account number:"))
                                    lis=list(dic[specific])
                                    cnt=1
                                    for kl in lis:
                                        if(cnt==1):
                                            print("Account Number :",kl)
                                            cnt=cnt+1
                                            continue
                                        if(cnt==2):
                                            print("Name           :",kl)
                                            cnt=cnt+1
                                            continue
                                        if(cnt==3):
                                            print("Password       :",kl)
                                            cnt=cnt+1
                                            continue
                                        if(cnt==4):
                                            print("Balance        :",kl)
                                            cnt=1
                                            break
                                    print("-----------------------------")
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
                        elif(checkuser==3):
                            u=0
                            break
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
