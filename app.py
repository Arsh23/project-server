from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return 'Flask is running with git and supervisor and automated and without sudo !!!!'


@app.route('/data')
def names():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer", "sakshi"]}
    return jsonify(data)


if __name__ == '__main__':
    app.run()
