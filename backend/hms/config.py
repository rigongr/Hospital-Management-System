import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_DB_URI = str(os.getenv('MONGO_DB_URI'))
    SECRET_KEY = str(os.getenv('SECRET_KEY'))