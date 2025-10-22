from ride import RideSharing,RideMatching,Ride_request,Ride
from users import Driver, Rider
from veichle import Vechicle,Car,CNG,Bike




ride_share = RideSharing("RideBond")
shakil = Rider("Shakil","shakil@gmail.com",123908,"Uttara",2000)

ride_share.add_rider(shakil)

ridoy = Driver("Ridoy","ridoy@gmail.com",123908,"Mohakhali")
ride_share.add_driver(ridoy)
request = shakil.request_ride(ride_share,"Mirpur","Car")
# ride = RideMatching.find_driver(request,"Car")



ridoy.reach_destination(shakil.current_ride)

shakil.show_current_ride()


