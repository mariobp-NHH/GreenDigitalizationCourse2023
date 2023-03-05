#1.a Create a dictionary.
efco2={'Bus': 0.1,
  'Car': 0.2,
  'Plane': 0.3,
  'Ferry': 0.1,
  'Motorbike': 0.1,
  'Bicycle': 0,
  'Walk': 0 }
print(efco2)

#1.b. Accessing an entry in a dictionary
print(efco2['Bus'])

#1.c. Updating an entry in a dictionary
efco2['Bus']=0.5
print(efco2['Bus'])
print(efco2)

#1.d. Deleting an entry
del efco2['Bus']
print(efco2)

#1.e. Know with type of Python component is efco2
print(type(efco2))

#2.a. Create a dictionary inside a dictionary
efco2['Bus']={'Diesel':0.10231,'CNG':0.08,'Petrol':0.10231,'No Fossil Fuel':0}
print(efco2)

#2.b. Accessing an entry in a dictionary
print(efco2['Bus']['Diesel'])

#3. Python methods in a dictionary
efco2={'Bus':{'Diesel':0.10231,'CNG':0.08,'Petrol':0.10231,'No Fossil Fuel':0},
  'Car':{'Petrol':0.18592,'Diesel':0.16453,'No Fossil Fuel':0},
  'Plane':{'Petrol':0.24298},
  'Ferry':{'Diesel':0.11131, 'CNG':0.1131, 'No Fossil Fuel':0},
  'Motorbike':{'Petrol':0.09816,'No Fossil Fuel':0},
  'Scooter':{'No Fossil Fuel':0},
  'Bicycle':{'No Fossil Fuel':0},
  'Walk':{'No Fossil Fuel':0}}
print(efco2)

#3.a. dictionary.get() method
print(efco2.get('Bus'))

#3.b. dictionary.items() method
print(efco2.items())
print(list(efco2.items()))
print(list(efco2.items())[0][0])
print(list(efco2.items())[0][1])

#3.c. dictionary.keys() method
print(efco2.keys())

#3.d. dictionary.values() method
print(efco2.values())

#4.a. Looping Techniques 
for k, v in efco2.items():
  print(k, v)

#4.b. Looping Techniques 
for k1, v1 in efco2.items():
  for k2, v2 in efco2[k1].items():
    print(k1, v1) 
    print(k2, v2)  


