import os
from dotenv import load_dotenv

load_dotenv()

usr = os.getenv('BD_USER')
pswd = os.getenv('BD_PASSWORD')
DEBUG = True
SQLALCHEMY_DATABASE_URI = f'mysql://{usr}:{pswd}@0.0.0.0/music_recomentation_app'