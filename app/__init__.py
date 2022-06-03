import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.jinja', title="MLH Fellow", url=os.getenv("URL"))

#@app.route ("/")
@app.route("/education")
def education():

     return render_template("education.jinja", educations=[{"name": "Michelle","school": "Binghamton University", 
      "major": "Computer Science"}, {"name": "Ruy", "school": "Tec de Monterrey", "major": "Computer Science" }] )

@app.route("/hobbies")
def hobbies():
     return render_template("hobbies.jinja" )

@app.route("/workexperience")
def workexperience():
     return render_template("work_experience.jinja", work=[{"name2": "Michelle", "company": "CS 110 Final Project", "description": "Using  the pygame library to build a basic platform game",
     "company2": "MLH Fellowship", "description2": "Part of the Production Engineer Track under the mentorship of Meta Engineers", "company3": "Tutor", "description3":" Voluteer to tutor elementary students on math"},

     {"name2": "Ruy", "company": "El club de los abuelos", "description": "develop a full-stack web application oriented to keep track of their patients health and examination procedures", 
     "company2": "Banco de Alimentos Guadalajara", "description2": "worked on the design of wireframes and system requirements of the web site of their branch Banco de Empleos Guadalajara", 
     "company3": "JANN (Jovenes ayudando a niñas y niños)", "description3": " free Math tutoring to kids from elementary and middle school" }])

if __name__ == "__main__":
     app.run(debug = True)

