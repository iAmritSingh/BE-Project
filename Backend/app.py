from flask import Flask, jsonify, request
import importlib
from flask_cors import CORS
import pandas as pd
import json
api_module = importlib.import_module("DatasetExtractor")
api_module1 = importlib.import_module('Recommendations')


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

    Recommendations = api_module1.recommend_skills(username)
        

    senddata = {
        'OurRating':str(userData[-1]),
        'programmingLanguages': programming_languages,
        'DSATopics':dsaTopics,
        'totalActiveDays' : int(userData['totalActiveDays']),
        'contest_LastYear' : int(userData['contest_LastYear']),
        'contest_6months' : int(userData['contest_6months']),
        'contest_1month' : int(userData['contest_1month']),
        'last1monthActiveDays' : int(userData['last1monthActiveDays']),
        'last6monthActiveDays' : int(userData['last6monthActiveDays']),
        'Rating':int(userData['rating']),
        'last1monthActiveDays':int(userData['last1monthActiveDays']),
        'last6monthActiveDays':int(userData['last6monthActiveDays']),
        'totalActiveDays':int(userData['totalActiveDays']),
        'Recommendations':Recommendations
    }

    return json.dumps(senddata)



@app.route('/show', methods=['GET', 'POST'])
def show():
   username = request.form['username']
#    print(username)
   return ourratingChart(username)



@app.route('/get_chart_data')
def get_chart_data():
    print("hello word")

if __name__ == '__main__':
    app.run(debug=True)
    
