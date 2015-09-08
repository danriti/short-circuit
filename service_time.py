""" service_time.py """

from datetime import datetime

from flask import Flask, jsonify


app = Flask(__name__)
count = 0


@app.route("/time", methods=['GET'])
def get_datetime():
    global count
    count += 1
    return jsonify(count=count,
                   datetime=datetime.now().isoformat())


if __name__ == "__main__":
    app.run(port=3001, debug=True)
