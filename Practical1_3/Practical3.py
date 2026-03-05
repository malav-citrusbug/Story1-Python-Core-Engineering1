# T1.3
# Create a Python script that will do the read/write operation on a given JSON file.
# There will be 2 files for the data store user1 and user2.
# Create a function that will do read/write operations on each file conditionally, without changing the caller logic.
#  ( Caller logic means by the main function that is created )
# The caller function should not be able to know in which file it is doing the operation.
# The read/write function should be private to the main operational class.


# Read from file and parse JSON
import json


class WR():
    def __init__(self):
        self.__files={"User1":"user1.json","User2":"user2.json"}


    def __Writer1(self,file_name,file_data):
       
       json_str = json.dumps(file_data, indent=4)
       with open(str(file_name), "w") as f:

        f.write(json_str)
       
        
       

    def __Reader1(self,file_name):
        with open(str(file_name),"r") as f:
            data=json.load(f)
            
        print(data)       
         

    

    def get_user_details(self,user_name):
        file_name=self.__files.get(user_name)
        if file_name==None:
            print("User Not Found")
        else:
            self.__Reader1(str(file_name))

        

    def update_user_details(self,user_name,data):
        file_name=self.__files.get(user_name)
        if file_name==None:
            print("User Not Found, You Can't Write Data")
        else:
             self.__Writer1(str(file_name),data)  

         

         
           


my_world=WR()

file_change="Start"
while(file_change):
    
    file_change=str(input("Enter \n1.r For Read \n2.w For Write \n3.e For Exit \n--> "))
    
    if file_change=="e":
        exit()
    else:
        user_name=str(input("Enter User name --> "))    
    
    if file_change=="w":
        file_data=str(input("Enter Data You Want to Write --> "))
        my_world.update_user_details(user_name,file_data)
        
    elif file_change=="r":
        file_data=""
        my_world.get_user_details(user_name)
        
    
               
    
        





 