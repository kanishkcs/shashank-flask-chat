from flask import Flask, render_template
from flask_socketio import SocketIO,send,emit
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret!"
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['transports'] = 'websocket'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

@socketio.on('message')
def handle_message(data):
    global list1
    if data!='m connected!':
        send(data,broadcast=True)
    else:
        print(data)

@app.route("/")
def home_page():
    return render_template("index.html")

if __name__ == '__main__':
    socketio.run(app,debug=True)


