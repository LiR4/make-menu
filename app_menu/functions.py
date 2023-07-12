import requests as req 

class menuInfo():
    def getData(Data):
        data = req.get(Data['url'])
        global newData
        newData = data.json()
        global Name
        Name = list(newData.keys())

    def getCategory(cate):
        list = []
        for x in newData[f'{Name[0]}']:
            if x['categoria'] == cate:
                list.append(x)
        return list

