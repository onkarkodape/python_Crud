import json
from src.utils.read_data import  read_file
from flask import Flask
from flask import request
from flask import (jsonify,make_response)
from  src import  app

# app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/get-details",methods= ['GET'])
def get_details():
    """
    Get the user details
    :return:
    """
    #Get content from the
    content =  read_file()

    name = dict()

    for data in content:
        index = data['index'],
        id = data['_id'],
        age = data['age']


        value = {
            "index": index,
            "age" : age,
            "id" : id
        }
        name[data['_id']] = value
    result = name






    return make_response(jsonify(result))



# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=3000,debug= True)
