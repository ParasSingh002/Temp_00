user="Name@123"
uname=input("enter ur username : ")
a=0
b=0
c=0
d=0
count=0
if user==uname:
  pwd=input("enter ur password : ")
  if len(pwd)>=8:
    for i in pwd:
      if i==" ":
        count+=1
    for i in pwd:
      if count==0:
        if i.isupper()==True:
          a+=1
        elif i.islower()==True:
            b+=1
        elif i.isdigit()==True:
          c+=1
        else:
          d+=1
    if a>0 and b>0 and c>0 and d>0:
      print("plogin successfu!!l")
      balance=10000
      while True:
        print("*"*10)
        print("1. withdraw")
        print("2. deposit")
        print("3. balance")
        print("4. exit")
        print("*"*10)
        n=int(input("enter your choice : "))
        if n==1:
          withdraw=int(input("enter amount u want to withdraw : "))
          if withdraw<=balance:
            balance=balance-withdraw
          else:
            print("insufficient balance")
        if n==2:
          deposit=int(input("enter amount u want to deposit : "))
          balance=balance+deposit
        if n==3:
          print(f"your current balance : {balance}")
        if n==4:
          print("u exited")
          break
        else:
          print("invalid choice!!")
    else:
      print("signup failed!!")
  else:
    print("short password!!")
else:
  print("invalid username!!")
