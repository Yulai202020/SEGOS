import json
def init(pyth):
    with open(pyth,"r") as f:
        return json.loads(f.read())
def update(conf,pyth):
    with open(pyth, 'w') as f:
        f.write(conf)
pyths = "../data/confjson/confige.json"
pyth = "../data/conf/confige.json"
mainconf = init(pyth)[0]['mainforlder']
settingdataconf = init(pyth)[1]['settingdataconf']