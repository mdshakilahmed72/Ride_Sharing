from abc import ABC,abstractmethod
from ride import Ride_request,RideMatching


class User(ABC):
    def __init__(self,name,email,nid):
        self.name = name
        self.email = email
        self.nid = nid 
        self.wallet = 0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError

class Rider(User):

    def __init__(self,name,email,nid,current_location,initial_amount):
        super().__init__(name,email,nid)
        self.current_location = current_location
        self.wallet = initial_amount
        self.current_ride = None
    
    def display_profile(self):
        print(f"Rider : {self.name}  and Email : {self.email}")
    
    def load_cash(self,amount):

        if amount>0:
            self.wallet += amount
        else:
            print("Your Amount is less Than 0 ")
    
    def update_location(self,current_location):
        self.current_location = current_location
    
    def request_ride(self,ride_sharing,destination,vechicle_type):
        ride_request = Ride_request(self,destination)
        ride_matching = RideMatching(ride_sharing.drivers)
        ride = ride_matching.find_driver(ride_request,vechicle_type)
        ride.rider = self
        self.current_ride = ride
        print("YAAA We got a Ride !! ")

    def show_current_ride(self):
        print("Ride Details !!!")
        print(f"Rider Name : {self.name}")
        print(f"Driver Name : {self.current_ride.driver.name}")
        print(f"Selected Veichle : {self.current_ride.vechicle.vechicle_type}")
        print(f"Star Location : {self.current_ride.start_location}")
        print(f"End Location : {self.current_ride.end_location}")
        print(f"Total Cost : {self.current_ride.estimated_fair}")
        



class Driver(User):

    def __init__(self,name,email,nid,current_location):
        super().__init__(name,email,nid)
        self.current_location = current_location
        self.wallet = 0
    

    def display_profile(self):
        print(f"Driver Name : {self.name}")
    
    def accept_ride(self,ride):
        ride.start_ride()
        ride.set_driver(self)

    def reach_destination(self,ride):
        ride.end_ride()





