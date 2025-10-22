from abc import ABC


class Vechicle(ABC):
    speed = {
        "Car":60,
        "Bike":50,
        "CNG":30
    }

    def __init__(self,vechicle_type,license_plate,rate):
        self.vechicle_type = vechicle_type
        self.license_plate = license_plate
        self.rate = rate
    


class Car(Vechicle):
    def __init__(self,vechicle_type,license_plate,rate):
        super().__init__(vechicle_type,license_plate,rate)
    

class Bike(Vechicle):
    def __init__(self,vechicle_type,license_plate,rate):
        super().__init__(vechicle_type,license_plate,rate)   


class CNG(Vechicle):
    def __init__(self,vechicle_type,license_plate,rate):
        super().__init__(vechicle_type,license_plate,rate)