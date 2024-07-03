class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def display_info(self):
        print("Product name:",self.name)
        print("product price",self.price)
        print("product quantity",self.quantity)
database=[]
def reg():
    print("enter the name of the product")
    name=input()
    print("enter the price of the product")
    price=input()
    print("enter the quantity of the product ")
    quantity=input()
    print("Registered successfully")
    u=Product(name,price,quantity)
    u.display_info()
    database.append(u)

while(True):
    print("Do u want to register yes or no")
    a=input()
    if(a=="yes" or a=="YES"):
        reg()
    elif(a=="no" or a== "NO"):
        exit()


