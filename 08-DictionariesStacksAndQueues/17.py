import json

f = open("euro.json")
rate = json.load(f)
print("effectiveDate","      ","mid")
for k, v in rate.items():
    print(v,",","      ")
f.close()