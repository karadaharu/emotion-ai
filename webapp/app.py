from flask import Flask, jsonify, render_template, g, request
from sklearn import datasets, svm
from instaLooter import InstaLooter
import sqlite3
import os, random, sys

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

def init_records():
    db = get_db()
    imgs = os.listdir(os.path.join(app.root_path, 'static/img/'))
    for img in imgs:
        db.execute('insert or ignore into votes (filename) values (?)', [img])
    db.commit()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    init_records()
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

@app.route('/vote', methods=['GET', 'POST'])
def vote():
    if request.method == 'POST':
        img = request.form['img']
        print(request.form['ans'], file=sys.stderr)
        db = get_db()
        if request.form['ans'] == 'y':
            db.execute("update votes set yes_count = yes_count+1 where filename = ?", [img])
        elif request.form['ans'] == 'n':
            db.execute("update votes set no_count = no_count+1 where filename = ?", [img])
        db.commit()
        count = query_db('select * from votes where filename = ?', [img], one=True)
        print(count['yes_count'], file=sys.stderr)
        return 'aaa'

        # return count['yes_count']
    else:
        return 'aaab'
    # db = get_db()
    # db.execute('insert into votes (filename, count

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
