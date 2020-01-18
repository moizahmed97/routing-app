from pymongo import MongoClient
import os 

from dotenv import load_dotenv
from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

import urllib.parse

username = urllib.parse.quote_plus(USERNAME)
password = urllib.parse.quote_plus(PASSWORD)

client = MongoClient('mongodb+srv://%s:%s@routingapp-ifsle.mongodb.net/test?retryWrites=true&w=majority' % (username, password))