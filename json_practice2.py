import json
a={"name":"mona","enducation":"software","age":23}
with open("sam1.json","w")as data:
	json.dump(a,data)


