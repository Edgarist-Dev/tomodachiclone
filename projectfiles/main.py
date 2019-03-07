##### main.py
##### last update 7/3/2019 

from sqlite3 import * #Import the sql lib 
from math import *    #Import math lib for stuff like floor() and ceil()
import datetime       #Import datetime to get dates

database = 'data/data.sqlite' #find database file

personalities = ["Blank","Weird","Normal"] #Lists to contain a few values
genders = ["Male","Female"]


connection = connect(database) #Open the database
cursor = connection.cursor()   #Create a cursor
cursor.execute("SELECT * FROM islanders") #Select all islanders
islanders = len(cursor.fetchall()) #set islanders to the amount of islanders in the database
connection.close() #close the database


def new_islander(nickname,firstname,surname,gender,age,personality): #Function to create a new islander
    now = datetime.datetime.utcnow() #get the current date in utc
    now = int((now - datetime.datetime(1970, 1, 1)).total_seconds()) #convert to epoch
 

    connection = connect(database) #Open the database
    cursor = connection.cursor()   #Create a cursor
    if age >= 18:  #Check to see if adult
        adult = 1
    else:
        adult = 0
            
    params = (nickname,firstname,surname,genders[gender],age,0,1,0,personalities[personality],adult,0,now) #Tuple contain all parameters
    cursor.execute("INSERT INTO islanders VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", params)      #Add a new islander based on params
    islanders += 1 #Add one to islanders
    
    connection.commit() #Save and close database
    connection.close()


def find_islander(search,field):  #Basically just a query
    connection = connect(database)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM islanders WHERE %s='%s'" %(field,search))

    finds = cursor.fetchall()
    for i in finds:
        print(i)
    return finds

    connection.close()

def enter_room(room): #This doesnt do much yet other than tell you an islanders name based on an id
    connection = connect(database)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM islanders WHERE primary_key='%s'" %(room))
    finds = cursor.fetchall()
    if len(finds) == 0:
        print("No one in this room")
    else:
        print("You entered",finds[0][1]+"'s room")
    connection.close()

def show_building(): #This doesnt do anything yet
    print("There are currently",islanders,"islanders")


    
