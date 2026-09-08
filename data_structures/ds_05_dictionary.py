# Dictionary in Python
# A dictionary is an unordered collection of items. Each item is stored as a key-value pair.
# Dictionaries are mutable, meaning they can be changed after creation.
# Syntax: my_dict = {"key1": "value1", "key2": "value2"}

user = {"name": "vinod", "age": 30, "city": "New York", "email": "vinod@example.com", "phone": "123-456-7890"}

user = {"name": "vinod", "age": 30, "city": "New York", "email": "vinod@example.com", "phone": "123-456-7890"}

#How to access values based on keys

print(user["name"]) #vinod
print(user["age"])#30
print(user["email"])#vinod@example.com

print(user.get("name")) #vinod
print(user.get("age"))#30
print(user.get("email"))#vinod@example.com


#update dict
# ====================
user["salary"] = 50000

print(user) #{'name': 'vinod', 'age': 30, 'city': 'New York', 'email': 'vinod@example.com', 'phone': '123-456-7890', 'salary': 50000}
print(user["salary"]) #50000

#How to get all keys and values from the dictionary
#========================================================
print(user.keys()) #dict_keys(['name', 'age', 'city', 'email', 'phone', 'salary'])
print(user.values())#dict_values(['vinod', 30, 'New York', 'vinod@example.com', '123-456-7890', 50000])

#How to get all key-value pairs from the dictionary
#========================================================
print(user.items()) #dict_items([('name', 'vinod'), ('age', 30), ('city', 'New York'), ('email', 'vinod@example.com'), ('phone', '123-456-7890'), ('salary', 50000)])

#How to check if a key exists in the dictionary
#========================================================
print( "email" in user) #True
print( "name" in user) #True
print( "location" in user) #False

#Update Value
# =====================================================
user.update({"name": "kumar"})
print(user.get("name")) #kumar
print(user) #{'name': 'kumar', 'age': 30, 'city': 'New York', 'email': 'vinod@example.com', 'phone': '123-456-7890', 'salary': 50000}

#Remove Key-Value Pair
# =====================================================
user.pop("salary")
print(user) #{'name': 'kumar', 'age': 30, 'city': 'New York', 'email': 'vinod@example.com', 'phone': '123-456-7890'}

#Remove Key-Value Pair using del
# =====================================================
del user["phone"]
print(user) #{'name': 'kumar', 'age': 30, 'city': 'New York', 'email': 'vinod@example.com'}

user.clear()
print(user) #{}