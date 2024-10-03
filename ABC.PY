from abc import ABC,abstractmethod

class Robot(ABC):
    def __init__(self,name,model,power_level=100):
        self.name = name
        self.model = model
        self.power_level = power_level

    def show_info(self):
        print(f"name = {self.name},model = {self.model},power lvl = {self.power_level}")

    @abstractmethod
    def perform_task(self):
        pass

    def charge(self,charge):
        self.power_level = min(100,self.power_level+charge)
        print(f"charged power = {self.power_level}")



class WorkerRobot(Robot):
    def __init__(self,name,model,tool):
        super().__init__(name,model)
        self.tool = tool

    def perform_task(self):
        if self.power_level>=10:
           self.power_level-=10
           print(f"task 1 completed {self.name}, {self.model},{self.tool},{self.power_level}")
        else:
            print(f"robot need more power")

    def save_file(self, file):
        with open(file, 'w') as file:
            file.write(f"name: {self.name}, power_level: {self.power_level}")


class DefenseRobot(Robot):
    def __init__(self,name,model,weapon):
        super().__init__(name,model)
        self.weapon = weapon

    def perform_task(self):
        if self.power_level>=15:
           self.power_level-=15
           print(f"task 2 completed {self.name}, {self.model},{self.weapon},{self.power_level}")
        else:
            print(f"robot need more power")

    def __del__(self):
        print("Object cleaned")



class ServiceRobot(Robot):
    def __init__(self,name,model,service_type):
        super().__init__(name,model)
        self.service_type = service_type

    def perform_task(self):
        if self.power_level>=5:
           self.power_level-=5
           print(f"task 3 completed {self.name}, {self.model},{self.service_type},{self.power_level}")
        else:
            print(f"robot need more power")

    def __del__(self):
        print("Object cleaned")


work = WorkerRobot('Bob',"X1","Wrench")
work.perform_task()
work.charge(1)
work.show_info()
work.save_file("my")

defend = DefenseRobot("Defender","Z3","Laser")
defend.perform_task()
defend.charge(5)
defend.show_info()

service = ServiceRobot('Helper','x2','Cleaning')
service.perform_task()
service.charge(5)
service.show_info()