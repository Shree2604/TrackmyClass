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
        
def show_events(_id):
    user = db.users.find_one({'_id':_id})

def edit_groups(_id):
    user = db.users.find_one({'_id':_id})
    while 1 :
        x = int(input("Enter 1 to add group or 2 to remove :"))
        group = input("Enter the groupname of group you want to add or remove or 'exit' to stop editing :")
            if group == 'exit':
                break
            else:
                if x == 1 :
                    user['groups'].append(group)
                if x == 2 :
                    try : 
                        user['groups'].remove(group)
                        print('Group removed succesfully')
                    except :
                        print('You were not a member of that to begin with :')
    printf('You are in the following groups :',user['groups'])
                

def add_event(_id):
    user = db.user.find_one({'_id':_id})
    while 1 :
        group = input("Enter the groupname of the group for which you want to add the event or 'exit' to stop :")
        if group = 'exit' :
            break
        if group in user['groups']:
            group_info = db.groups.find_one({'groupname' : groups})
            if group_info == None :
                print("No such group exists, please try again .")
                continue
            name = input('Enter the name of the event you want to enter :')
            time_start = input("Enter the starting date and time of the event in following format using only digits (<date> <month> <year(YYYY)> - <hour> <minutes>) :")
            time_end = input("Enter the ending date and time of the event in following format using only digits (<date> <month> <year(YYYY)> - <hour(24 hour format)> <minutes>) :")
            time_start = datetime.strptime(time_start,"%d %m %Y - %H %M")
            time_end = datetime.strptime(time_end,"%d %m %Y - %H %M")
            event = {
                'name' : name ,
                'time_start' : time_start ,
                'time_end' : time_end
            }
            group_info['events'].append(event)
        else :
            print('You are not in that group, please try again')
            
def remove_event(_id):
    user = db.user.find_one({'_id':_id})
    while 1 :
        group = input("Enter the groupname of the group for which you want to remove the event or 'exit' to stop :")
        if group = 'exit' :
            break
        if group in user['groups']:
            group_info = db.groups.find_one({'groupname' : groups})
            if group_info == None :
                print("No such group exists, please try again .")
                continue
            name = input('Enter the name of the event you want to enter :')
            time_start = input("Enter the starting date and time of the event in following format using only digits (<date> <month> <year(YYYY)> - <hour> <minutes>) :")
            time_end = input("Enter the ending date and time of the event in following format using only digits (<date> <month> <year(YYYY)> - <hour(24 hour format)> <minutes>) :")
            time_start = datetime.strptime(time_start,"%d %m %Y - %H %M")
            time_end = datetime.strptime(time_end,"%d %m %Y - %H %M")
            event = {
                'name' : name ,
                'time_start' : time_start ,
                'time_end' : time_end
            }
            try :
                group_info['events'].remove(event)
            except :
                print('No such event found, please try again.')
        else :
            print('You are not in that group, please try again')

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
            print("You are signing up as a student :")
            username = input("Enter Username:")
            password = input("Enter Password:")
            password = hash(password)
            temp = db.students.find_one({"username" : username , "role" : "Student"})
            if temp == None :
                student = {
                    "username" : username , 
                    "password" : password ,
                    "role" : "Student" ,
                    'groups' : []
                }
                db.users.insert_one(student)
                temp = db.users.find_one(student)
                dashboard(temp['_id'])
            else :
                print("The username is taken. \nPlease try again..")

loginsignup()

