from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    title   ="homepage"
    num_ls = [1,2,3,4]
    return render_template('index.html', title=title, num_ls = num_ls)


@app.route('/about')
def about():
    title   ="About Us"
    return render_template('about.html', title=title)


@app.route('/contact')
def contact():
    title   ="Contact Us"
    return render_template('contact.html', title=title)

@app.route('/terms')
def terms():
    title   ="Terms of Use"
    return render_template('terms.html', title=title)

@app.route('/privacy')
def privacy():
    title   ="Privacy"
    return render_template('privacy.html', title=title)