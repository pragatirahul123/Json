import json
#python dictionary convert to json string format
a={'name':'mona','age':23}
print(type(a))
b=json.dumps(a)
print(type(b))
