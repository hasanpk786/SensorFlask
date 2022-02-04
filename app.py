from flask_cors import CORS
import keyboard
import threading
import mysql.connector as mariadb
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def hello_world():

    return "Hello cross origin world"


# connecting to mariadb using root user when no database selected#http://127.0.0.1:5000/
# mydb = mariadb.connect(host="localhost", user="root",
#                        password="1234", port=3306)

# connecting to certain database in mariadb using root user.
# mydb = mariadb.connect(
#     host="localhost", user="root", database="testing", password="1234", port=3306
# )


# if mydb:
#     print("Connected to MariaDB")
#     # Alarm()
#     print(mydb)
# else:
#     print("Connection Failed")
# my_cursor = mydb.cursor()

# cursor for writing queries.


# @app.route("/all", methods=["GET"])
# def all():

#     lister = {}
#     retlist = []
#     counter = 1

#     try:
#         my_cursor.execute("select * from accounts")

#         for i in my_cursor:
#             print(i, "entry")
#             lister = {
#                 "Entry" + (str)(counter) + ":": {},
#                 "ID": i[0],
#                 "Name": i[1],
#                 "Temperature": i[2],
#             }

#             retlist.append(lister)
#             counter += 1
#         print("in try")
#     except:
#         return jsonify(errormsg="error in displaying All")
#     return jsonify(retlist)
