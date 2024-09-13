class Appliance:
    def __init__(self,brand):
        self.brand=brand
    def get_info(self):
        print(f"brand {self.brand}",end="")
class KitchenAppliance(Appliance):
    def __init__(self,brand,power):
        super().__init__(brand)
        self.power = power
    def get_info(self):
        super().get_info()
        print(f" power: {self.power}",end="")
class Oven(KitchenAppliance):
    def __init__(self,brand,power,temperature_range):
        super().__init__(brand,power)
        self.temperature_range = temperature_range
    def get_info(self):
        super().get_info()
        print(f" tem range:{self.temperature_range}",end="")
class Microwave(KitchenAppliance):
    def __init__(self,brand,power,capacity):
        super().__init__(brand,power)
        self.capacity = capacity
    def get_info(self):
        super().get_info()
        print(f" capacity {self.capacity }",end="")

obj_oven = Oven("philips","12A","30degres")
obj_oven.get_info()
print()
obj_microwave = Microwave("philps","12A","80")
obj_microwave.get_info()