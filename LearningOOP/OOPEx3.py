class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    
class Bus(Vehicle):
    def __init__(self,name,max_speed,mileage,capacity=50):
        super().__init__(name,max_speed,mileage)
        self.capacity=capacity
        

        
if __name__=='__main__':
    SchoolBus= Bus('Volvo',180,15)
    print(SchoolBus.name,SchoolBus.max_speed,SchoolBus.mileage,SchoolBus.capacity)
    print('The seating capacity of a', SchoolBus.name,' is', SchoolBus.capacity,'passengers')