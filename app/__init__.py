from flask import Flask

app = Flask(__name__)
app.secret_key = 's0mth1ng s3cr3t'

from app import views
