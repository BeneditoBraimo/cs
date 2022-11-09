import os

SECRET_KEY = os.urandom(32)

# get the folder where the script is running
basedir = os.path.abspath(os.path.dirname(__file__))

# enable debug
DEBUG = True

# database connections params
db_user = "postgres"
db_password = "abc"
db_server = "127.0.0.1"
db_port = "5432"
db_name = "cs_db"

# connect to the database
SQLALCHEMY_DATABASE_URI = f"postgresql://{db_user}:{db_password}@{db_server}:{db_port}/{db_name}"