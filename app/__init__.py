import os
from flask import Flask, render_template, request,json
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__, template_folder='templates')

data = json.load(open('./app/static/data.json'))

@app.route('/')
def index():
    return render_template('index.jinja', title="MEET THE TEAM!",user1 = data["ruy"],user2 = data["michelle"], url=os.getenv("URL"))

@app.route('/<user>')
def homepage(user):
    return render_template('home.jinja',title = data[user]["name"],user_data = data[user],user = user,url=os.getenv("URL"))

#@app.route ("/")
@app.route("/<user>/education")
def education(user):

     return render_template("education.jinja",  title = data[user]["name"], majors = data[user]["major"], uni_name = data[user]["school"],user = user,url=os.getenv("URL"))

@app.route("/<user>/hobbies")
def hobbies(user):

     return render_template("hobbies.jinja", title = data[user]["name"], pics = data[user]["hobbies_pics"],user = user,url=os.getenv("URL"))


@app.route("/<user>/workexperience")
def workexperience(user):
      return render_template("work_experience.jinja", title = data[user]["name"], companies = data[user]["companies"], workexperiences = data[user]["work_experiences"],user = user,url=os.getenv("URL"))

@app.route("/<user>/trips")
def trips(user):

     return render_template("trips.jinja", title = data[user]["name"],user = user,trips = data[user]["trips"],url=os.getenv("URL"))

if __name__ == "__main__":
     app.run(debug = True)





