import json

def SaveLatest(tosave: dict)->None:
    with open('./assets/config/temp/latest-save.json', 'w') as tmFilee:
        json.dump(tosave, tmFilee, indent=4)

def LoadLatest()->dict:
    with open('./assets/config/temp/latest-save.json', 'r') as tmFile:
        return json.load(tmFile)