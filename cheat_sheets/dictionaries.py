# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# The dictionary contains keys linked to values
dict = {'key':'value', 'key':'value'}
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo'}
europe['france'] = 'paris'
# Keys must be uniquem otherwise only the last one will stay
# Keys must be immutable : no lists allowed

# Select all keys :
dict.keys()

# Add a key or modify its value :
europe["italy"] = 'rome'

# Remove a value :
del(europe["italy"])

# Check if a value is in the dictionary :
"italy" in world 
# gives True

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

# Use
print(europe['france']['capital'])

# Create sub-dictionary data
data = { 'capital':'rome', 'population': 59.83 }
# Add data to europe under key 'italy'
europe['italy'] = data