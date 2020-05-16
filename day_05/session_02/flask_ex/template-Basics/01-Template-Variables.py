from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # Pass in a puppy name
    # We insert it to the html with jinja2 templates!
    return '<h1> Go to /puppy/name </h1>'

@app.route('/puppy/<puppyname>')  # 127.0.0.1:5000/puppy/coconut
def puppy_name(puppyname):
    # Pass in a puppy name
    # We insert it to the html with jinja2 templates!
    return render_template('01-Template-Variables.html',name=puppyname)

@app.route('/advpuppy/<puppyname>')
def adv_puppy_name(puppyname):
    letters = list(puppyname)
    pup_dict = {'pup_name':puppyname}
    return render_template('01-Template-Variables.html',
                           name=puppyname,mylist=letters,mydict=pup_dict)


if __name__ == '__main__':
    app.run(debug=True)
