from customer import Customer
from employee import Employee
from ice_cream import IceCream
class Transaction:
    def __init__(self, type): #card, cash ve dept adında 3 tane nesne oluşturacağım
        self.__type = type
        
    def sell_ice_cream(self, customer_name, purchase_amount, employee_name, flavor, cone_or_bowl):
        if self.type == "dept":
            self.customer_instance = Customer()
            self.employee_instance = Employee()
            self.ice_cream_instance = IceCream()
            customer_name.purchased_amount += purchase_amount
            employee_name.sales_quantity += purchase_amount
            flavor

            #...
    
