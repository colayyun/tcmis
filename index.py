import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

from flask import Flask, render_template,request
from datetime import datetime,timezone,timedelta

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>洪可芸Python網頁20231114b</h1>"
    homepage += "<a href=/mis>MIS</a><br>"
    homepage += "<a href=/today>顯示日期時間</a><br>"
    homepage += "<a href=/welcome?nick=洪可芸>傳送使用者暱稱</a><br>"
    homepage += "<a href=/about>可芸簡介網頁</a><br>"
    homepage += "<a href=/account>網頁表單輸入帳密傳值</a><br><br>"
    homepage += "<a href=/read>人選之人演員</a><br>"
    homepage += "<a href=/search>根據角色查詢演員</a><br><br>"
    homepage += "<a href=/books>精選圖書列表</a><br>"
    return homepage


@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    tz = timezone(timedelta(hours=+8))
    now = datetime.now(tz)
    return render_template("today.html",datetime = str(now))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)

@app.route("/account",methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd
        return result
    else:
        return render_template("account.html")

@app.route("/read")
def read():
    Request = ""
    db = firestore.client()
    collection_ref = collection("人選之人-造浪者")
    docs = collection_ref.get()
    for doc in docs:
        Rusult += "文件內容:{}".format(doc.to_dics()) + "<br>"
    return Result

@app.route("/books")
def books():
    request = ""
    db = firestore.client()
    collection_ref = db.collection("圖書精選")
    docs = collection_ref.order_by("anniversary").get()
    for doc in docs:
        bk = doc.to_dict()
        Rusult += "書名:<a href=" + bk["url"] + ">" + bk["title"] + "</a><br>"
        Result += "作者:"+ bk["author"] + "<br>"
        Result += str(bk["anniversary"] )+ "周年<br>"
        Result += "<img scr+=" + bk["cover"] + "></img><br><br>"
    return Result

if __name__ == "__main__":
    app.run(debug=True)
