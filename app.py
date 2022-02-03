import time
import keyboard

# import mariadb
import threading
from types import TracebackType
import mysql.connector as mariadb
from flask import Flask, request, jsonify, render_template
from winsound import Beep

# import mysql.connector as mariadb

# Used to kill threads
# Killer = True
# counter = 0

# # Function used to run something every 'delay = 5' seconds
# def every(delay, task):
#     next_time = time.time() + delay
#     while True:
#         time.sleep(max(0, next_time - time.time()))
#         try:
#             if Killer:
#                 task()
#             else:
#                 break
#         except Exception:
#             TracebackType.print_exc()
#             # in production code you might want to have this instead of course:
#             # logger.exception("Problem while executing repetitive task.")
#         # skip tasks if we are behind schedule:
#         next_time += (time.time() - next_time) // delay * delay + delay


# # Test function
# def foo():
#     print("foo", time.time())


# Rings an alarm whenever functions is called for 3 secs.
# def Alarm():
#     AlarmTimer = 0
#     while AlarmTimer < 2:
#         duration = 1000  # milliseconds
#         freq = 420  # Hz
#         Beep(freq, duration)
#         print(AlarmTimer)
#         AlarmTimer += 1


# # Kills all threads when p is pressed
# def thread_killer():
#     while True:
#         if keyboard.read_key() == "p":
#             print("You pressed p")
#             global Killer
#             Killer = False
#             print("Threads killed")
#             break


# Multi threading to call functions every 5 seconds will not stop other code from running.
# 300 = 5mins 600= 10 mins.
# t1 = threading.Thread(target=lambda: every(5, Alarm))
# t1.start()

# t2 = threading.Thread(target=lambda: thread_killer())
# t2.start()


# def Every5():
#     while(True):
#         print('hello geek!')
#         schedule.run_pending()
#         time.sleep(1)
#         time.sleep(300)


app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():

    return "Hellow world"
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


# # creating database if it doesn't exist.
# my_cursor.execute("Create database if not exists testing")

# # Showing all databases
# my_cursor.execute("Show databases")

# # For loop to print all databases
# for records in my_cursor:
#     print(records)

# # create table called employee in database testing if it doesn't exist.
# my_cursor.execute(
#     "Create table if not exists employee (name varchar(200), salary int(20))"
# )


# # Showing all Tables
# my_cursor.execute("Show full tables")

# print("\n")
# # For loop to print all databases
# for tables in my_cursor:
#     print("Are there any tables? \n", tables)

# # Displays information about the columns in a given table.
# my_cursor.execute("Show columns from employee")
# print("This should be a new line", "\n")


# # For loop to display columns with their data in table eg:
# # { Feild    Type      Null   Key  Default  Extra}
# # ( 'sal', 'int(20)', 'YES',  '',    None,   ''  )
# for col in my_cursor:
#     print(col)

# print("\n")

# print("check tes")
# my_cursor.execute(
#     "CREATE TABLE IF NOT EXISTS accounts"
#     "("
#     "id int(11) NOT NULL AUTO_INCREMENT,"
#     "username varchar(50) NOT NULL,"
#     "temperature varchar(255) NOT NULL,"
#     "PRIMARY KEY (id)"
#     ")AUTO_INCREMENT=1"
# )
# print("UH Hello?")

# # for col in my_cursor:
# #     print(col)

# my_cursor.execute("Show columns from accounts")

# print("This should be a new line", "\n")

# for i in my_cursor:
#     print(i)


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


# name = "Hassan"
#     global counter

#     try:
#         data = request.get_json()
#         print(data)
#         global my_cursor, mydb
#         my_cursor.execute(
#             "INSERT INTO accounts" "(" "username, temperature" ")" "values(%s,%s)",
#             (data["username"], data["temperature"]),
#         )
#         # "DateCreated:": checkuser["dateCreated"].strftime("%d/%m/%Y %H:%M:%S"),
#         mydb.commit()
#         my_cursor.execute("select * from accounts")

#         for i in my_cursor:
#             print(i)

#     except Exception as e:
#         print("\n", e, "Error\n ")
#         # return  jsonify(e, "Error in data")
#         return (str)(e)

#     # if keyboard.read_key("p") and (counter == 0):
#     #     t1.join()
#     #     t2.join()
#     #     counter += 1
#     #     print("Should be ok")
#     return "works"
