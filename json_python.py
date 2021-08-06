# Use Case:- fetching data from online API, configuration files etc. Javascript Object Notation.
import json

anime_collection = '''
{
    "anime": [
        {                
            "name":"One Piece",
            "isCompleted": false,
            "startYear": '1996'
        },
        {
            "name": "Naruto Shippuden",
            "isCompleted" : True,
            "StartYear": '1995'
        }
    ]
}
'''
# json(String) to python object --> json.loads()
data = json.loads(anime_collection)
print(type(data))

new_string = json.dumps(data, indent=2)
# python object to json string --> json.dumps

# json file to python object --> json.load()
# python object to json file --> json.dump()