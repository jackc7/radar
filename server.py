from flask import Flask, redirect, render_template, request, make_response
import serial

app = Flask(__name__)

@app.route('/')
def index():
    return '<a href="/collect">collect data</a>'

@app.route('/collect')
def collect():
    if request.args.get('n'):
        n = int(request.args.get('n'))
    else:
        n = 100000

    ser = serial.Serial('COM3', 115200)
    data = ser.read(n)
    ser.close()

    resp = make_response(data)
    resp.mimetype = "text/plain"
<<<<<<< HEAD

=======
    
>>>>>>> 8accb17a91241fb81294220f24ad2c84b4038d09
    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
