#Python object key unique key value ko accecc in json object
import json
a={
 "a":  1,
 "a":  2,
 "a":  3, 
 "a": 4,   
 "b": 1, 
 "b": 2
 }

s=json.dumps(a)
print(s)
