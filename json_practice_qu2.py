import json

sampleJson = """{"key1": "value1", "key2": "value2"}"""
var=json.loads(sampleJson)
print(var['key2'])
