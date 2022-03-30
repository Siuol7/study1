class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    def __init__(self,name, mileage, capacity):
        super().__init__(name,mileage,capacity)
        print('Type of',self.name,type(self.name) )
        print('Type of',self.mileage,type(self.mileage) )
        print('Type of',self.capacity,type(self.capacity) )
        
School_bus = Bus("School Volvo", 12, 50)
print(School_bus)