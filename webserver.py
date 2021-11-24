from flask import Flask, render_template
from waitress import serve

app = Flask(__name__, static_url_path='',static_folder='dashboard/static',template_folder='dashboard/templates')

@app.route('/')
def index():
  return render_template('index.html')

def webserver_start():
    #for development
    #app.run()
    #for prod
    serve(app, host="0.0.0.0", port=5000)
