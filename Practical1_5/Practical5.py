# Continue to the previous ErrorHandling practical. Every error that is raised should have a proper log in a separate log
# When the error is raised, that error should be logged in the error.log file with each exception's details that will help
#  to debug the issue. I.e: InvalidNameException: Valid name should be length of 3-8 chars, input value ab.
# Success logs should be added in success.log file to manage the track of user activity. I.e: Name john is validated.


import logging
formatter = logging.Formatter('%(message)s')


def setup_logger(name, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# first file logger
logger1 = setup_logger('first_logger', 'error.log')


# second file logger
logger2 = setup_logger('second_logger', 'success.log')






class InvalidNameException(Exception):
    def __init__(self, name, msg="Name must be between 3 and 8 Characters"):
        self.name = name
        self.msg = msg
        logger1.error('InvalidNameException: Valid name should be length of 3-8 chars, input name {}'.format(self.name)) 
        
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.name} -> {self.msg}'        


class MustBe18YearOldException(Exception):
    def __init__(self, age, msg="Age must be between 0 and 120"):
        self.age = age
        self.msg = msg
        logger1.error('MustBe18YearOldException: Valid Age must be between 0 and 120, input age {}'.format(self.age))
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.age} -> {self.msg}'

class BothError(Exception):
    def __init__(self, age,name, msg="Age must be between 0 and 120",msg1="Name must be between 3 and 8 Characters"):
        self.age = age
        self.name=name
        self.msg = msg
        self.msg1=msg1
       
        logger1.error('InvalidNameException: Valid name should be length of 3-8 chars, input name {}'.format(self.name)) 
        logger1.error('MustBe18YearOldException: Valid Age must be between 0 and 120, input age {}'.format(self.age))
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
            logger2.info('Name {} is Validated'.format(name))     
    
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


    
    
