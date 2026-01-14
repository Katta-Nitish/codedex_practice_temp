import json
da={"name":"Nitish","Age":21,"City":"Hyderabad"}
data=json.dumps(da,indent=4)
f=open("sample1.json","w")
f.write(data)
print(f)
print(data)
f.close()
