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
     return render_template("hobbies.jinja")

@app.route("/workexperience")
def workexperience():
     return render_template("work_experience.jinja")

if __name__ == "__main__":
     app.run(debug = True)

