from flask import Flask,render_template,request,redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    title   ="Love_ff"
    return render_template('index.html', title=title)

# @app.route('/lang/<name>')
# def lang(name):
#     title   = name
#     return render_template('lang.html', title=title)

# @app.route('/about')
# def about():
#     title   ="About Us"
#     return render_template('about.html', title=title)


# @app.route('/contact')
# def contact():
#     title   ="Contact Us"
#     return render_template('contact.html', title=title)

# @app.route('/terms')
# def terms():
#     title   ="Terms of Use"
#     return render_template('terms.html', title=title)

# @app.route('/privacy')
# def privacy():
#     title   ="Privacy"
#     return render_template('privacy.html', title=title)


if __name__ == "__main__":
    # app.debug = True
    # app.run(host= '0.0.0.0', port='5000')
    app.run()  