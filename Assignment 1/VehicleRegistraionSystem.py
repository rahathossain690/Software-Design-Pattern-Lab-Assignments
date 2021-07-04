"""
Rahat Hossain
SH-32
2-7-21
"""

import pandas                                                               # for data storage
from RegistryInterface import RegistryInterface                             # Abstract class for implementation

class VehicleRegistraionSystem(RegistryInterface):
    """Vehicle Registration System that implements RegistryInterface"""

    __instance = None                                                       # object instance is held here 

    def __init__(self):
        columns = ['id', 'owner', 'model', 'manufacturing_date', 'manufacturing_year', 'manufacturer', 'city', 'country', 'registration_type']
        self.__datastore = pandas.DataFrame(columns=columns)                  # declaring pandas dataframe. A private variable

    def register(self, id, owner, model, manufacturing_date, manufacturing_year, manufacturer, city, country):
        """Creates a registration data entry"""

        if self.__datastore[self.__datastore['id'] == id].size != 0:            # if vehicle is already registered then raises exception
            raise Exception("Vehicle already registered. Please renew.")
        self.__datastore = self.__datastore.append({
            'id': id,
            'owner': owner,
            'model': model,
            'manufacturing_date': manufacturing_date,
            'manufacturing_year': manufacturing_year,
            'manufacturer': manufacturer,
            'city': city,
            'country': country,
            'registration_type': 'Registration'
        }, ignore_index=True)
    
    def renew(self, id, owner, model, manufacturing_date, manufacturing_year, manufacturer, city, country):
        """Creates a renew data entry"""

        if self.__datastore[self.__datastore['id'] == id].size == 0:            # if vehicle is already registered then raises exception
            raise Exception("Vehicle is not registered yet.")

        self.__datastore = self.__datastore.append({
            'id': id,
            'owner': owner,
            'model': model,
            'manufacturing_date': manufacturing_date,
            'manufacturing_year': manufacturing_year,
            'manufacturer': manufacturer,
            'city': city,
            'country': country,
            'registration_type': 'Renew'
        }, ignore_index=True)

    def registry_information(self):
        """
            Get whole data storage
        """
        return self.__datastore

    def search(self, atribute, value):
        """
            Method for searching in the data storage
        """
        return self.__datastore[self.__datastore[atribute] == value]
    
    def __new__(self): 
        """
            Calls before object creation. This method holds the instance for all inscanciation call.
        """
        if self.__instance is None:
            self.__instance = object.__new__(self)                          # Maintains singeleton design pattern. Creates one instance and shares for all calls.
        return self.__instance