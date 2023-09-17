import json
from pymongo import MongoClient


def PushToMongodb():

    # Locate chaos report file location
    filename = 'ChaosReport.txt'


    #Transform to json to push into the mongodb
    #Limitations text file & type ='name jhon' to {"name": "jhon"} works for multiple lines 
    dict1 ={}

    with open(filename) as chaosFile:

        for line in chaosFile:

            command, description = line.strip().split(None, 1)

            dict1[command] = description.strip()



    # create json file in the same folder
    # will override the same file in next run
    out_file = open("ChaosJsonFile.json","w")
    json.dump(dict1,out_file,indent=4,sort_keys=False)
    out_file.close()

    # building up connection with mongodb
    myclient = MongoClient("mongodb://localhost:27017/")

    # db will create/use with name chaosdb
    db = myclient["chaosdb"]

    # new collection will create/use with name chaoscollection
    collection = db["chaoscollection"]

    # reading json file and load it into a json object
    with open("ChaosJsonFile.json","r") as jsonfile:
        data = json.load(jsonfile)


    # insert the json object into the mongodb collection
    result = collection.insert_one(data)


    # close file & connection to db
    jsonfile.close()
    myclient.close()

    #return the inserted id of the instance
    return result.inserted_id



# print(PushToMongodb())