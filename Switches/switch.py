import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#define actuators GPIOs
sw1o = 14
sw2o = 15
sw3o = 18
sw4o = 2
sw5o = 3
sw6o = 4
sw7o = 17
sw8o = 27

#initialize GPIO status variables
sw1s = 0
sw2s = 0
sw3s = 0
sw4s = 0
sw5s = 0
sw6s = 0
sw7s = 0
sw8s = 0

GPIO.setup(sw1o, GPIO.OUT)
GPIO.setup(sw2o, GPIO.OUT)
GPIO.setup(sw3o, GPIO.OUT)
GPIO.setup(sw4o, GPIO.OUT)
GPIO.setup(sw5o, GPIO.OUT)
GPIO.setup(sw6o, GPIO.OUT)
GPIO.setup(sw7o, GPIO.OUT)
GPIO.setup(sw8o, GPIO.OUT)




GPIO.output(sw1o, GPIO.LOW)
GPIO.output(sw2o, GPIO.LOW)
GPIO.output(sw3o, GPIO.LOW)
GPIO.output(sw4o, GPIO.LOW)
GPIO.output(sw5o, GPIO.LOW)
GPIO.output(sw6o, GPIO.LOW)
GPIO.output(sw7o, GPIO.LOW)
GPIO.output(sw8o, GPIO.LOW)

@app.route("/")
def index():
    return render_template('switch.html')


@app.route("/<switchname>/<action>")
def action(switchname, action):
	if switchname == 'sw1':
		actuator = sw1o
	if switchname == 'sw2':
		actuator = sw2o
	if switchname == 'sw3':
		actuator = sw3o
	if switchname == 'sw4':
		actuator = sw4o
	if switchname == 'sw5':
		actuator = sw5o
	if switchname == 'sw6':
		actuator = sw6o
	if switchname == 'sw7':
		actuator = sw7o
	if switchname == 'sw8':
		actuator = sw8o
   
	if action == "on":
		GPIO.output(actuator, GPIO.HIGH)
	if action == "off":
		GPIO.output(actuator, GPIO.LOW)
		     
	
	sw1s = GPIO.input(sw1o)
	sw2s = GPIO.input(sw2o)
	sw3s = GPIO.input(sw3o)
	sw4s = GPIO.input(sw4o)
	sw5s = GPIO.input(sw5o)
	sw6s = GPIO.input(sw6o)
	sw7s = GPIO.input(sw7o)
	sw8s = GPIO.input(sw8o)
   
	templateData = {
	 	'sw1s'  : sw1s,
      		'sw2s'  : sw2s,
      		'sw3s'  : sw3s,
			'sw4s'  : sw4s,
			'sw5s'  : sw5s,
			'sw6s'  : sw6s,
			'sw7s'  : sw7s,
			'sw8s'  : sw8s,
	}
	return render_template('switch.html', **templateData)

@app.route("/find")
def test():
    result = "switch"
    return result


if __name__=="__main__":
    app.run(host ='0.0.0.0', port=80 ,debug=True )
