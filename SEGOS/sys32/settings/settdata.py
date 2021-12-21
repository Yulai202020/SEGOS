import conf,json
def read(pyth):
    with open (pyth , "r") as files:
        textjson = files.read() 
        return textjson
data = read(conf.pyths)
data = json.loads(data)
Logs = data["logs"];progfiles = data["pyth"]