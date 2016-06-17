"""Flask app to control a robot arm - run on a Raspberry Pi."""
import flask
import RPi.GPIO as GPIO
import time


app = flask.Flask(__name__)


@app.route('/')
def index():
    """Index page."""
    return flask.render_template('index.html')


@app.route('/move/<direction>')
def move(direction):
    """Move in a direction."""
    GPIO.setmode(GPIO.BOARD)

    if direction == 'up':
        pin_number = 10
    elif direction == 'down':
        pin_number = 11
    elif direction == 'left':
        pin_number = 12
    elif direction == 'right':
        pin_number = 13
    else:
        flask.abort(400, 'Unknown command?!?!')

    GPIO.setup(pin_number, GPIO.OUT)
    GPIO.output(pin_number, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin_number, GPIO.LOW)
    GPIO.cleanup()

    return 'OK'


# Start app if running from command line like: python flask_arm.py
if __name__ == '__main__':
    app.run(host='', port=8000, debug=True)
