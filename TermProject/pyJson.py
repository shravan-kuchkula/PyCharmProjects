import json
with open('jobs1.json','r') as json_file:
	json_data = json.load(json_file)
print(type(json_data))
