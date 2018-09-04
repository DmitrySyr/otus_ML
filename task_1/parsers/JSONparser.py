import pandas as pd

from parsers.parser import Parser

class JSONParser(Parser):
    def __init__(self):
        pass

    def parse(self, data_json):
        """
        Override this method for fields extraction from data
        :param data: data can be in any appropriate format
        (text, json or other)
        :return: list of dictionaries where key is
        one of defined fields and value is this field's value
        """

        
        df = pd.DataFrame()

        for row in range(len(data_json)):
            try:
                if data_json[row]['cmeAnalyses'] != None:
                    df.loc[row, "activityID"] = data_json[row]['activityID']
                    df.loc[row, "sourceLocation"] = data_json[row]['sourceLocation']
                    df.loc[row, "latitude"] = data_json[row]['cmeAnalyses'][0]['latitude']
                    df.loc[row, "longitude"] = data_json[row]['cmeAnalyses'][0]['longitude']
                    df.loc[row, "halfAngle"] = data_json[row]['cmeAnalyses'][0]['halfAngle']
                    df.loc[row, "speed"] = data_json[row]['cmeAnalyses'][0]['speed']
                    df.loc[row, "type"] = data_json[row]['cmeAnalyses'][0]['type']
                    df.loc[row, "note"] = data_json[row]['note']
            except:
                print("Error while parsing json source in line ", row)

        return df
