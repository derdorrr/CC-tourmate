import re
from model import Data
from flask import Flask, jsonify, make_response, request
import pickle
from flask_restful import Api, reqparse, Resource
import numpy as np


# class MyClass:
#     def __init__(self, name):
#         self.name = name


# if __name__ == '__main__':
#     o = MyClass('test')
#     with open('model.pkl', 'rb') as f:
#         pickle.dump(o, f)

app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))
api = Api(app)


# data_arg = reqparse.RequestParser()
# data_arg.add_argument("id", type=str)


@app.route('/')
def hello():

    return 'Hello World !'


@app.route('/wisata', methods=['GET'])
def get():

    dt = Data()
    values = ()

    id_ = request.args.get("Place_Id")
    if id_:
        query = "SELECT * FROM tourist where Place_Id = %s"
        values = (id_,)
    else:
        query = "SELECT * FROM tourist"
    data = dt.get_data(query, values)

    return make_response(jsonify({'data': data}), 200)


@app.route('/rekomendasi', methods=['GET'])
def rating():

    dt = Data()
    values = ()

    id_ = request.args.get("Place_Id")
    if id_:
        query = "SELECT * FROM tourist where Place_Id = %s"
        values = (id_,)
    else:
        query = "SELECT * FROM tourist ORDER BY Rating DESC LIMIT 10"
    data = dt.get_data(query, values)

    return make_response(jsonify({'data': data}), 200)


# @app.route("/rekomendasi", methods=['POST'])
# def rekomendasi():
#     def __init__(self):
#         self.model1 = model

#     def post(self):
#         # parse data from post request
#         args = data_arg.parse_args()
#         # convert string into int list
#         temp = args.id.strip('][').split(',')
#         temp = [float(i) for i in temp]
#         # predict output
#         out = self.model1.predict([temp])
#         # Return prediction
#         return jsonify({"message":  int(out)})


# api.add_resource(rekomendasi, '/')


if __name__ == '__main__':
    app.run(debug=True)
