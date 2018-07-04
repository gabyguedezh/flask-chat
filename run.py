import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    """Main page with instructions"""
    return "To send a message use /USERNAME/MESSAGE"

#The next route will be a personalised homepage for each user
#depending on their URL
@app.route("/<username>")
def user(username):
    return "Hi " + username
    
#The next thing we need is a route that takes the username and message
@app.route("/<username>/<message>")
def send_message(username, message):
    return "{0}: {1}".format(username, message)

#The code "os.getenv" does the same as "os.environ.get('IP')" but it is shorter
app.run(host=os.getenv("IP"), 
        port=int(os.getenv("PORT")), 
        debug=True)