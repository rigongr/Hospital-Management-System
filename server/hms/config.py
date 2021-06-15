import os

class Config:
    SECRET_KEY = 'b3815e21a23ee172f7ee12d304db313c' #For CSRF 
    MONGO_URI =  "mongodb+srv://Rigongr:rigon123@cluster0.oedx8.mongodb.net/sample_airbnb?retryWrites=true&w=majority"
    POSTGRE_URI = "postgresql://admin:testing123@localhost/myhospitality_db"