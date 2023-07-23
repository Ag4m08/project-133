# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "agam" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/pro1162/family tree/templates/father.html")

# define the route to mother webpage
@app.route("/C:\Users\Admin\Downloads\pro116\pro1162\family tree\templates\mother.html")

# define the route to friends webpage
@app.route("/pro1162/family tree/templates/friend.html")

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
