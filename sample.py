"""
Flask app to host my sample
"""

from flask import Flask
app = Flask(__name__)


@app.route("/")
def index_page():
    return "Hello"

#--start---
if __name__=='__main__':
    app.run(host='0.0.0.0',port=6464)

