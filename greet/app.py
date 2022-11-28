from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
    html = '''
        <h1 
        style = "
        font-size:3em; 
        color:purple; 
        text-decoration: underline 3px purple;
        text-align: center"
        >The Home Page</h1>
        '''
    return html

@app.route('/welcome')
def welcome():
    html = '''
        <h1 
        style = "
        font-size:3em; 
        color:purple; 
        text-decoration: underline 3px purple;
        text-align: center"
        >Welcome!!!</h1>
        '''
    return html
@app.route('/welcome/home')
def welcome_home():
    html = '''
        <h1 
        style = "
        font-size:3em;
        margin:5em auto; 
        color:purple; 
        text-decoration: underline 3px purple;
        text-align: center"
        >Welcome Home!!!</h1>
        '''
    return html
@app.route('/welcome/back')
def welcome_back():
    html = '''
        <h1 
        style = "
        font-size:3em;
        margin: 5em auto; 
        color:purple; 
        text-decoration: underline 3px purple;
        text-align: center"
        >Welcome Back!!!</h1>
        '''
    return html