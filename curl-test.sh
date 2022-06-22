#!/bin/bash 

##POST it 
curl -X POST http://localhost:5000/api/timeline_post -d 'name=chelle&email=week4@gmail.com&content=completing week 4 LMS'

##get the request
curl http://localhost:5000/api/timeline_post
