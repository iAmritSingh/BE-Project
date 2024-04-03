from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import json


data = pd.read_csv('./Leetcode.csv')


app = Flask(__name__)
CORS(app)

def ourratingChart(username):
    usernameData = data[data['username'] == username].iloc[0]
    # print(usernameData)

    senddata = {
        'OurRating':str(usernameData[-1])
    }

    return json.dumps(senddata)

@app.route('/show', methods=['GET', 'POST'])
def show():
   username = request.form['username']
   print(username)
   return ourratingChart(username)

@app.route('/get_chart_data')
def get_chart_data():
    print("hello word")

if __name__ == '__main__':
    app.run(debug=True)
    
