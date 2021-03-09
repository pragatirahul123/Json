#python dictionary convert to json

import json
dic={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}


var=dict(sorted(dic.items()))
s=json.dumps(var,indent=3)
with open("q4.json","w") as f:
	f.write(s)
