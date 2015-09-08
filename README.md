# short-circuit

Example of the [circuit breaker pattern][2] in Python. Uses the [pybreaker][3]
library.

![Johnny Five][1]

## Setup

```bash
$ git clone git@github.com:danriti/short-circuit.git
$ cd short-circuit
$ virtualenv .env
$ source .env/bin/activate
$ pip install -r requirements.txt
```

## Run the Example

Run the following command each in a separate terminal:

```bash
$ cd short-circuit
$ source .env/bin/activate
$ python app.py
```

```bash
$ cd short-circuit
$ source .env/bin/activate
$ python service_time.py
```

```bash
$ cd short-circuit
$ source .env/bin/activate
$ python service_user.py
```

Now visit `http://localhost:3000/` in your favorite browser!

[1]: https://github.com/danriti/short-circuit/raw/master/johnny-five.jpg
[2]: https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern
[3]: https://github.com/danielfm/pybreaker
