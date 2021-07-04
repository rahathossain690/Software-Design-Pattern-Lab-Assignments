"""
Rahat Hossain
SH-32
2-7-21
"""


class RegistrationAdapter:
    """Adapter class"""

    def __init__(self, vehicleRegistraionSystem):
        self.vehicleRegistraionSystem = vehicleRegistraionSystem
    

    def register(self, vehicle, city, country):
        """
            Registers the vehicle.
        """
        vehicle.register(city, country)
        self.vehicleRegistraionSystem.register(
            vehicle.id,
            vehicle.owner, 
            vehicle.model, 
            vehicle.manufacturing_date, 
            vehicle.manufacturing_year, 
            vehicle.manufacturer, 
            city, 
            country)
    
    def renew(self, vehicle, city, country):
        """
            Renews the vehicle.
        """
        vehicle.renew(city, country)
        self.vehicleRegistraionSystem.renew(
            vehicle.id,
            vehicle.owner, 
            vehicle.model, 
            vehicle.manufacturing_date, 
            vehicle.manufacturing_year, 
            vehicle.manufacturer, 
            city, 
            country)