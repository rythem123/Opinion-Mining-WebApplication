from ast import keyword
from flask import Flask,render_template,request,redirect,session,Response
import snscrape.modules.twitter as sntwitter
import mysql.connector
from requests import Session
from sentiment import *
import os

app=Flask(__name__)
app.secret_key=os.urandom(24)
# app.register_blueprint(second)

try:
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="user")
    cursor=conn.cursor()
except:
    print("An exception occured")

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/home')
def home():
    if 'user_id' in session:
        return render_template('front.html')
    else:
        return render_template('/')


@app.route('/login_validation', methods=['POST'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="user")
    cursor=conn.cursor()
    cursor.execute("""SELECT * from `users_table` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email, password))
    users = cursor.fetchall()
    if len(users)>0:
        session['user_id']=users[0][0]
        session['user_email'] = users[0][1]
        return render_template('front.html')
    else:
        return render_template('login.html')


@app.route('/add_user', methods=['POST'])
def add_user():
    name=request.form.get('uname')
    email = request.form.get('uemail')
    password = request.form.get('upassword')
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="user")
    cursor=conn.cursor()
    cursor.execute("""INSERT INTO `users_table` (`username`,`email`,`password`) VALUES ('{}','{}','{}')""".format(name,email, password))
    conn.commit()
    cursor.execute("""SELECT * from `users_table` WHERE `email` LIKE '{}'""".format(email))
    myuser=cursor.fetchall()
    session['user_id']=myuser[0][0]
    session['user_email'] = myuser[0][1]
    # return render_template('front.html')
    return home()

@app.route('/sentiment_analyzer', methods=['GET'])
def sentiment_analyzer():
    # q = request.form.get('keyword')
    # print(q)
    # getQuery(q, session['user_email'])
    # print(session['user_id'])
    # print(session['user_email'])
    return render_template("sentiment_analyze.html")

@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')

@app.route('/sentiment_logic',methods=['GET','POST'])
def logic():
    q = request.form.get('keyword')
    n = request.form.get('tweets')
    pos,neg,neu,pol,sub=getQuery(q,session['user_email'],n)
    return render_template('sentiment_analyze.html',polarity=pol,subjectivity=sub,positive=pos,neutral=neu,negative=neg,keyword=q,tweets=n)
@app.route('/visualize')
def visualize():
    return render_template('visual.html')    
if __name__=="__main__":
    app.run(debug=True)


