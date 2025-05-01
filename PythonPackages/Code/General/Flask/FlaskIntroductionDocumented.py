"""! @brief Python program showcasing the Flask package."""
##
# @file: FlaskIntroductionDocumented.py
#
# @brief This script demonstrates a simple Flask web application using Doxygen-style comments for documentation.

############################
# Author: Sadegh Naderi
# Date created: 13.08.2023
# Path: BA23-14-Packages\report\Code\General\Flask\FlaskIntroductionDocumented.py
# Version: 2.0
# Reviewed by: Sadegh Naderi
# Review Date: 02.09.2023
############################

##
# @file: FlaskIntroductionDocumented.py
#
# @section description_of_file Description
# This script creates a basic Flask web application with routes for the homepage and an About page. HTML templates
# are used to render dynamic content, including a list of articles on the homepage and information about the blog
# on the About page.
#
# @section libraries Required Libraries
# The following code imports the necessary library for building the Flask web application:
# - Flask: A micro web framework used for creating web applications.
#   - For detailed documentation, visit: https://flask.palletsprojects.com/
#
# @section authors Author
# - Created by Sadegh Naderi on 13.08.2023.
# - Modified by Sadegh Naderi on 02.09.2023.
#

from flask import Flask, render_template

# Create a Flask web application instance

## @var app
#  @brief The Flask web application instance.
#
#  This instance of the Flask class is used to create and manage the web application.
#  It is the core object that handles incoming requests and routes them to the appropriate functions.
app = Flask(__name__)

# Define a list of dictionaries representing articles

## @var articles
#  @brief A list of dictionaries representing articles.
#
#  This list holds dictionaries containing information about different articles.
#  Each dictionary includes details such as the author, title, content, and date of the article.
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
    """! Render the homepage template with the list of articles.
    
    This function is associated with both the root URL '/' and the '/homepage' URL.
    It is responsible for rendering the homepage of the web application.
    It uses the 'homepage.html' template and provides the list of articles to be displayed.
    
    @return The rendered HTML page for the homepage.
    """
    return render_template('homepage.html', articles=articles)


@app.route("/about")     # Maps '/about' URL to the about function
def about():
    """! Render the about template with information about the blog.
    
    This function is associated with the '/about' URL.
    It is responsible for rendering the About page of the web application.
    It uses the 'about.html' template and provides the title 'About'.
    
    @return The rendered HTML page for the About page.
    """
    return render_template('about.html', title='About')

# Run the Flask app only when the script is executed directly (not imported as a module)
if __name__ == '__main__':
    app.run(debug=True)
