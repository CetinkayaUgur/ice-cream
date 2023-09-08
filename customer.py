class Customer:
    def __init__(self, name, surname, adress, purchased_amount, dept_amount = 0):        
        self.__name = name
        self.__surname = surname
        self.__adress = adress
        self.purchased_amount = purchased_amount
        self.__dept_amount = dept_amount

    # def get_name(self):
    #     return self.__name
    
    # def get_surname(self):
    #     return self.__surname
    
    # def get_adress(self):
    #     return self.__adress
    
    def get_purchased_amount(self):
        return self.__purchased_amount
    
    def get_dept_amount(self):
        return self.__dept_amount

    # def set_name(self, name):
    #     self.__name = name

    # def set_surname(self, surname):
    #     self.__surname = surname

    # def set_adress(self, adress):
    #     self.__adress = adress

    def set_purchased_amount(self, purchased_amount):
        if purchased_amount > 0:
            self.__purchased_amount = purchased_amount

    def set_dept_amount(self, dept_amount):
        if dept_amount > 0:
            self.__dept_amount = dept_amount

    def delete(self):
        print(f"{self.name} isimli müşteri başarıyla silindi...")
        del self