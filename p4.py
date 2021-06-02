# python program to sort a list of dictionaries using lambda.
dict1 = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
         {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
         {'make': 'Samsung', 'model': 7, 'color': 'BLue'}]

print("list after sorting by using lambda function(method:1)")
print(sorted(dict1, key=lambda i: i['model'])[::-1])
print("list after sorting by using lambda function(method:2)")
print(sorted(dict1, key=lambda i: i['model'], reverse=True))

