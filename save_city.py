import json


with open("active_cities.json", 'r') as f:
    # print(f.read())
    json_result = json.loads(f.read())
    print(json_result)

# json.loads()