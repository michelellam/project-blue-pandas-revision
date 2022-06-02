import os
from flask import Flask, render_template, request,json
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

data = json.load(open('./app/static/data.json'))

@app.route('/')
def index():
    return render_template('index.html', title="MEET THE TEAM!",user1 = data["name1"],user2 = data["name2"], url=os.getenv("URL"))
