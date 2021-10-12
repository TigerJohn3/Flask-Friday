from flask import Flask, render_template

# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')

#def index():
#    return '<h1>Hello World!</h1>'

#Important Filters:
#safe - allows you to pass through HTML yourself
#capitalize
#lower
#upper
#title - capitalizes every first letter in every word
#trim - removes trailing spaces from the end
#striptags - use if you do not want people taking over your web server

def index():
    first_name = 'John'
    stuff = 'This is <strong>Bold</strong> text'

    great_states = ['Pennsylvania', 'Arizona', 'South Dakota', 'Utah']
    return render_template('index.html',
        first_name = first_name,
        stuff = stuff,
        great_states = great_states)

# localhost:5000/user/John
@app.route('/user/<name>')

def user(name):
    return render_template('user.html', name=name)

# Create Custom Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
