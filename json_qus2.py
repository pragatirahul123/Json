#python object ko json data convert
import json 
a={
    "name": "David",
     "class":"I",
     "age": 6  
 }
with open("q2.json","w") as f:
	json.dump(a,f)
	print(f)

