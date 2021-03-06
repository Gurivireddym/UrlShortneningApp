
from flask import render_template, request,redirect, Flask, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = 'hello'
app.config["SQLACHEMY_DATABASE_URI"] = 'sqlite:///app.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Urltable(db.Model):

   id = db.Column('id', db.Integer, primary_key = True)
   longurl = db.Column(db.String(100))
   shorturl = db.Column(db.String(50), unique = True)  
   

   def __init__(self, longurl, shorturl):
        self.longurl = longurl
        self.shorturl = shorturl
        
        
def ShortUrl():
    id = 10
    for i in Urltable.query.all():
        if i == id:
            pass
        else:
            id += 1
    char = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = len(char)
    data = str()
    while id > 0:
        var = id % base
        data = data + char[var]
        id = id // base

    else: 
        id +=1
        
    return data[::-1]

@app.route("/", methods = ["POST","GET"])
def home():
    if request.method == "POST":
        longurl = request.form["URL"]
        
        found_url = Urltable.query.filter_by(longurl = longurl).first()

        if found_url:
            return redirect(url_for("display",url1 = found_url.shorturl))
        else:
            
            shorturl = ShortUrl()
            new_url = Urltable(longurl = longurl,shorturl = shorturl)
            db.session.add(new_url)
            db.session.commit()
            
            return redirect(url_for("display",url1 = str(shorturl)))
    else:
        return  render_template("home.html")
    

@app.route("/display/<url1>")
def display(url1):
    
    return render_template("shorturl.html", shorturl = url1 )

@app.route("/all_urls")
def displayall():
    return render_template("all_urls.html", vals = Urltable.query.all())
    
if __name__ == "__main__":
    db.create_all()
    app.run(port = 10, debug = True)
            
