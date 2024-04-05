from flask import Flask, jsonify, request
import importlib
from flask_cors import CORS
import pandas as pd
import json
api_module = importlib.import_module("DatasetExtractor")


data = pd.read_csv('./Leetcode.csv')


app = Flask(__name__)
CORS(app)

def ourratingChart(username):
    global data

    if username not in data['username'].values:
        api_module.getData(username)
        # return json.dumps({'message': "User not found"})

    

    
    data = pd.read_csv('./Leetcode.csv')
    userData = data[data['username'] == username].iloc[0]
   
       
    programming_languages = []
    for i in range(6,30,1):
        programming_languages.append({'Language':data.columns[i],'ProblemSolved':int(userData[i])})

    dsaTopics = []
    for i in range(31,102,1) :
        dsaTopics.append({'DSATopics':data.columns[i],'ProblemSolved':int(userData[i])})
        
    # print(programming_languages)

    senddata = {
        'OurRating':str(userData[-1]),
        'programmingLanguages': programming_languages,
        'DSATopics':dsaTopics
    }

    return json.dumps(senddata)

def DSAPTopic():
    df = data[['username','Array']]
    print(df)

@app.route('/show', methods=['GET', 'POST'])
def show():
   username = request.form['username']
#    print(username)
   return ourratingChart(username)

@app.route('/showDSA', methods=['GET', 'POST'])
def showDSA():
   DSATopic = request.form['DSATopic']
#    print(DSATopic)
   DSAPTopic()
   return json.dumps(DSATopic)

@app.route('/get_chart_data')
def get_chart_data():
    print("hello word")

if __name__ == '__main__':
    app.run(debug=True)
    
