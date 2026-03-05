# T1.2: Create an in-memory user store in which CRUD operations are performed via the User ID.
# Each item should include: Email, Username, ID
d={}
n=int(input("Enter Options No \n1.For Create \n2.For Read \n3.For Update \n4.For Delete \n5.For Exit \n--> "))
while(n):
    if n==1:
        user_id=int(input("Enter User ID --> "))
        email_id=str(input("Enter Email ID -->"))
        username=str(input("Enter Username -->"))
        d[user_id]=[email_id,username]
        print("User Created SuccessFully\n")
        n=int(input("Enter Options No \n1.For Create \n2.For Read \n3.For Update \n4.For Delete \n5.For Exit \n-->"))
    elif(n==2):
        user_id=int(input("Enter User ID --> "))
        print()
        if(user_id in list(d.keys())):
            print("User Details Are As Follow\n")
            print("User ID --> ",user_id)
            print("Email ID --> ",d[user_id][0])
            print("Username --> ",d[user_id][1],"\n")
            print("User Details Found SuccessFully\n")
            n=int(input("Enter Options No \n1.For Create \n2.For Read \n3.For Update \n4.For Delete \n5.For Exit \n-->"))
        else:
            print("User Not Found !!\n")
            n=int(input("Enter Options No \n1.For Create \n2.For Read \n3.For Update \n4.For Delete \n5.For Exit \n-->"))
    elif(n==3):
        user_id=int(input("Enter User ID --> "))
        print()
        if(user_id in list(d.keys())):
            a=int(input("What You Want To Update \n1.For Email ID \n2.For Username \n3.For Both\n--> "))
            print()
            if(a==1):
                email_id_updated=str(input("Enter Updated Email ID --> "))
                d[user_id][0]=email_id_updated
                n=int(input("Enter Options No \n1.For Create \n2.For Read \n3.For Update \n4.For Delete \n5.For Exit \n-->"))
            elif(a==2):
                username_updated=str(input("Enter Updated Username --> "))
                d[user_id][1]=username_updated
                n=int(input("Enter Options No \n1.For Create \n2.For Read \n3.For Update \n4.For Delete \n5.For Exit \n-->"))
            elif(a==3):
                email_id_updated=str(input("Enter Updated Email ID --> "))
                print()
                username_updated=str(input("Enter Updated Username --> "))
                d[user_id][1]=username_updated
                d[user_id][0]=email_id_updated
                n=int(input("Enter Options No \n1.For Create \n2.For Read \n3.For Update \n4.For Delete \n5.For Exit \n-->"))
            else:
                print("Select Valid Input\n")    
    elif(n==4):
        user_id_del=int(input("Enter User ID You Want To Delete --> "))
        del d[user_id_del]
        print("User Deleted Successfully\n")
        n=int(input("Enter Options No \n1.For Create \n2.For Read \n3.For Update \n4.For Delete \n5.For Exit \n-->"))
    elif(n==5):
        
        print("Thanks For Visiting")
        exit()
    else:
        print("Please Select Valid Input\n")
        n=int(input("Enter Options No \n1.For Create \n2.For Read \n3.For Update \n4.For Delete \n5.For Exit \n-->"))        





            


            
