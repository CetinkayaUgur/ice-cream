class IceCream:
    def __init__(self, name, flavor, stock_amount): #direkt flavor adı ile nesne oluştur
        self.name = name
        self.flavor = flavor
        self.__stock_amount = stock_amount 

    # def get_name(self):
    #     return self.__name
    
    # def get_flavor(self):
    #     return self.__flavor
    
    def get_stock_amount(self):
        return self.__stock_amount
    
    # def set_name(self, new_name):
    #     self.__name = new_name
    
    # def set_flavor(self, new_flavor):
    #     self.__flavor = new_flavor
    
    def set_stock_amount(self, new_stock_amount):
        if new_stock_amount > 0:
            self.__stock_amount = new_stock_amount
    