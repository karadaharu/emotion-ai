from flask import Flask, jsonify
from sklearn import datasets, svm

app = Flask(__name__)


@app.route('/')
def hello():
    # Load Dataset from scikit-learn.
    digits = datasets.load_digits()
    clf = svm.SVC(gamma=0.001, C=100.)
    clf.fit(digits.data[:-1], digits.target[:-1])
    prediction = clf.predict(digits.data[-1:])

    return jsonify({'prediction': repr(prediction)})

@app.route('/about')
def about():
    return 'about aaaaaaa'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
