import csv

class Item(object):
    payment = 0.8
    all = [] #To store all the instances in an array
    def __init__(self, name : str, price : float, quantity = 1):
        # print("I am created")
        # print(f"Instances from {name}")
        # print(f"Instances from {price}")
        # print(f"Instances from {quantity}")
        
        #Condition
        assert price >= 0, f"Price {price} shouldn't be zero"
        assert quantity > 0, f"Quantity {quantity} shouldn't be zero"

        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self) #To Append instances 
        
    def calc_tl_price(self):
        return f" {self.name} costs {self.price * self.quantity} for {self.quantity} nos" 

    def apply_discount(self):
        self.price = self.price * self.payment
    def __repr__(self):           #Change the name of the object (original name)
        return f"{self.__class__.__name__}('{self.name}')"
    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name = item["name"],
                price = float(item["price"]),
                quantity = float(item["quantity"])
            )

#Class Attribute Invoking test
# print(Item.payment)



#List all the attributes of Class
# print(Item.__dict__)
# 

#Instances
item1 = Item("Phone", 5000, 10)
item2 = Item("Laptop", 15000, 10)
item3 = Item("Cable", 100, 5)
item4 = Item("Mouse", 500, 5)
item5 = Item("Keyboard", 2500, 5)

Item.instantiate_from_csv()
print(Item.all)
# print(Item.all) # Print all the instances


# dict1 = {"name" : "Aarjav", "Age" : 12}

# print(dict1.get("name"))
# print(dict1["name"])

# for i in Item.all :
#     print(i.name, i.quantity, i.price)  #Showing all instance variables 

#Invoking
# item1.apply_discount()
# print(item1.calc_tl_price())


# item2.payment = 0.6
# item2.apply_discount()
# print(item2.calc_tl_price())





# item1 = Item("Laptop")
# item1.name = "Phone"
# item1.price = 500
# item1.quantity = 5
# print(item1.calc_tl_price(item1.price, item1.quantity))
