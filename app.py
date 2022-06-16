import tweepy
import smtplib
from textblob import TextBlob
import re
import pandas as pd
import smtplib
from email.message import  EmailMessage
from flask import Flask,render_template, request


app = Flask(__name__)
@app.route("/")
@app.route("/",methods=['POST'])


def getvalue():
    if request.method=='POST':
        cus=request.form['Fname']
        sub=request.form['Sub']
        em=request.form['email']
        sentiment(cus,sub,em)
    return render_template('project.html')


def sentiment(a,b,c):
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    consumer_key = "zvghpJLaBrHdUqloJDlcV7rum"
    consumer_sec = "BKvbGtBlMBUPn9ONG1x7LrYkLclA2sRXT5G4KuGZiPgGlnNq2R"
    access_token = "1383703955218132994-lz4OavJh4DLABqVo4SBnjzqSWw72vE"
    access_token_sec = "oj254ngv1FjYnVveQOL1SQuRxOtR88xkROqaXSm8zalPQ"

    auth = tweepy.OAuthHandler(consumer_key, consumer_sec)
    # set the access token and access token secret
    auth.set_access_token(access_token, access_token_sec)
    # create an API object
    api_connect = tweepy.API(auth)
    text1 = b
    tweet_data = api_connect.search(text1,count=100)
    df = pd.DataFrame([tweet.text for tweet in tweet_data], columns=['Tweets'])
    
    def cleantxt(text):
        text = re.sub(r'@[A-Za-z0-9]+','',text)
        text = re.sub(r'#', '', text)
        text = re.sub(r'RT[\s]+','', text)
        text = re.sub(r'https?:\/\/\S+','',text)
        return text
    


    def getsubjectivity(text):
        return TextBlob(text).sentiment.subjectivity

# function to get polarity
    def getpolarity(text):
        return TextBlob(text).sentiment.polarity

    def getAnalysis(x): #polarity
        if (x < 0):
            return 'Negative'
        elif (x == 0):
            return 'Neutral'
        elif (x > 0):
            return 'Positive'


    df['Tweets'] = df['Tweets'].apply(cleantxt)
    

    df['Subjectivity'] = df['Tweets'].apply(getsubjectivity)
    df['Polarity'] = df['Tweets'].apply(getpolarity)
    df['Analysis'] = df['Polarity'].apply(getAnalysis)
    df.to_csv('sentimental_analysis.csv', header=False, index=False)
   
    msg=EmailMessage()
    msg['Subject']='Sentiment Analysis'
    msg['From']='Automation Team'
    msg['To']=c
    print(c)
    


    with open('email.txt') as myfile:
        data=myfile.read()
        msg.set_content("Sentimental Analysis on "+text1+" has been successfully done")
        msg.set_content(data)

    with open("sentimental_analysis.csv","rb") as f:
        file_data=f.read()
        file_name=f.name
        msg.add_attachment(file_data,maintype="application",subtype="xlsx",filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
        server.login('rythemsharma23@gmail.com','Project@1234')
        server.send_message(msg)
        








if __name__ == "__main__":  
    app.run(debug=True)  