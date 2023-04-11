import json

#############
# Example 1 # 
#############
# # Creating a dictionary
# Dictionary ={1:'Welcome', 2:'to',
#             3:'Geeks', 4:'for',
#             5:'Geeks'}
  
# # Converts input dictionary into
# # string and stores it in json_string
# json_string = json.dumps(Dictionary)
# print('Equivalent json string of input dictionary:',
#       json_string)
 
# # Checking type of object
# # returned by json.dumps
# print(type(Dictionary))
# print(type(json_string))

#############
# Example 2 # 
############# 
# Dictionary ={(1, 2, 3):'Welcome', 2:'to',
#             3:'Geeks', 4:'for',
#             5:'Geeks'}
 
 
# # Our dictionary contains tuple
# # as key, so it is automatically
# # skipped If we have not set
# # skipkeys = True then the code
# # throws the error
# json_string = json.dumps(Dictionary,
#                          skipkeys = True)
 
# print('Equivalent json string of dictionary:',
#       json_string)

#############
# Example 3 # 
############# 
# # We are adding nan values
# # (out of range float values)
# # in dictionary
# Dictionary ={(1, 2, 3):'Welcome', 2:'to',
#             3:'Geeks', 4:'for',
#             5:'Geeks', 6:float('nan')}
 
# # If we hadn't set allow_nan to
# # true we would have got
# # ValueError: Out of range float
# # values are not JSON compliant
# json_string = json.dumps(Dictionary,
#                          skipkeys = True,
#                          allow_nan = True)
 
# print('Equivalent json string of dictionary:',
#       json_string)

#############
# Example 4 # 
############# 
Dictionary ={(1, 2, 3):'Welcome', 2:'to',
            3:'Geeks', 4:'for',
            5:'Geeks', 6:float('nan')}
 
# Indentation can be used
# for pretty-printing
json_string = json.dumps(Dictionary,
                         skipkeys = True,
                         allow_nan = True,
                         indent = 6)
 
print('Equivalent json string of dictionary:',
      json_string)