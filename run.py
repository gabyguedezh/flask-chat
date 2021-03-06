import os
from datetime import datetime
from flask import Flask, redirect, render_template, request

app = Flask(__name__)
#we'll remove the var below from global and into our get_all_messages function
# messages = []

#Refactoring - Concentrate the process of writing to a file in a function
def write_to_file(filename, data):
    """Handle the process of writing data to a file"""
    with open(filename, "a") as file:
        file.writelines(data)

# #MAKING OF FUNCTION
# def add_messages(username, message):
#     """Add messages to the 'messages' list"""
#     #We will create a new variable called now to be able to use datetime here
#     now = datetime.now().strftime("%H:%M:%S")
#     #We will create a dictionary in order to be able to access more of our data
#     message_dict = {"timestamp": now, "from": username, "message": message}
#     # messages.append("{}: {}".format(username, message))
#     #After we've imported datetime and added it to this function, we change the 
#     #code commented above for the following...
#     # messages.append("({}) {}: {}".format(now, username, message))
#     #After we've create a dictionary, we change the code above for the following
#     messages.append(message_dict)
#So, at this point (before creating messages.txt to store our chats) we have:
# def add_messages(username, message):
#     """Add messages to the `messages` list"""
#     now = datetime.now().strftime("%H:%M:%S")
#     messages_dict = {"timestamp": now, "from": username, "message": message}
#     messages.append(messages_dict)
#And, then, we move things around and delete variables no longer needed...
# def add_messages(username, message):
#     """Add messages to the `messages` list"""
#     now = datetime.now().strftime("%H:%M:%S")
#     messages_dict = {"timestamp": now, "from": username, "message": message}
#     with open("data/messages.txt", "a") as chat_list:
#         chat_list.writelines("({0}) {1} - {2}\n".format(
#         messages_dict["timestamp"], 
#         messages_dict["from"].title(), 
#         messages_dict["message"]))
#Once we've created our write_to_file function, we refactor this function as well
        
#Just function
def add_messages(username, message):
    """Add messages to the `messages` text file"""
    write_to_file("data/messages.txt", "({0}) {1} - {2}\n".format(
            datetime.now().strftime("%H:%M:%S"),
            username.title(),
            message))

# #MAKING OF FUNCTION
# #We need a function to get all the messages, we'll use it later to display them
# def get_all_messages():
#     """Get all of the messages and separate them by a 'br'"""
#     #return "<br>".join(messages)
#     #Once we've changed our list for a dictionary un add_messages, we change the
#     #code above to return the dictionary, otherwise, we'd be trying to return a
#     #list, but our chat is now a dictionary so we'd get an error
#     return messages

#Just function
def get_all_messages():
    """Get all of the messages and separate them by a `br`"""
    messages = []
    with open("data/messages.txt", "r") as chat_messages:
        messages = chat_messages.readlines()
    return messages

# #MAKING OF FUNCTION
# # @app.route("/")
# #In order to add a form, we replace the commented code above for the following
# @app.route("/", methods=["GET", "POST"])
# def index():
#     """Main page with instructions"""
#     #We will add a form to request the username
#     if request.method == "POST":
#         # print(request.form)
#         #After we've created users.txt, we replace the commented code above...
#         with open("data/users.txt", "a") as user_list:
#             user_list.writelines(request.form["username"] + "\n")
#         return redirect(request.form["username"])
#     # return "To send a message use /USERNAME/MESSAGE"
#     #After we've created our templates folder and index.html file, we replace
#     return render_template("index.html")
# So, before refactoring, our function will be looking like this:
# @app.route('/', methods=["GET", "POST"])
# def index():
#     """Main page with instructions"""
#     if request.method == "POST":
#         with open("data/users.txt", "a") as user_list:
#             user_list.writelines(request.form["username"] + "\n")
#         return redirect(request.form["username"])
#     return render_template("index.html")
#Then, we refactor after creating the write_to_file function...

#Just the function
@app.route('/', methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    # Handle POST request
    if request.method == "POST":
        write_to_file("data/users.txt", request.form["username"] + "\n")
        return redirect(request.form["username"])
    return render_template("index.html")

#MAKING OF FUNCTION
# # #The next thing we need is a route that takes the username and message
# @app.route("/<username>/<message>")
# def send_message(username, message):
#     """Create a new message and redirect it back to he chat page"""
#     #We've added the add_messages function
#     add_messages(username, message)
#     #Intead of returning the string as commented above, we can use redirect...
#     # return "{0}: {1}".format(username, message)
#     return redirect(username)

#Just function

@app.route("/<username>/<message>")
def send_message(username, message):
    """Create a new message and redirect it back to he chat page"""
    add_messages(username, message)
    return redirect(username)

# #MAKING OF FUNCTION
# #The next route will be a personalised homepage for each user
# #depending on their URL
# @app.route("/<username>")
# def user(username):
#     """Display chat messages"""
#     # return "Welcome, {0} - {1}".format(username, messages)
#     #Once we have out get_all_messages function, we comment the above and use it
#     return "<h1>Welcome, {0}</h1> {1}".format(username, get_all_messages())
#     #Notice how you can give a function as an argument here
#After we've created our chat.html file, we will need to change this function
#and add a variable to store our messages, as well as update our return

#Just the function
@app.route('/<username>')
def user(username):
    """Display chat messages"""
    messages = get_all_messages()
    return render_template("chat.html", 
                            username=username, chat_messages=messages)

#The code "os.getenv" does the same as "os.environ.get('IP')" but it is shorter
app.run(host=os.getenv("IP"), 
        port=int(os.getenv("PORT")), 
        debug=True)