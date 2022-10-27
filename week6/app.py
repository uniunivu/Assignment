# 連線到資料庫

import mysql.connector
websiteDB = mysql.connector.connect (
    host="localhost",
    user="root",
    password="mlt125reV",
    database="website"
)

print(websiteDB)
webCursor = websiteDB.cursor()

sql = """SELECT * FROM member"""
addsql = """INSERT INTO member(name, username, password) VALUES (%s, %s, %s)"""


webCursor.execute(sql)
List = webCursor.fetchall()

usernameList =[]
passwordList =[]
nameList =[]
for x in List:
    usernameList= usernameList+[x[2]]
    passwordList= passwordList+[x[3]]
    nameList= nameList+[x[1]]
    
# print(username in usernameList)
# number = int(usernameList.index(username))
# print(webCursor)



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
        webCursor.execute(sql)
        List = webCursor.fetchall()
        usernameList =[]
        passwordList =[]
        nameList =[]
        for x in List:
            usernameList= usernameList+[x[2]]
            passwordList= passwordList+[x[3]]
            nameList= nameList+[x[1]]
        if username in usernameList and password == passwordList[int(usernameList.index(username))]:
            number = int(usernameList.index(username))
            session['username'] = nameList[number]
            return redirect("/member")
        elif username =="" or password == "":
            return redirect(url_for("error",message="請輸入帳號密碼"))
        else: 
            return redirect(url_for("error",message="帳號、或密碼輸入錯誤"))


@app.route("/member")
def member():
    if 'username' in session:
        name=session["username"]
        return render_template("member.html",n=name)
    else:
        return redirect("/")

@app.route("/error")
def error():
    message=request.args.get("message")
    return render_template("error.html",data=message)

@app.route("/signout")
def signout():
    session.pop("username", None)
    return render_template("signout.html")

@app.route("/count")
def count():
        return redirect(url_for('square', square_num=request.args.get("sq-number")))

@app.route("/signup", methods=["POST"])
def signup():
    newname=request.form["newname"]
    newusername=request.form["newusername"]
    newpassword=request.form["newpassword"]
    webCursor.execute(sql)
    List = webCursor.fetchall()
    usernameList =[]
    passwordList =[]
    nameList =[]
    for x in List:
        usernameList= usernameList+[x[2]]
        passwordList= passwordList+[x[3]]
        nameList= nameList+[x[1]]
    if newusername in usernameList:
        return redirect(url_for("error",message="帳號已經被註冊"))
    else:
        addData=(newname, newusername, newpassword)
        webCursor.execute(addsql, addData)
        websiteDB.commit() 
        return render_template("signup.html")


@app.route("/square/<square_num>")
def square(square_num):
    square_num=int(square_num)
    result = square_num**2
    return render_template("square.html",num=result)


app.run(port=3000)

