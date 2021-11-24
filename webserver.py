from flask import Flask, render_template

app = Flask(__name__, static_url_path='',static_folder='dashboard/static',template_folder='dashboard/templates')

@app.route('/')
def index():
  return render_template('index.html')

def webserver_start():
    app.run()
