class User:
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password=password
    def display_info(self):
        print("Name:",self.name)
        print("Email:",self.email)
        print("Password:",self.password)
database=[]
def registration():
       
          print("NAME:")
          name=input()
          print("EMAIL:")
          email=input()
          for data in database:
             if data.email==email:
                  print("email already exist")
                  return # exist from the function
        
          print("PASSWORD:") 
          password=input()
        
          
          print("Registration successfull")
          u=User(name,email,password)
          database.append(u)
          
          u.display_info()


        
          
         

while(True):
     print("do u want to register yes/no")
     a=input()
     if(a=="yes" or "YES"):
          registration()
     elif(a=="no" or "NO"):
          exit()

 
 
