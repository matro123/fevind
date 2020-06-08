import os
from flask import Flask, render_template
from flask import send_from_directory


app = Flask(__name__)
app.config.from_object('config')


@app.route('/favicon.ico')
def fav():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/use/')
def use():
    return render_template('use.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/me/')
def me():
    return render_template('me.html')


#global-------------------------------------------------------------------


#if __name__ == "__main__":
#    app.run()