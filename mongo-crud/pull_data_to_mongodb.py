from pymongo import MongoClient
from bson.objectid import ObjectId
import json

def PullFromMongodb(uniqueId):

    myclient = MongoClient("mongodb://localhost:27017/")

    db = myclient["chaosdb"]

    collection = db["chaoscollection"]

    
    query = {"_id": ObjectId(uniqueId)}
    #to filter '_id' from output
    filter = {"_id":0}

    document = collection.find_one(query, filter) # document type dict


    # Convert dict into json object
    json_file = json.dumps(document, indent=4)
    # print(json_file)


    #To save file JsonFile.json in the same directory
    # with open("JsonFile.json", "w") as outfile:
    #     json.dump(document, outfile)


    myclient.close()
    return json_file   # retun type json 
    # return document # retun type dict
