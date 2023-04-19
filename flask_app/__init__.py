from flask import Flask

app = Flask(__name__)
app.secret_key = "any string we want"