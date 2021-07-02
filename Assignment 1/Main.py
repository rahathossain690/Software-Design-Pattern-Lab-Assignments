"""
Rahat Hossain
2-7-21
"""

from Vehicle import Vehicle
from VehicleRegistraionSystem import VehicleRegistraionSystem
from RegistrationAdapter import RegistrationAdapter


"""Code demonstration"""

if __name__ == '__main__':


    """Declaring several vehicles"""
    
    vehicle_1 = Vehicle(
        owner="Rahat Hossain", 
        manufacturer="BMW",
        manufacturing_date="17-6",
        manufacturing_year="2021",
        model="BMWx7")

    print(vehicle_1) # printing vehicle information

    vehicle_2 = Vehicle(
        owner="Nafisa Naznin",
        manufacturer="Toyota",
        manufacturing_date="27-6",
        manufacturing_year="2021",
        model="Corolla"
    )

    print(vehicle_2)

    vehicle_3 = Vehicle(
        owner="Lil Rapper",
        manufacturer="Volkswagen",
        manufacturing_date="30-6",
        manufacturing_year="2020",
        model="ID.4"
    )

    print(vehicle_3)





    """Declaring a central vehicle registration system"""
    vehicleRegistraionSystem = VehicleRegistraionSystem() # declaring central vehicle registration system





    """Declaring an adapter for registration/renewal process"""
    registrationAdapter = RegistrationAdapter(vehicleRegistraionSystem) # declaring vehicle registration adapter 





    """performing several registration and renewal procedures"""

    registrationAdapter.register(
        vehicle=vehicle_1, 
        city="Dhaka",
        country="Bangladesh")
    
    registrationAdapter.register(
        vehicle=vehicle_2, 
        city="Sylhet",
        country="Bangladesh")
    
    registrationAdapter.register(
        vehicle=vehicle_3, 
        city="Chattogram",
        country="Bangladesh")
    
    registrationAdapter.renew(
        vehicle=vehicle_1, 
        city="Mumbai",
        country="India")



    """showing a single vehicle registry information"""
    print(vehicle_1.registry_information())


    
    """Showing all vehicle registry information"""
    print(vehicleRegistraionSystem.registry_information())






    """Vehicle information extraction for an id"""
    print(vehicleRegistraionSystem.search(atribute="id", value=vehicle_1.id))
    