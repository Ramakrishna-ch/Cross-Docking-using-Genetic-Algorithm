import random
import pprint
import numpy

dataset = []
datasize = 5128
truck_no = 0        # unique number of truck
approach_type = ""  
truckTypeList = ["OpenFlatBed", "ClosedFlatBed", "Container"]
truck_capacity = 0
material_category = 0
operation_time = 0  # total loading or unloading time in minutes.
weatherList = ["Summer", "Rainy", "Winter"]

c50 = 0
c100 = 0

for i in range(0, datasize//2):
    truck_no = i+1
    truck_type = truckTypeList[random.randint(0,2)]
    material_category = random.randint(1,3)
    operation_time = random.randint(30,240)
    weather = weatherList[random.randint(0,2)]
    
    approach_type = "In"
    truck_capacity = random.randrange(50, 150, 50)
    if truck_capacity == 50:
        c50 += 1
    else:
        c100 += 1
        
    dataset.append([truck_no, approach_type, truck_type, truck_capacity, material_category, operation_time,weather])
    
for i in range(datasize//2, datasize):
    truck_no = i+1
    truck_type = truckTypeList[random.randint(0,2)]
    material_category = random.randint(1,3)
    operation_time = random.randint(30,240)
    weather = weatherList[random.randint(0,2)]
    
    approach_type = "Out"
    truck_capacity = random.randrange(50, 150, 50)
    if truck_capacity == 50:
        if c50 >= 1:
           c50 -= 1 
        else:
            truck_capacity = 100
            c100 -= 1
    else:
        if c100 >= 1:
            c100 -= 1
        else:
            truck_capacity = 50
            c50 -= 1
        
    dataset.append([truck_no, approach_type, truck_type, truck_capacity, material_category, operation_time,weather])
    
dataset.insert(0, ["Truck No.", "In/Out", "Truck Type", "Truck Capacity", "Material Type", "Total Opr", "Weather"])
pprint.pprint(dataset)

numpy.savetxt('output.csv', dataset, delimiter=',', fmt='%s')