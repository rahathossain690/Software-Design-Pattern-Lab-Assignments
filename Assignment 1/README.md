# Assignment 1
Python code for assignment 1. This code uses composite, singeleton and adapter design pattern.

# Installing
1. Install python and pip.
2. Install packages from requirement.
```
pip install -r requirements.txt
```
3. Run 
```
python Main.py
```

# Problem description
A vehicle registration happens in Bangladesh, and involves a particular vehicle and its owners.
You may assume that there is only one owner per vehicle. Each vehicle maps to a vehicle
description that includes its manufacturing date, model, year, and manufacturer. A registration
can be renewed multiple times for the same owner and vehicle at the same county OR a different
one. It is necessary to keep track of the City in which the renewal was made. The vehicle
registration system is to be designed for quick retrieval of information about any vehicle or any
vehicle owner (in any City) and the related registration details.

# File Structure
1. RegistryInterface.py: Abstract class for vehicle and vehicle-registry-system.
2. Vehicle.py: Vehicle class implementation.
3. VehicleRegistrationSystem.py: Vehicle-registration-system class implementation. 
4. RegistrationAdapter.py: Registration adapter for Vehicle and vehicleRegistrationSystem class instances.
5. Main.py: Example driver program.
6. Output.txt: Output for the current Main.py.
7. ClassDiagram.png
8. SequenceDiagramOne_32.png: Sequence diagram for vehicle registration.
9. SequenceDiagramTwo_32.png: Sequence diagram for vehicle renewal.
10. TaskOneUML_32.zargo: argoUML file
11. SDP_Assignment_TaskOne.docx: Assumption details and basic description about the assignment.