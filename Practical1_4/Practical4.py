# Practical Assignment
# Validate user input before saving data to the in-memory user store.
# Validate name: Name must be between  3 and 8 chars. Error should raise InvalidNameException
# Validate Age: Age should be more than 18 years. Error should raise MustBe18YearOldException
# On each error console should log the appropriate message without any error
# Step 1: Define a custom exception class
class InvalidNameException(Exception):
    def __init__(self, name, msg="Name must be between 3 and 8 Characters"):
        self.name = name
        self.msg = msg
        
        
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.name} -> {self.msg}'        


class MustBe18YearOldException(Exception):
    def __init__(self, age, msg="Age must be between 0 and 120"):
        self.age = age
        self.msg = msg
        
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.age} -> {self.msg}'

class BothError(Exception):
    def __init__(self, age,name, msg="Age must be between 0 and 120",msg1="Name must be between 3 and 8 Characters"):
        self.age = age
        self.name=name
        self.msg = msg
        self.msg1=msg1
       
        
        super().__init__(self.msg,self.msg1)

    def __str__(self):
        return f'{self.age} -> {self.msg}\n{self.name} -> {self.msg1}'
        



# Step 2: Use the custom exception in your code
def set_age_name(age,name):
    if (age <= 18) and (len(name)>=3 and len(name)<=8):
        raise  MustBe18YearOldException(age) 
        
   
           
    elif (len(name)<3 or len(name)>8) and (age>18):
        raise InvalidNameException(name)
    elif (age <= 18) and (len(name)<3 or len(name)>8):
        raise BothError(age,name) 
        
    else:
        if name in list(a.keys()):
            print("Name Already Exists")
        else:
            print()
            print(f"Name set to: {name}") 
            print(f"Age set to: {age}") 
            print()
            a[name]=age
            print(a)
               
    
a={}
n=0
# Step 3: Handling the custom exception
while(n!=1):
    if n==0:
        try:
            age1=int(input("Enter Age --> "))
            name1=str(input("Enter Name --> "))
            set_age_name(age1,name1)  # This will raise the custom exception
        except InvalidNameException as e:
            print(e)
        except MustBe18YearOldException as ve:
            print(ve)
        except BothError as v1:
            print(v1)
            

                
        n=int(input("Enter 0 To Continue And 1 To Exit --> "))    
    
    else:
        print("Please Enter Valid Input")
        n=int(input("Enter 0 To Continue And 1 To Exit --> "))    

