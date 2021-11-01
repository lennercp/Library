import json
import psycopg2 as db

def connectDb():
    with open('config.json', 'r', encoding= 'utf-8') as file:
        dicionary = json.load(file)
        try:
            connect = db.connect(user= dicionary['user'], 
                                password= dicionary['password'],
                                host= dicionary['host'],
                                database= dicionary['database'])
            return connect
        except Exception as e:
            print('erro', e)
        