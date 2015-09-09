""" app.py """

from flask import Flask, render_template
import pybreaker
import requests


app = Flask(__name__)
time_breaker = pybreaker.CircuitBreaker(fail_max=3, reset_timeout=30)


@time_breaker
def _get_time():
    try:
        response = requests.get('http://localhost:3001/time', timeout=3.0)
    except (requests.exceptions.ConnectionError,
            requests.exceptions.Timeout):
        # please note that this is an example implementation and is
        # dangerously masking the original exception. i highly recommend
        # you take the appropriate means to capture/log the exception so
        # that you are aware of the underlying problem that is triggering
        # the circuit breaker!
        raise pybreaker.CircuitBreakerError
    return response.json().get('datetime')


def get_time():
    try:
        return _get_time()
    except pybreaker.CircuitBreakerError:
        return 'Unavailable'


def get_user():
    response = requests.get('http://localhost:3002/user')
    return response.json().get('name')


@app.errorhandler(500)
def page_not_found(_):
    return 'Server error', 500


@app.route("/")
def hello():
    time = get_time()
    name = get_user()
    return render_template('hello.html', name=name, time=time)


if __name__ == "__main__":
    app.run(port=3000, debug=True)
