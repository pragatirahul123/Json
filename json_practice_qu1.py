#import json
#data = {"key1" : "value1", "key2" : "value2"}
#b=json.dumps(data)
#print(type(b))



###########################################################

import json
data = {"key1" : "value1", "key2" : "value2"}
with open ("practice.json","w") as f:
	var=json.dump(data,f)

