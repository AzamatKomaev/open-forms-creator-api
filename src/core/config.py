import os


"""
###################################################################################################
Do not change ENV variables here! Just create .env and .env.testing (copy .env.example and set your own values)
file in root folder and add these vars there!
###################################################################################################
"""


# Env variables for connection to DB
POSTGRES_DB = os.getenv('POSTGRES_DB', 'open_forms')
POSTGRES_TEST_DB = os.getenv('POSTGRES_TEST_DB', 'open_forms_test')
POSTGRES_USER = os.getenv('POSTGRES_USER', 'admin')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'admin123')

# Env variables for API
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'random_string')
UVICORN_HOST = os.getenv('UVICORN_HOST', '127.0.0.1')
UVICORN_PORT = os.getenv('UVICORN_PORT', '8000')
