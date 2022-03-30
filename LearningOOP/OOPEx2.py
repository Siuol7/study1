class Vehicles:
    def __init__(self,name,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
        self.name=name

class Bus(Vehicles):
    pass

Volvo= Bus('School Volvo',180,15)
print('Bus name:',Volvo.name,'Max speed:',Volvo.max_speed,'Mileage',Volvo.mileage )