from collections import defaultdict
class City:
    def __init__(self):
        self.lights = {'AJ':0,'BJ':1}
        self.cars = defaultdict(dict)
        self.roads = ['A','B','J']
    def addCar(self, id,details):
        self.cars[details.id] = details

    def updateLights(self):
        for i in self.lights.keys():
            self.lights[i] = 1 - self.lights[i]
    def simulate(self,car_id):
        #self.updateLights()
        waitingTime = 0
        exit = self.cars[car_id].entryTime
        for light in self.lights:
            if self.lights[light] == 1:
                exit += 1
            else:
                waitingTime += 3
        exit += 1
        return int(exit + waitingTime)

        
    

class Car:
    def __init__(self,id, entryTime):
        self.id = id
        self.entryTime = entryTime
        self.exitTime = 0
         

car = Car(1,2)
city = City()
city.addCar(1,car)
print(city.simulate(1))
        


        