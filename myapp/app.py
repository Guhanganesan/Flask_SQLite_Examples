from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome!"

@app.route('/insert-data')
def insert_data():
    # http://127.0.0.1:5000/insert-data?name=Anbu&age=30&address=test&salary=23500
    with sqlite3.connect("./databases/test.db") as con:
        NAME=request.args.get('name')
        AGE=request.args.get('age')
        ADDRESS=request.args.get('address')
        SALARY=request.args.get('salary')
        cur = con.cursor()  
        cur.execute("INSERT into Employee (NAME,AGE,ADDRESS,SALARY) values (?,?,?,?)",(NAME,AGE,ADDRESS,SALARY))  
        con.commit()  
        return jsonify({'message':"Employee successfully Added"})  


@app.route('/retrieve-data')
def retrieve_data():
    with sqlite3.connect("./databases/test.db") as con:
        con.row_factory = sqlite3.Row  
        cur = con.cursor()  
        cur.execute("select * from Employee")  
        rows = cur.fetchall()
        for row in rows:
            print(row["ID"])
            print(row["NAME"])
            print(row["AGE"])
            print(row["SALARY"])
        return jsonify({'message':"Employee details successfully retrieved"}) 

if __name__=="__main__":
    #app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)
    app.run(debug=True)


