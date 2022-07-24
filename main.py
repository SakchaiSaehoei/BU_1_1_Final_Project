def register ():
 user, password = '0', '0'
 cf=open("uandp.txt",'a')
 cf.close()
 import os
 if os.stat("uandp.txt").st_size == 0 :
     #print("this is for in case the file is emthy ")
     while user and password == '0' and '0':
         with open('uandp.txt', 'r+') as f:
             print('=' * 40)
             print("Welcome to register page")
             print('='*40)
             user = input("Enter user name:")
             password = input("Enter password:")
             compass = input("Enter password again:")
             print('=' * 40)
             if password == compass:
                 new_data = user + " " + password
                 f.write(new_data+'\n')
                 print("welcome %s to Yong Money \n You have successfully registered" % user)
                 print('=' * 40)
             else:
                 print("the passwords are not match!!")
                 user, password = '0', '0'
                 print('=' * 40)
                 break
 else:
  #print("thsi is for test if the user name is already exit")
  while user and password =='0'and'0' :
   with open('uandp.txt','r+') as f:
    data=f.read().splitlines()
    print('=' * 40)
    print("Welcome to register page")
    print('=' * 40)
    user=input("enter user name:")#need to check if the user is alreay exit in the or system
    for line in data:
     info=line.split()
     #print(line)
     #print(info[0])
     if user==info[0]: #for check if it is exit
       print("This user name is already used !!!")
       print('please try other user name.')
       user, password = '0', '0'
       print('=' * 40)
       break
     password=input("enter password:")
     compass=input("enter password again:")
     print('=' * 40)
     if password==compass:
        new_data=user+" "+password
        f.write(new_data+'\n')
        print("welcome %s to Yong Money \n You have successfully registered"%user)
        print('=' * 40)
        break
     else:
         print("The passwords are not match \n Please try agian!")
         user,password ='0','0'
         break
def login():
 print('Welcome to login page')
 #=input("To login type :1 \n Don't have account? \n to register type :2\n Enter your Choice:")
 #if choice=='1':
 user, password = '0', '0'
 while user and password == '0' and '0':  # if want to log out command to change user and password to '0'
    with open('uandp.txt', 'r') as f:
     code=""
     data = f.read().splitlines()
     print('=' * 40)
     user = input("Enter User name:")
     password = input("Enter Password:")
     x = user + " " + password
     if x in data:  # to check if the user and password match the file
       print("Successfully log in ")
       print('=' * 40)
       code = user[1] + user[0] + str(len(user))
       c="E"
       with open("login.txt", 'w') as f:
           to_login = 'yes' + ' ' + code
           f.write(to_login)
     else:
       user, password = '0', '0'
       print('=' * 40)
       print('Wrong user name or password try again')
       print('=' * 40)
       b=input("Back to Log in register page? :Y,N")
       if b.upper() =="Y":
              break
 return user,password,code,c
def income (code):
  name=input("Enter name of income:")
  in_amount=int(input("Enter income amount:"))
  to_balance=in_amount
  date=input("Enter date dd/mm/yyyy")
  y=date.split('/')
  file_code=y[2]+y[1]+code+'.txt'
  with open (file_code,'a')as file: #or "%s"%openfile,'r+'
   file.write( '%-15s %-15s %-5d in\n'%(date,name,in_amount))
  import os
  while os.stat('%sbalance.txt' % code).st_size == 0:
      with open('%sbalance.txt' % code, 'w') as f:
          f.write('0')
  if os.stat('%sbalance.txt' % code).st_size > 0:
      with open('%sbalance.txt' % code, 'r') as f:
          r = f.read()
          # print(r)
          balance = int(r) + (to_balance)
      with open('%sbalance.txt' % code, 'w') as f2:
          b_write = (str(balance))
          f2.write(b_write)
      print("Income is saved")
def expenses (code):
 #code='ey4'
 name=input("Enter name of expense:")
 out_amount=int(input("Enter expense amount:"))
 to_balance=-(out_amount)
 date=input("Enter date dd/mm/yyyy")
 y=date.split('/')
 file_code=y[2]+y[1]+code+'.txt'
 with open (file_code,'a')as file: #or "%s"%openfile,'r+'
  file.write( '%-15s %-15s %-5d out \n'%(date,name,to_balance))
 import os
 while os.stat('%sbalance.txt'%code).st_size == 0:
     with open('%sbalance.txt'%code, 'w') as f:
         f.write('0')
 if os.stat('%sbalance.txt' % code).st_size >0 :
   with open  ('%sbalance.txt'%code,'r') as f:
       r=f.read()
       balance=int(r)+(to_balance)
   with open  ('%sbalance.txt'%code,'w') as f2:
    b_write=(str(balance))
    f2.write(b_write)
   print("expense is saved")
def login_register():
 print('Welcome to young Money')
 print(("Login:1 \n Register:2 \n Exit= :E"))
 c=input("Enter choice")
 while c !='E':
  if c=='2':
   register()
   print(("Login:1 \n Register:2 \n Exit= :E"))
   c = input("Enter choice")
  elif c=='1':
   user, password, code,c = login()
   print(("Login:1 \n Register:2 \n Go to home= :E"))
   c = input("Enter choice")
  else:
      print("Invalid choice Please Try again!!")
      print(("Login:1 \n Register:2 \n Exit= :E"))
      c = input("Enter choice")
 #print(code)
 return user,password,code
def log_out():
 with open("login.txt",'w') as f:
    data='no'+' '+'none'
    f.write(data)
    print("you are now logout")
    print('=' * 40)
def check_login():
 with open("login.txt",'r') as f:
   datafile = f.read() #it will contian condtion of login and  user file code
   data='no'+' '+'none'
   while  datafile == data :
     #("yes")#not login yet
     user,password,code=login_register()
     datafile = f.read()
     if   datafile != data:
         break
def report (code):
    total_income =0
    total_expenses = 0
    year=input("Enter Year:")
    month=input("Enter Month:")
    #report=year+month+code
    with open("%s%s%s.txt"%(year,month,code),'r') as f:
        data=f.read().splitlines()
        for x in data:
            x2=x.split()
            y=int(x2[-2])
            if y>0:
                total_income+=y
            elif y<0:
                total_expenses+=y
        total_expenses=-(total_expenses)
        print("See month %s year %s summary:1"%(month,year))
        print("See month %s year %s detial:2"%(month,year))
        act=input("Enter 1 or 2 :")
        if act=="1":
         print("Summary of month %s year %s  "%(month,year))
         print("Total income =%.2f"%total_income)
         print("Total expense =%.2f"%total_expenses)
        elif act=="2":
         print('%-15s %-15s %-5s ' % ('date', 'name', 'amount'))
         for x in data:
          print(x)
def mine_code():
    f_s = open("login.txt", 'r')
    s = f_s.read().split()
    #print(s[1])
    code = s[1]
    return code
def balance (code):
   with open  ('%sbalance.txt'%code,'r+') as f2:
    print("Your balance is",f2.read())
    b_write=(str(balance))
    f2.write(b_write)
def menu ():
    print('='*40)
    print('=' * 40)
    print("Welcome to Young money")
    print('=' * 40)
    print("Add income : 1 \n Add expences:2 \n Check balance:3 \n See report :4 \n Exit:5 \nLogout :6")
    print('=' * 40)
def full_funtion():
    file=open("uandp.txt",'a')
    l_file=open("login.txt", 'a')
    import os
    if os.stat("login.txt").st_size == 0:
      l_file.write('no'+' '+'none')

    file.close()
    l_file.close()
    check_login()
    #login_register()
    code = mine_code()
    cf = open('%sbalance.txt' % code, 'a')
    import os
    if os.stat('%sbalance.txt' % code).st_size == 0:
        cf.write('0')
    cf.close()
    menu()
    act=input("Enter 1 -6:")
    while act!='5':#3check balane #4 see report
     if act == '1':
        income(code)
        menu()
        act = input("Enter 1 -6:")
     elif act =='2':
        expenses(code)
        menu()
        act = input("Enter 1 -6:")
     elif act=='3':
         balance (code)
         menu()
         act = input("Enter 1 -6:")
     elif act =='4':
         report(code)
         menu()
         act = input("Enter 1 -6:")
     elif act=='5':
      print('Exited \n Bye Bye')
      break
     elif act=='6':
        log_out()
        print("You are log out \nSee you soon")
        act == '5'
        break



full_funtion()


#total_in=open("total_in.txt","w")
#total_out=
#balance=[0]#always update  assum if write in file will be better
#total_income=[0]
#total_expenses=[0]
#code=['ey4']#need to creat demand change when login
#balance[0]=balance[0]
#in_amount,to_balance=income (code[0],total_income[0]) #call for the fuction
#balance[0]=balance[0]+to_balance
#print(balance)
#out_amount,to_balance=expenses (code[0],total_expenses[0])#call for the fuction
#total_income[0]=total_income[0]+in_amount
#total_expenses[0]=total_expenses[0]+out_amount
#balance[0]=balance[0]+to_balance

#print(total_income)
#print(total_expenses)
#print(balance)
#with open('login.txt','w')as f :
  #f.write('')