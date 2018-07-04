import os
from flask import Flask, redirect

app = Flask(__name__)
messages = []

def add_messages(username, message):
    """Add messagesto the messages list"""
    messages.append("{}: {}".format(username, message))

#We need a function to get all the messages, we'll use it later to display them
def get_all_messages():
     """Get all of the messages and separate them by a 'br'"""
     return "<br>".join(messages)

@app.route("/")
def index():
    """Main page with instructions"""
    return "To send a message use /USERNAME/MESSAGE"

#The next route will be a personalised homepage for each user
#depending on their URL
@app.route("/<username>")
def user(username):
    """Display chat messages"""
    # return "Welcome, {0} - {1}".format(username, messages)
    #Once we have out get_all_messages function, we comment the above and use it
    return "<h1>Welcome, {0}</h1> {1}".format(username, get_all_messages())
    #Notice how you can give a function as an argument here
    
#The next thing we need is a route that takes the username and message
@app.route("/<username>/<message>")
def send_message(username, message):
    """Create a new message and redirect it back to he chat page"""
    #We've added the add_messages function
    add_messages(username, message)
    #Intead of returning the string as commented above, we can use redirect...
    # return "{0}: {1}".format(username, message)
    return redirect(username)

#The code "os.getenv" does the same as "os.environ.get('IP')" but it is shorter
app.run(host=os.getenv("IP"), 
        port=int(os.getenv("PORT")), 
        debug=True)