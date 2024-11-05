class Product:
    """
    this class is used to create a code
    for online shopping
    """
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def product_display(self):
        """
        Displays the details of the product.
        """
        print("the product name is :", self.name)
        print("then product price is :",self.price)
        print("the product quantity is :",self.quantity)

class ElectronicProduct(Product):
    """ 
    this class is used to create
    elctronic product objects
    """
    def __init__(self, name, price, quantity, model, brand):
        super().__init__(name, price, quantity)
        self.brand = brand
        self.model = model
    def product_display(self):
        """
        Displays the details of the electronic product.
        """
        super().product_display()
        print("the brand name is :",self.brand)
        print("the model name is  :",self.model)
        
    def total_price(self):
        """
        Calculates and returns the total price of the electronic product.
        """
        return self.price * self.quantity
    
    def __add__(self,other):
        """
        Calculates and returns the total price of the electronic product.
        """
        return Product(self.name + other.name, self.total_price + other.total_price, self.quantity + other.quantity)

class ClothingProduct(Product):
    """ 
    this class is used to create
    clothing product objects
    """
    def __init__(self, name, colour, size, price, quantity):
        super().__init__(name, price, quantity)
        self.colour = colour
        self.size = size
    def product_display(self):
        """
        Displays the details of the clothing product.
        """
        super().product_display()
        print("the product size is :",self.size)
        print("the product colour is :",self.colour)
        
    def total_price(self):
        """
        Calculates and returns the total price of the clothing product.
        """
        return self.price * self.quantity
        
    def __add__(self,other):
        """
        Adds two ClothingProduct objects and returns a new Product object.
        """
        return Product(self.name + other.name, self.total_price + other.total_price, self.quantity + other.quantity)


if '__main__' == __name__:
    #storing product informations
    electronic_products = {"stove" : [2000, 10, "xpress", "preethi"], "fan" : [2750, 8, "cool", "anchor"], "ac" : [10000, 15, "polar", "vovlvo"],
                           "washing machine" : [7000, 20, "super", "samsung"]}
    clothing_products = {"shirt" : ["pink", 40, 500, 10], "tshirt" : ["orange", 40, 1000, 15], "pant" : ["black", 32, 1500, 20],
                         "jean" : ["blue", 30, 2000, 10]}
    product_list ={}
    #creating products
    for i , j in electronic_products.items():
        prod = ElectronicProduct(i, *j)
        product_list[i] = prod 
    for i , j in clothing_products.items():
        prod = ClothingProduct(i, *j)
        product_list[i] = prod
        
    while True:
        ans = input("enter product name to continue shopping or type 'end' to stop shopping : ")
        if ans not in product_list:
            print("product not available")
            break
        if ans == 'end':
            print("thank you for shopping")
            break
        else:
            prod_details = product_list[ans]
            quan = int(input("enter product quantity : "))
            if quan > prod_details.quantity:
                print("product out of stock")
                quan = int(input(f"enter product quantity less than {prod_details.quantity} : "))
                
            total_price = prod_details.price * quan
            print(f"the total price of {ans} is {total_price}")
                