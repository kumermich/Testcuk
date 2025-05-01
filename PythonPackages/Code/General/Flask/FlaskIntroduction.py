############################
# Author: Sadegh Naderi
# Date created: 13.08.2023
# Path: BA23-14-Packages\report\Code\General\Flask\FlaskIntroduction.py
# Version: 1
# Reviewed by: Sadegh Naderi
# Review Date: 14.08.2023
############################


from flask import Flask, render_template

# Create a Flask web application instance
app = Flask(__name__)

# Define a list of dictionaries representing articles
articles = [
    {
        'author': 'John Smith',
        'title': 'Exploring Flask',
        'content': 'Diving into the world of Flask framework.',
        'date_posted': 'September 5, 2023'
    },
    {
        'author': 'Jane Williams',
        'title': 'Flask Magic',
        'content': 'Unveiling the magical aspects of Flask.',
        'date_posted': 'September 6, 2023'
    }
]


# Define route handlers using decorators to associate URLs with functions
@app.route("/")           # Maps root URL '/' to the homepage function
@app.route("/homepage")   # Maps '/homepage' URL to the same function
def homepage():
    return render_template('homepage.html', articles=articles)


@app.route("/about")     # Maps '/about' URL to the about function
def about():
    return render_template('about.html', title='About')

# Run the Flask app only when the script is executed directly (not imported as a module)
if __name__ == '__main__':
    app.run(debug=True)
