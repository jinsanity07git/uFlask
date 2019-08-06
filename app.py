from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    title   ="homepage"
    num_ls = [1,2,3,4]
    return render_template('index.html', title=title, num_ls = num_ls)

    