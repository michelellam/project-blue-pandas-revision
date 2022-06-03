import os
from turtle import title
from flask import Flask, render_template, request,json
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

data = json.load(open('./app/static/data.json'))

@app.route('/')
def index():
    return render_template('index.jinja', title="MEET THE TEAM!",user1 = data["ruy"],user2 = data["michelle"], url=os.getenv("URL"))

@app.route('/<user>')
def homepage(user):
    return render_template('home.jinja',title = data[user]["name"],user = data[user],url=os.getenv("URL"))
