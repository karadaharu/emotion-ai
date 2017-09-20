from flask import Flask, jsonify, render_template, g
from sklearn import datasets, svm
from instaLooter import InstaLooter
import sqlite3
import os, random

app = Flask(__name__)

app.config.from_object(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'emotionai.db'),
    SECRET_KEY='development key ai',
    USERNAME='admin',
    PASSWORD='defaultai'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

@app.route('/hello')
def hello():
    # Load Dataset from scikit-learn.
    digits = datasets.load_digits()
    clf = svm.SVC(gamma=0.001, C=100.)
    clf.fit(digits.data[:-1], digits.target[:-1])
    prediction = clf.predict(digits.data[-1:])

    return jsonify({'prediction': repr(prediction)})

@app.route('/')
def about():
    imgs = os.listdir(os.path.join(app.root_path, 'static/img/'))
    img = random.choice(imgs)
    return render_template('index.html', img=img)
    # return render_template('index.html')

@app.route('/vote', methods=['GET', 'POST'])
def vote():
    # db = get_db()
    # db.execute('insert into votes (filename, count
    return 'aaaa'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
