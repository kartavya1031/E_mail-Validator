email=input("Enter your Email address :")
j=k=l=0


if len(email)>6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if((email[-4] == ".") ^ (email[-3]==".")):
                for i in email:
                    if i==i.isspace():
                        j=1
                    elif i.isalpha():
                        if i==i.isupper():
                            k=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="@" or i==".":
                        continue
                    else:
                        l==1
                if j==1 or k==1 or l==1:
                    print ("Wrong Email 5")
                else:
                    print("The Email is correct")
            else:
                print("Wront email 4")
        else:
            print("Wrong Email 3")
    else:
        print("Wrong Email 2")
else:
    print("Wrong Email 1")