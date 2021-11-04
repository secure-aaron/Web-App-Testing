from flask import Flask, render_template
app = Flask(__name__) # __name__ is passed in. It is a special variable that python uses that contains the name of the module.

 
# This is a declarator that provides a route to allow us to write a function to return data on the website.
@app.route("/") # / is the root page, so homepage of the website.
@app.route("/home") # /home will return the same content.
def home():
    return render_template('home.html')

# About Page
@app.route("/about") # / is the root page, so homepage of the website.
def about():
    return "<h1>About Page</h1>" # Here we return a string, but all of this data can be HTML.

# Market Page
@app.route("/market") # / is the root page, so homepage of the website.
def market():
    return "<h1>Market Page</h1>" # Here we return a string, but all of this data can be HTML.

# Scanner Page
@app.route("/scanner") # / is the root page, so homepage of the website.
def scanner():
    return "<h1>Scanner Page</h1>" # Here we return a string, but all of this data can be HTML.


if __name__ == '__main__':
    app.run(debug=True)

