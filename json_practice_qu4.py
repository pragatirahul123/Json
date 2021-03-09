import json

sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
with open("practice2.json","w") as f:
	json.dump(sampleJson,f,sort_keys=True)
	
