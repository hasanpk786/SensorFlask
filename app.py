from flask_cors import CORS
import os
import mysql.connector as mariadb
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def hello_world():

    return "Hello cross origin world"


# connecting to mariadb using root user when no database selected#http://127.0.0.1:5000/
mydb = mariadb.connect(
    host="sql6.freemysqlhosting.net",
    user="sql6474147",
    password=os.environ.get("password"),
    port=3306,
    database="sql6474147",
)



# connecting to certain database in mariadb using root user.
# mydb = mariadb.connect(
#     host="localhost", user="root", database="testing", password="1234", port=3306
# )

# 
mydb = mariadb.connect(
    host="192.168.0.253", user="roche", database="Testing", password="Karachi123", port=3306
)


if mydb:
    print("Connected to MariaDB")
    # Alarm()
    print(mydb)
else:
    print("Connection Failed")
my_cursor = mydb.cursor()

# cursor for writing queries.

my_cursor.execute(
    "CREATE TABLE IF NOT EXISTS accounts"
    "("
    "id int(11) NOT NULL AUTO_INCREMENT,"
    "username varchar(50) NOT NULL,"
    "temperature varchar(255) NOT NULL,"
    "PRIMARY KEY (id)"
    ")AUTO_INCREMENT=1"
)


@app.route("/insert", methods=["GET", "POST"])
def insert():
    global my_cursor
    data = request.get_json()
    my_cursor.execute(
        "INSERT INTO accounts" "(" "username, temperature" ")" "values(%s,%s)",
        (data["username"], data["temperature"]),
    )
    print("Inserted")
    # "DateCreated:": checkuser["dateCreated"].strftime("%d/%m/%Y %H:%M:%S"),
    mydb.commit()
    return "Data inserted"


@app.route("/all", methods=["GET"])
def all():

    lister = {}
    retlist = []
    counter = 1

    try:
        my_cursor.execute("select * from accounts")

        for i in my_cursor:
            print(i, "entry")
            lister = {
                "Entry" + (str)(counter) + ":": {},
                "ID": i[0],
                "Name": i[1],
                "Temperature": i[2],
            }

            retlist.append(lister)
            counter += 1
        print("in try")
    except:
        return jsonify(errormsg="error in displaying All")
    return jsonify(retlist)


@app.route("/countRows", methods=["GET"])
def countRows():
    global my_cursor
    returner = 0
    my_cursor.execute("select COUNT(*) as RowCount from accounts")
    for i in my_cursor:
        if i[0] > 0:
            returner = i[0]
        print(i, "row count checks out")

    print(returner, "no loop needed here!")

    return (str)(returner)
