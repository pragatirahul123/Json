import json

#data=json.load(open("hello1.json"))
#print(data)


file=open("hello1.json","r")
data=json.load(file)
print(data)

