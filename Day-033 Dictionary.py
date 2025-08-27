info = {'name': 'Karan', 'age': 19, 'eligible': True}
# print(info)
# print(info.keys())
# print(info['name']) -> both will give sam output
# print(info['name'])
# print(info['age2'])  -> it will throw a name error
# print(info.get('age2')) -> it will give None
# print(info.values())

# for key in info.keys():
#   print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")
