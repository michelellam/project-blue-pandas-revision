#!/bin/bash 


#cd into our project folder
cd project-blue-pandas-revision-2

#making sure we have the updated changes from the main branch 
git fetch && git reset origin/main --hard

docker compose -f docker-compose.prod.yml down

docker compose -f docker-compose.prod.yml up -d --build