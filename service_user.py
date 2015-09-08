""" service_user.py """

from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/user", methods=['GET'])
def get_user():
    return jsonify(name='Dan Riti')


if __name__ == "__main__":
    app.run(port=3002, debug=True)
