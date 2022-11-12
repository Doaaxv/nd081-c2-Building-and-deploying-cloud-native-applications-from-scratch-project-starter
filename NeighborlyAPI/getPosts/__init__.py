import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
import os


def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        # Change the Variable name, as applicable to you
        url = os.environ["MyDbConnection"]
        client = pymongo.MongoClient(url)
        database = client['neighbourly']  # Change the MongoDB name
        collection = database['posts']    # Change the collection name

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except ConnectionError:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)
