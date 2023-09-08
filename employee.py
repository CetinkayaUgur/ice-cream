from datetime import datetime

class Employee:
    def __init__(self, name, surname, age, phone_number, adress, email, salary = 15000):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.adress = adress
        self.email = email
        self.__salary = salary
        self.__uptime = datetime.now()
        self.__sales_quantity = 0
    
    def get_full_name(self):
        return f"Çalışanın adı: {self.__name}, çalışanın soyadı: {self.__surname}"

    def get_salary(self):
        return self.__salary

    def get_sales_quantity(self):
        return self.__sales_quantity
    
    def get_uptime(self): #kişinin ne zamandan beri bizimle çalıştığını hesaplayan metot
        return datetime.now() - self.__uptime

    def update(self, name, surname, phone_number, adress, email, salary):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.adress = adress
        self.email = email

    def set_salary(self, new_salary):
        self.__salary = new_salary
    
    def set_sales_quantity(self, sale_quantity):
        self.__sales_quantity = sale_quantity
    