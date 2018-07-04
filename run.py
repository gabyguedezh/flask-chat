import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello there!</h1>"
    
    
#The code "os.getenv" does the same as "os.environ.get('IP')" but it is shorter
app.run(host=os.getenv("IP"), 
        port=int(os.getenv("PORT")), 
        debug=True)