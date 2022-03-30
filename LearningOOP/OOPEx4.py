class Vehicle:
    color='White'
    def __init__(self,name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
class Bus(Vehicle):
    def __init__(self,name, max_speed,mileage):
        super().__init__(name, max_speed,mileage)
class Car(Vehicle):
    def __init__(self,name, max_speed,mileage,):
        super().__init__(name, max_speed,mileage,)

X=Bus('School VoVo',180,12)
Y=Car('Audi Q5',240,18)
print('Color:',X.color,'Vehicle Name:',X.name,'Speed:',X.max_speed,'Mileage:',X.mileage)
print('Color:',Y.color,'Vehicle Name:',Y.name,'Speed:',Y.max_speed,'Mileage:',Y.mileage)