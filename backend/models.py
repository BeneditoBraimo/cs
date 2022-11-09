from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy


db_name = "cs_db"
db_user = "postgres"
db_password = "abc"
db_server = "127.0.0.1"
port = "5432"
database_path = f"postgres://{db_user}:{db_password}@{db_server}:{port}/{db_name}"