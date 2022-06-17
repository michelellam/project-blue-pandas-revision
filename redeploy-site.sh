#!/bin/bash 

#kill all tmux sessions
tmux kill-server

#cd into our project folder
cd project-blue-pandas-revision-2

#making sure we have the updated changes from the main branch 
git fetch && git reset origin/main --hard

#entering the python virtual environment
source python3-virtualenv/bin/activate

#install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt 

#detached tmux + enters the flask environment 
tmux new -d "flask run --host=0.0.0.0"