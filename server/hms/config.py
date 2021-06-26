import os

class Config:
    SECRET_KEY = 'b3815e21a23ee172f7ee12d304db313c' #For CSRF forms
    MONGO_URI =  "mongodb+srv://Rigongr:rigon123@cluster0.oedx8.mongodb.net/sample_airbnb?retryWrites=true&w=majority"


    def get_env_variable(name):
        try:
            return os.environ[name]
        except KeyError:
            message = "Expected environment variable '{}' not set.".format(name)
            raise Exception(message)


    
    POSTGRES_URL = get_env_variable("POSTGRES_URL")
    POSTGRES_USER = get_env_variable("POSTGRES_USER")
    POSTGRES_PW = get_env_variable("POSTGRES_PW")
    POSTGRES_DB = get_env_variable("POSTGRES_DB")
    
    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)

