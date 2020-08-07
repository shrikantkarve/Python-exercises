import json
import pprint
import os

pth = os.getcwd()
fpath = os.path.join(pth, "json/sample.json")
with open(fpath) as f:
    data = json.load(f)

pprint.pprint(data)