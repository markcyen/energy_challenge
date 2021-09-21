from flask import Flask, jsonify
from collections import Counter
# from flask_restful import Resource, Api
# from flask_cors import CORS
import requests, json
import csv
# import os
# from urllib.request import urlopen
# import code; code.interact(local=dict(globals(), **locals()))

app = Flask(__name__)

# @app.route('/person/', methods=['GET'])
# def hello():
#   return jsonify({
#     'name': 'Mark',
#     'address': 'India'
#   })

r = requests.get('https://www.energy.gov/sites/prod/files/2020/12/f81/code-12-15-2020.json')
json_object = json.loads(r.text)
# json = r.json()
# data = json["releases"]

# @app.route('/')
# def convert():
raw_list = []
for object in json_object["releases"]:
  raw_list.append({
    "organization" : object["organization"],
    "status" : object["status"],
    "labor_hours" : object["laborHours"],
    "licenses": object["permissions"]["licenses"],
    "month" : object["date"]["created"]
  })
  # data_list
  # return jsonify(data_list)
d1 = {}
for key,value in raw_list.items():
  if value not in d1.values():
    d1[key] = value
print(d1)
# print(convert)

@app.route('/')
def energy():
  return jsonify(raw_list)

app.run(debug=True, port=5000)

# def energy_data():
#   # open_url = urllib.request.urlopen('https://www.energy.gov/sites/prod/files/2020/12/f81/code-12-15-2020.json')
#   r = requests.get('https://www.energy.gov/sites/prod/files/2020/12/f81/code-12-15-2020.json')
#   data = json.dumps(r)
  # object_list = []
  # for object in json:
  #   return jsonify({
  #     "organizations": object_list.append({
  #       'organization' : object.releases
  #     })
  #   })
  # json = r.text
  # data = json.loads(json)
  # return data
