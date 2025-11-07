dogs = {"Fido": 10, "Biggie": 9, "Wolfie": 1}

dogs["Lucy"] = 5

for dog, age in dogs.items():
    print(f"{dog} {age}")
    
for dog in dogs.keys():
    print(f"{dog} {dogs[dog]}")
    
for age in dogs.values():
    print(f"{age}")
    
sorted_dogs = sorted(dogs.items(), key=lambda x: x[0], reverse=False)
for dog, age in sorted_dogs:
    print(f"{dog}: {age}")

    