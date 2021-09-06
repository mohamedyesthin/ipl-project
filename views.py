from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
import pymongo

def home(request):
        return render(request,'home.html',{'defenition':'INDIAN PREMIUM LEAGUE','Time':dt.datetime.now()})

def details(request):
    team=(request.GET['team'])
    captain=(request.GET['captain'])
    coach=(request.GET['coach'])
    p1=(request.GET['p1'])
    p2 = (request.GET['p2'])
    p3 = (request.GET['p3'])
    p4 = (request.GET['p4'])
    p5 = (request.GET['p5'])
    p6 = (request.GET['p6'])
    p7 = (request.GET['p7'])
    p8 = (request.GET['p8'])
    p9 = (request.GET['p9'])
    p10 = (request.GET['p10'])
    return render(request,'home.html',{'defenition':'INDIAN PREMIUM LEAGUE','Time':dt.datetime.now(),'team':team,'captain':captain,'coach':coach,'p1':p1,'p2':p2,'p3':p3,'p4':p4,'p5':p5,'p6':p6,'p7':p7,'p8':p8,'p9':p9,'p10':p10,'submit':"second.html"})
def result(request):
    team = (request.GET['team'])
    captain = (request.GET['captain'])
    coach = (request.GET['coach'])
    p1 = (request.GET['p1'])
    p2 = (request.GET['p2'])
    p3 = (request.GET['p3'])
    p4 = (request.GET['p4'])
    p5 = (request.GET['p5'])
    p6 = (request.GET['p6'])
    p7 = (request.GET['p7'])
    p8 = (request.GET['p8'])
    p9 = (request.GET['p9'])
    p10 = (request.GET['p10'])
    c = pymongo.MongoClient()
    db = c["ipl"]
    col = db["data"]
    x = col.insert_one({'team':team,'captain':captain,'coach':coach, 'p1': p1,'p2': p2,'p3':p3,'p4':p4,'p5':p5,'p6':p6,'p7':p7,'p8':p8,'p9':p9,'p10':p10})
    return render(request,'result.html',{'team':team,'captain':captain,'coach':coach,'p1':p1,'p2':p2,'p3':p3,'p4':p4,'p5':p5,'p6':p6,'p7':p7,'p8':p8,'p9':p9,'p10':p10})

# construct json object save into mongo
def index(request):
    return render(request,'index.html',{'hobbies':['a','b','c']})

def registerteams(request):
    c = pymongo.MongoClient()
    db = c["ipl"]
    col = db["data"]
    y=col.find()
    return render(request,'registerteams.html',{'regteam':y})

