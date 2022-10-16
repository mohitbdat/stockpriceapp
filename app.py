from flask import Flask, request
import json 
import random
import requests
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello():
    return '{"Student Number": "200504622"}'

@app.route('/webhook',methods=['POST'])
def index():
    
    body = request.json
    symbol = body['queryResult']['parameters']['stock']

    #symbol = 'AAPL'
    apikey = 'e15054a89cfd4361adafd867b422fe0c'

    api_url='https://api.twelvedata.com/eod?symbol='+ symbol + '&format=JSON&apikey='+ apikey
    #headers = {'Content-Type': 'application/json'} #Set the HTTP header for the API request
    response = requests.get(api_url) #Connect to openweather and read the JSON response.
    r=response.json() #Conver the JSON string to a dict for easier parsing.

    return r

