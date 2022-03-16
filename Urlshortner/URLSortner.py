# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 10:09:21 2022

@author: gguru
"""

from flask import render_template, request,redirect, Flask, url_for
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLACHEMY_DATABASE_URI"] = 'W:\HCL\VSCODe\app.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanant_session_lifetime = timedelta(minutes = 5)

db = SQLAlchemy(app)

class Urls(db.Model):
    id  = db.column(db.Integer, primary_key = True)
    longurl = db.column(db.varchar(100))
    shorturl = db.column(db.varchar(100), unique = True)
    
    def __init__(self,longurl,shorturl):
        self.longurl = longurl
        self.shorturl = shorturl

def ShortUrl(id):
    char = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = len(char)
    data = []
    while id > 0:
        var = id % base
        data.append(var)
        id = id // base
    return "".join(data[::-1])

@app.route("/", methods = ["POST","GET"])
def home():
    if request.method == "POST":
        longurl = request.form["url"]
        
        found_url = Urls.query.filter_by(longurl = longurl).first()
        if found_url:
            return redirect(url_for("display",url = found_url.shorturl))
        else:
            shorturl = ShortUrl(id)
            print(shorturl)
            new_url = Urls(longurl,shorturl)
            db.session.add(new_url)
            db.session.commit()
            return redirect(url_for("display",url = shorturl))
        
        
    else:
        
        return  render_template("home.html")
    

@app.route("/display/<url>")
def display(url):
   return render_template("shorturl.html", shorturl = url)

@app.route("/all_urls")
def displayall():
    return render_template("all_urls.html", vals = Urls.query.all())
    
if __name__ == "__main__":
    db.createall()
    app.run(port = 10, debug = True)
            