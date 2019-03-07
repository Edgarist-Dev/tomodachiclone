from sqlite3 import *
from math import *
import datetime

database = 'data/data.sqlite' #database file

personalities = ["Blank","Weird","Normal"]
genders = ["Male","Female","Other"]


connection = connect(database)
cursor = connection.cursor()
cursor.execute("SELECT * FROM islanders")
islanders = len(cursor.fetchall())
connection.close()


def new_islander(nickname,firstname,surname,gender,age,personality):
    now = datetime.datetime.utcnow()
    now = int((now - datetime.datetime(1970, 1, 1)).total_seconds())
 

    connection = connect(database)
    cursor = connection.cursor()
    if age >= 18:
        adult = 1
    else:
        adult = 0
        
        
        
    params = (nickname,firstname,surname,genders[gender],age,0,1,0,personalities[personality],adult,0,now)
    try:
        cursor.execute("INSERT INTO islanders VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", params)
        islanders += 1
    except IntegrityError:
        print("Error, ID already exists")
    
    connection.commit()
    connection.close()


def find_islander(search,field):  
    connection = connect(database)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM islanders WHERE %s='%s'" %(field,search))

    finds = cursor.fetchall()
    for i in finds:
        print(i)
    return finds

    connection.close()

def enter_room(room):
    connection = connect(database)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM islanders WHERE primary_key='%s'" %(room))
    finds = cursor.fetchall()
    if len(finds) == 0:
        print("No one in this room")
    else:
        print("You entered",finds[0][1]+"'s room")
    connection.close()

def show_building():
    print("There are currently",islanders,"islanders")


    
