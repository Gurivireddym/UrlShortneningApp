from flask import Flask, redirect , render_template, request, session, flash, url_for
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes = 5)



@app.route("/")
def home():
	
	return render_template("index.html")


@app.route("/originalurl", methods = ['POST','GET'])
def Original():
	if request.method == 'POST':
		session.parmanent = True
		OUrl = request.form["URL"]
		session["OriginalUrl"] = redirect
		
		flash("login successfully")
		return redirect(url_for("ShortUrl"))
	else:
		if "OriginalUrl" in session:
			flash("already login")
			return redirect(url_for("ShortURL"))
			
		return render_template("login.html")

@app.route("/user", methods = ["POST","GET"])
def ShortURL():
	if "OriginalUrl" in session:
		OriginalUrl = session["OriginalUrl"]
		
		return redirect(url_for("IdRange",id = 10))
	else:
		flash("you are not logged in")
		return redirect(url_for("IdRange",id = 10))

@app.route("/Idrange")
def IdRange(id):
	
    char = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = len(char)
    data = []
	
    temp = id
    while id > 0:
        val = id % base
        data.append(char[val])
        id = id // base
    id = temp + 1
    return "".join(data[::-1])


if __name__ == "__main__":
	app.run(port = 2001, debug = True)


