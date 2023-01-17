class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.big = big
        self.medium = medium 
        self.small = small

    def addCar(self, carType):
        #checking if the incoming car is big and if parking space is available for big cars
        if carType == 1 and self.big > 0:
            self.big -=1
            return True
        
        #checking if the incoming car is medium and if parking space is available for medium cars
        elif carType == 2 and self.medium > 0:
            self.medium -=1
            return True 
        
        #checking if the incoming car is small and if parking space is available for small cars
        elif carType == 3 and self.small > 0:
            self.small -=1
            return True
        
        #If the car isnt either small,medium,big or if the parking space isnt available then we return false
        else:
            return False

class ParkingSystem(object):
    
    def __init__(self, big, medium, small):
        self.spaces = {1: big, 2: medium, 3: small}

    def addCar(self, carType):
        self.spaces[carType] -= 1
        return self.spaces[carType] >= 0       