#Email validation in python using string function 

email = input("Enter your email: ")#A@g.in , noobmaster69@gmail.com
k,j,d=0,0,0
if len(email)>=6: #Condition 1 for email verification
    if email[0].isalpha():#Condition 2 for email verification
        if ("@"in email) and (email.count("@")==1):#Condition 3 for email verification
            if (email[-4]==".") ^ (email[-3]=="."):#Condition 4 for email verification
                for i in email:# sub - Condition  for email verification
                    if i==i.isspace():# sub - Condition 1 for email verification
                        k=1
                    elif i.isalpha():
                        if i==i.upper():#sub - Condition 2 for email verification
                            j=1
                    elif i.isdigit():#sub - Condition 3 for email verification
                        continue
                    elif i=="_" or i=="." or i=="@":#sub - Condition 4 for email verification
                        continue
                    else:#Condition 5 for email verification
                        d = 1   
                if k==1 or j==1 or d == 1:
                    print("Wrong email 5") #condition applied 5 for email verification
                else:
                    print("Right email")#Final answers
            else:
                print("Wrong email 4")#Condition applied 4 for email verification
        else:
            print("Wrong email 3")#Condition appplied 3 for email verification
    else:
        print("Wrong email 2")#Condition applied 2 for email verification
else:
    print("Wrong email 1")#Condition applied 1 for email verification


