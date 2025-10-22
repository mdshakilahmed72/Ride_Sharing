from datetime import datetime
from veichle import Car,Bike,CNG


class RideSharing:
    def __init__(self,company_name):
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []
    def add_rider(self,rider):
        self.riders.append(rider)
    def add_driver(self,driver):
        self.drivers.append(driver)
    
    def __str__(self):
        return f"Company Name {self.company_name} with riders : {len(self.riders)} and Drivers : {len(self.drivers)}"


class Ride:
    def __init__(self,start_location,end_location,vechicle):
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fair = self.calculate_fare(vechicle.vechicle_type)
        self.vechicle = vechicle
    

    def calculate_fare(self,vechicle):
        distance = 20
        fare_per_km = {
            "Car": 30,
            "Bike":40,
            "CNG":20
        }

        return distance * fare_per_km.get(vechicle)

    def set_driver(self,driver):
        self.driver = driver
    
    def start_ride(self):
        self.star_time = datetime.now()
    
    def end_ride(self):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fair
        self.driver.wallet += self.estimated_fair
    
    def __repr__(self):
        return f"Ride Details. Started  {self.start_location} to {self.end_location} "
    


class Ride_request:
    def __init__(self,rider,end_location):
        self.rider = rider
        self.end_location = end_location


class RideMatching:
    def __init__(self,driver):
        self.available_driver = driver
    
    def find_driver(self,ride_request,vechicle_type):
        if len(self.available_driver)>0:
            print(".....Looking For Drivers.....")
            driver = self.available_driver[0]
            

            if vechicle_type =="Car":
                vechicle = Car("Car","123ABC23",90)
            elif vechicle_type =="Bike":
                 vechicle = Bike("Bike","234BCZ",70)
            elif vechicle_type=="CNG":
                vechicle = CNG("CNG","23BCF43",40)

            ride = Ride(ride_request.rider.current_location,ride_request.end_location,vechicle)
            driver.accept_ride(ride)
            return ride
        

