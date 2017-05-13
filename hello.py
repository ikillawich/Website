from flask import Flask, render_template, request, redirect, url_for
#from flask_ask import Ask, statement, question, session
import RPi.GPIO as gpio
import time
app = Flask(__name__)

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.cleanup()

on = False
off = True


pin = 12
gpio.setup(pin, gpio.OUT)
gpio.output(pin, off)

@app.route("/")
def hello():
    return render_template('index.html')


    
@app.route('/open/', methods = ['GET', 'POST'])
def openButton():
    if request.method == 'POST':
        gpio.output(pin, on)
    return redirect('/')

@app.route('/close/', methods = ['GET', 'POST'])
def closeButton():
    if request.method == 'POST':
        gpio.output(pin, on)
        time.sleep(13)
        gpio.output(pin, off)
    return redirect('/')

@app.route('/stop/', methods = ['GET', 'POST'])
def stopButton():
    if request.method == 'POST':
        gpio.output(pin, off)
        time.sleep(.5)
        gpio.output(pin, on)
        time.sleep(1)
        gpio.output(pin, off)
    return redirect('/')

@app.route('/off/', methods = ['GET', 'POST'])
def offButton():
    if request.method == 'POST':
        gpio.output(pin, off)
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True, port=8080)
