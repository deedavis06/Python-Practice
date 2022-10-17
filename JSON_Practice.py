import json
data = '''
{
    "name" : "Dee",
    "email" : {
        "type" : "student",
        "address" : "ddd1@my.unt.ex.edu"
    },
    "phone" :{
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Address:', info["email"]["address"])
print('Hide:', info["phone"]["hide"])