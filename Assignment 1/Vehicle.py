"""
Rahat Hossain
SH-32
2-7-21
"""

from random import getrandbits                                          # for random id generations
import pandas                                                           # For data storing purposes

from RegistryInterface import RegistryInterface                         # Abstract class for implementation


class Vehicle(RegistryInterface):
    """Vehicle class that implements Registry interface"""

    def __init__(self, manufacturing_date, model, manufacturing_year, manufacturer, owner):
        """
            Constructor function of the vehicle
        """
        self.id = getrandbits(100)                                      # generating random bites
        self.model = model
        self. manufacturing_date = manufacturing_date
        self.manufacturing_year = manufacturing_year
        self.manufacturer = manufacturer
        self.owner = owner
        columns = ['city', 'country', 'registration_type']              # Columns
        self.__datastore = pandas.DataFrame(columns=columns)            # Creating a pandas dataframe. A private variable

    



    def __repr__(self):
        """
            Shows vehicle informations
        """
        return "Vehicle Description (ID: {0})\nOwner: {1}\nModel: {2}\nManufacturing Date: {3}\nManufacturing Year: {4}\nManufacturer: {5}\n".format(
            self.id, 
            self.owner, 
            self.model, 
            self.manufacturing_date, 
            self.manufacturing_year, 
            self.manufacturer)
    


    def register(self, city, country):
        """
            Registers current vehicle
        """
        if self.__datastore.size != 0:                                       # if vehicle is already registered then raises exception
            raise Exception("Vehicle already registered. Please renew.")

        self.__datastore = self.__datastore.append({
            'city': city,
            'country': country,
            'registration_type': 'Registration'
        }, ignore_index=True)
    



    def renew(self, city, country):
        """
            Renew current vehicle to some city and country
        """
        if self.__datastore.size == 0:                                       # if vehicle is not already registered then raises exception
            raise Exception("Vehicle is not registered yet.")
            
        self.__datastore = self.__datastore.append({
            'city': city,
            'country': country,
            'registration_type': 'Renew'
        }, ignore_index=True)


    
    def registry_information(self):
        """
            returns registry informations
        """
        return self.__datastore