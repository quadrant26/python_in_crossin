speed = 60.0
distance = 100
time = distance/speed
print(time)

class Car:
    speed = 0

    def drive(self, distance):
        time = distance/ self.speed
        print(time)

car = Car()
car.speed = 60.0
car.drive(100.0)
car.drive(200.0)

car2 = Car()
car2.speed = 150.0
car2.drive(100.0)
car2.drive(200.0)
