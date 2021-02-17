from textsearch import TextSearch
import json

class ContractText():
    def __init__(self):
        with open('svo_extraction/contract_dict.json', mode="r", encoding="utf-8") as json_file:
            self.contractdict = json.load(json_file)
        self.searching = TextSearch("ignore", "norm")
        self.searching.add(self.contractdict)

    def uncontract(self, text:str):
        return self.searching.replace(text)




