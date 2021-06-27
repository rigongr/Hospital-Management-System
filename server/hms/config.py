import os

class Config:
    SECRET_KEY = 'b3815e21a23ee172f7ee12d304db313c' #For CSRF forms
    MONGO_URI =  "mongodb+srv://Rigongr:rigon123@cluster0.oedx8.mongodb.net/sample_airbnb?retryWrites=true&w=majority"
    
    POSTGRES_URL = "localhost:5432"
    POSTGRES_USER = "drizzle"
    POSTGRES_PW = "password"
    POSTGRES_DB = "hospitality"
    
    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)

