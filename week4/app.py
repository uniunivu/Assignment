from email import message
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for

app = Flask(__name__, static_folder="public", static_url_path="/")
app.secret_key = 'u3f9a82m4'
# 首頁
@app.route("/")
def index():
    if 'username' in session:
        return redirect("/member")
    return render_template("index.html")

# 驗證帳密頁面

@app.route("/signin", methods=["POST","GET"])
def signin():
    username=request.form["username"]
    password=request.form["password"]
    if request.method == 'POST':
        if username == "test" and password == "test":
            session['username'] = username
            return redirect("/member")
        elif username =="" or password == "":
            return redirect(url_for("error",message="請輸入帳號密碼"))
        else: 
            return redirect(url_for("error",message="帳號、或密碼輸入錯誤"))


@app.route("/member")
def member():
    name=session["username"]
    return render_template("member.html",n=name)

@app.route("/error")
def error():
    message=request.args.get("message")
    return render_template("error.html",data=message)

@app.route("/signout")
def signout():
    session.pop("username", None)
    return render_template("signout.html")

app.run(port=3000)

