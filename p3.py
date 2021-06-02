# program to convert the python dictionary object(sort by key) to JSON data
import json
dict1 = {"name": 'yamini', "age": '26', "city": 'visakhapatnam'}
print("dict1")
print("\n\noutput after convertion")
print(json.dumps(dict1, indent=4))

