import os

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{password}@{host}/textbook_buysell'.format(**{
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', 'himitu'),
    'host': os.getenv('DB_HOST', 'localhost:5432'),
})
SQLALCHEMY_TRACK_MODIFICATIONS = False


SECRET_KEY = 'secret_key'