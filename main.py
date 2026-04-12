import json
with open("data/sample_route.json",'r') as file:
  dat = json.load(file)
d=list()
for i in dat:
  a,b=i["start"].split(":")
  t=int(a)*60+int(b)
  i["start_min"]=t
  a,b=i["end"].split(":")
  t=int(a)*60+int(b)
  i["end_min"]=t
dat.sort(key=lambda r: r["start_min"])
return dat
