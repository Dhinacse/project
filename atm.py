import random,time,sys
def delete(acc):
    del database[acc]
    return 1
try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")
database={}
passdb={}
c=0
u=0
color.write("WELCOME TO OUR H&D E-BANK".center(70,"-"),"COMMENT")
print()
time.sleep(1)
print()
print("by Hari Balaji et Dhina".center(86,"-"))
time.sleep(1)
print()
while True:     #HariBalaji module
    SelectUser=input("Create Account(CA)/Admin Login(AL)/User Login(L) :").upper()
    if(SelectUser=="CA"):
        while True:
            import time
            color.write("please wait your account number is generating \n","KEYWORD")
            time.sleep(2)
            l=[]
            op=[]
            x=random.randint(1000,2000)
            print("Your Account number is:",x)
            name=input("Your Name :")
            pas=input("Your Password :")
            while True:
                try:
                    bal=int(input("please deposit 5000Rs to activate your Account:"))
                    if(bal>=5000):
                        
                        color.write("Creating your account...please wait.....\n","KEYWORD")
                        time.sleep(2)
                        color.write("Your account created successfully@H&D E-bank \n","STRING")
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
                        import datetime
                        xdatetime=datetime.datetime.now()
                        date=xdatetime.strftime("%d %B %y")
                        time=xdatetime.strftime("%I:%M:%S %p")
                        op.append(x)
                        op.append("deposit  ")
                        op.append(bal)
                        op.append(bal)
                        op.append(date)
                        op.append(time)
                        passdb[x]=op
                        c=1
                        break
                    else:
                        color.write("Deposit should be more than 5000...\n","COMMENT")
                        time.sleep(2)
                    if(c==1):
                        break
                except ValueError:
                    color.write("Deposit Should be numerical....\n","COMMENT")
                if(c==1):
                    break
            if(c==1):
                break
    elif(SelectUser=="L"):      #dhina module
        while True:
            import time
            try:
                acc=int(input("Enter your Account number:"))
                p=passdb[acc]
                while True and bool(database)==True:
                    try:
                        username=input("Enter your username :")
                        passw=input("Enter your password :")
                        while True:
                            y=database[acc]
                            import time
                            if(y[1]==username and y[2]==passw):
                                choice=input("Enter your choice(Deposit(D),Withdraw(W),Balance(B),Passbook(P) ,DeleteAccount(DA):").upper()       
                                if(choice=="D"):
                                    try:
                                        deposit=int(input("How much do you like to deposit :"))
                                        y[3]=y[3]+deposit
                                        print("please wait...")
                                        time.sleep(1)
                                        print(deposit,"rs credited in your Account...your balance is  :",y[3])
                                        time.sleep(1)
                                        import datetime
                                        xdatetime=datetime.datetime.now()
                                        date=xdatetime.strftime("%d %B %y")
                                        time=xdatetime.strftime("%I:%M:%S %p")
                                        p.append("deposit  ")
                                        p.append(deposit)
                                        p.append(y[3])
                                        p.append(date)
                                        p.append(time)
                                        passdb[acc]=p
                                        ce=input("Do you like to continue(C) or exit(E):").upper()
                                        
                                        if(ce=="E"):
                                            c=0
                                            break
                                        else:
                                            continue
                                    except ValueError:
                                        color.write("Deposit Should be numerical.....\n","COMMENT")
                                    if(c==0):
                                        break
                                if(choice=="W"):
                                    import time
                                    try:
                                        withdraw=int(input("How much do you like to withdraw :"))
                                        y[3]=y[3]-withdraw
                                        print("please wait...")
                                        time.sleep(1)
                                        if(y[3]>=5000):
                                            print(withdraw,"rs debited in your Account...your balance is  :",y[3])
                                            time.sleep(1)
                                            import datetime
                                            xdatetime=datetime.datetime.now()
                                            date=xdatetime.strftime("%d %B %y")
                                            time=xdatetime.strftime("%I:%M:%S %p")
                                            p.append("withdraw")
                                            p.append(withdraw)
                                            p.append(y[3])
                                            p.append(date)
                                            p.append(time)
                                            passdb[acc]=p
                                            ce=input("Do you like to continue(C) or exit(E):").upper()
                                            if(ce=="E"):
                                                c=0
                                                break
                                            else:
                                                continue
                                        else:
                                            color.write("Minimum balance should be atleast 5000rs.....\n","COMMENT")
                                            print("Please try again....")
                                            y[3]=y[3]+withdraw
                                            continue
                                        
                                    except ValueError:
                                        color.write("Deposit Should be numerical....\n","COMMENT")
                                    if(c==0):
                                        break
                                if(choice=="B"):
                                    print("Please wait...")
                                    time.sleep(1)
                                    print("Your balance is :",y[3])
                                    time.sleep(1)
                                    ce=input("Do you like to continue(C) or exit(E) :").upper()
                                    if(ce=="E"):
                                        c=0
                                        break
                                    else:
                                        continue
                                if(choice=="P"):
                                    print("Please wait...")
                                    ui=passdb[acc]
                                    co=0
                                    color.write("No\tTransaction\tC_or_D\t\tBalance\t          Date\t     Time\n","COMMENT")
                                    for i in range(1,len(ui),5):
                                        co=co+1
                                        print(co,"\t",ui[i],"\t",ui[i+1],"\t\t",ui[i+2],"\t",ui[i+3],"\t",ui[i+4])
                                if(choice=="DA"):
                                    time.sleep(1)
                                    print("please wait...")
                                    time.sleep(1)
                                    delete(acc)
                                    color.write("Your account has deleted........\n","COMMENT")
                                    c=0
                                    break
                                if(c==0):
                                    break
                            else:
                                color.write("Invalid login....try again....\n","COMMENT")
                                c=1
                                break
                    
                            if(c==0):
                                break
                        if(c==0):
                            break
                    except KeyError:
                        color.write("Invalid account number....\n","COMMENT")
                        c=1
                    if(c==0 or c==1):
                        break
                else:
                    color.write("Invalid login....\n","COMMENT")
                    c=1
                    break
                if(c==0):
                    break
            except ValueError:
                color.write("Enter valid Account number...\n","COMMENT")
            except KeyError:
                color.write("Enter valid Account number...\n","COMMENT")
    elif(SelectUser=='AL'):         #HariBalaji module
        import time
        while True:
            ap=input("Password:")
            if(ap=='admin'):
                while True:
                    if(ap=="admin" and bool(database)==True):
                        print("1.View all stakeholders")
                        print("2.view specific stakeholder")
                        print("3.delete specific stakeholder")
                        print("4.exit")
                        checkuser=input("Choose option :")
                        if(checkuser=='1'):
                            cnt=1
                            for i in database.values():
                                if(cnt==1):
                                    print("Account Number      :",i[0])
                                    cnt=cnt+1
                                if(cnt==2):
                                    print("Name                       :",i[1])
                                    cnt=cnt+1
                                if(cnt==3):
                                    print("Password                 :",i[2])
                                    cnt=cnt+1
                                if(cnt==4):
                                    print("Balance                   :",i[3])
                                    cnt=cnt+1
                                if(cnt==5):
                                    print("Creation of Account :",i[4],i[5])                        
                                    cnt=1
                                    break
                                color.write("-------------------------------------------------\n","KEYWORD")
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
                                            print("Account Number       :",kl)
                                            cnt=cnt+1
                                            continue
                                        if(cnt==2):
                                            print("Name                       :",kl)
                                            cnt=cnt+1
                                            continue
                                        if(cnt==3):
                                            print("Password                 :",kl)
                                            cnt=cnt+1
                                            continue
                                        if(cnt==4):
                                            print("Balance                   :",kl)
                                            cnt=cnt+1
                                            continue
                                        if(cnt==5):
                                            print("Creation of Account :",i[4],i[5])
                                            cnt=1
                                            break
                                    color.write("-------------------------------------------------\n","KEYWORD")
                                    time.sleep(1)
                                    ce=input("Do you like to continue(C) or exit(E):").upper()
                                    if(ce=="E"):
                                        c=0
                                        break
                                    elif(ce=='C'):
                                        c=1
                                        break
                                except KeyError:
                                    color.write("invalid account number....\n","COMMENT")
                                    c=1
                                except ValueError:
                                    color.write("invalid account number....\n","COMMENT")
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
                            delspecific=int(input("Enter Account Number to remove account from H&D E-bank :"))
                            delete(delspecific)
                            time.sleep(1)
                            print("please wait...")
                            time.sleep(1)
                            color.write("Account has deleted........\n","COMMENT")
                            c=0
                            break
                        elif(checkuser=='4'):
                            u=0
                            break
                        else:
                            color.write("Please choose the given field...\n","COMMENT")
                    if(c==1):
                        continue
                    else:
                        color.write("no stakeholder currently....redirect to home....\n","COMMENT")
                        time.sleep(2)
                    if(u==0):
                        break
                if(u==0):
                    break
            else:
                color.write("Invalid password....\n","COMMENT")
                continue
                    
    else:
        color.write("Please choose the given criteria....\n","COMMENT")
