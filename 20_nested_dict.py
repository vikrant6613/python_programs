# create a nested dictionary

my_self = {
    "Name": "Vikrant",
    5687 : "ID",
    "Age": 35,
    "Sex": "Male",
    "Address": {
        "city": "Hyderabad",
        "state": "Telangana"
    }
}

for key, values in my_self.items():
    print(f"{key} : {values}")
