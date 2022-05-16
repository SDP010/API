from flask import Flask, request, jsonify
import mysql.connector as conn
import pymongo

app = Flask(__name__)

@app.route('/fromsql', methods = ['POST'])  #route for extracting from sql databsse
def get_sqldata():
    user_id = request.json['user']
    passwd = request.json['password']
    db_name = request.json['database name']
    tab_name = request.json['table name']

    mydb = conn.connect(host='localhost', user=user_id, passwd=passwd)
    cursor = mydb.cursor()
    cursor.execute(f'select * from {db_name}.{tab_name}')
    result = cursor.fetchall()
    return jsonify(result)

@app.route('/frommongodb', methods = ['POST'])    #route for extracting from mongodb
def get_mongodbdata():

    connection_string = request.json['connection string']
    db_name = request.json['database name']
    coll_name = request.json['collection name']

    client = pymongo.MongoClient(connection_string)
    db = client[f'{db_name}']
    coll = db[f'{coll_name}']
    result = coll.find()
    return jsonify(str(list(result)))

if __name__ == '__main__' :
    app.run()


# connection_string = "mongodb+srv://sdp:mongodb@cluster0.q8kfd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
# db_name = test1
# coll_name = test1_coll2