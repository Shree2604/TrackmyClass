import pymongo
from bson.objectid import ObjectId 
from bson.json_util import dumps
import os 
import json
from datetime import datetime
import hashlib
import datetime

MONGODB_URI = 'mongodb+srv://Pubzeee1311:12345@30daysofpython.xpenqyh.mongodb.net/'
client = pymongo.MongoClient(MONGODB_URI)
db = client['TrackmyClass']

def hash(classified):
    hasher = hashlib.sha256()
    binary_classified = classified.encode('utf-8')
    hasher.update(binary_classified)
    return hasher.hexdigest()

def add_groups(_id):
    user = db.users.find_one({'_id':_id})

def add_event(_id):
    user = db.user.find_one({'_id':_id})
    group = input("Enter the username of the group for which you want to add the event :")
    while 1 :
        if group in user['groups']:
            db.groups.find_one({'groupname'})
    name = input('Enter the name of the event you want to enter :')
    time_start = input("Enter the starting date and time of the event in following format using only digits (<date>-<month>-<year>--<hour>-<minutes>) :")
    time_end = input("Enter the ending date and time of the event in following format using only digits (<date>-<month>-<year>--<hour>-<minutes>) :")
    description = input("Enter a small description of the event :")
    event = {
        'name' : name ,
        'description' : description , 
        'time_start' : time_start ,
        'time_end' : time_end
    }
    
    

def show_events(_id):
    pass

def dashboard_student(_id):
    pass

def dashboard_cr(_id):
    pass

def dashboard_admin(_id):
    pass

def dashboard(_id):
    user = db.users.find_one({"_id":_id})
    if user['role'] == 'student' :
        dashboard_student(user['_id'])
    if user['role'] == 'cr' :
        dashboard_cr(user['_id'])
    if user['role'] == 'admin' :
        dashboard_admin(user['_id'])
    

def loginsignup():
    print("Welcome to TrackmyClass !!!\n")
    a = int(input("Enter 1 to login or 2 to sign up:"))
    if a == 1 : 
        roles = [ "Student" , "CR" , "Admin" ]
        while 1:
            b = int(input("Enter how do you want to login :\n0 for Student..\n1 for CR..\n1 for Admin..\n"))
            username = input("Enter Username:")
            password = input("Enter Password:")
            password = hash(password)
            user = db.users.find_one({"username" : username , "role" : roles[b] , "password" : password })
            if user == None :
                print("No such credentials found ...\nPlease try again.")
            else :
                print(f"You are logged in as {username} and role {user['role']}.")
                dashboard(user['_id'])
                break
            
        
    if a == 2 :
        while 1:
            roles = [ "Student" , "CR" , "Admin" ]
            b = int(input("Enter how do you want to login :\n0 for Student..\n1 for CR..\n"))
            while b == 2:
                print("You cannot signup as a admin")
                b = int(input("Enter how do you want to login :\n0 for Student..\n1 for CR..\n"))
            username = input("Enter Username:")
            password = input("Enter Password:")
            password = hash(password)
            temp = db.students.find_one({"username" : username , "role" : "Student"})
            if temp == None :
                groups = []
                while 1:
                    group = input("Enter a group username you are in or 'exit' to stop adding :")
                    if group == 'exit':
                        break
                    else:
                        groups.append(group)
                student = {
                    "username" : username , 
                    "password" : password ,
                    "role" : "Student" ,
                    "groups" : groups
                }
                db.users.insert_one(student)
                temp = db.users.find_one(student)
                dashboard(temp['_id'])
            else :
                print("The username is taken. \nPlease try again..")

loginsignup()

