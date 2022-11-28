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