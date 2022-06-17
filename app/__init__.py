from flask.app import Flask
from flask.templating import render_template
from flask_socketio import SocketIO,emit
app = Flask(__name__)
io = SocketIO(app)

@app.route('/')
def index():
    return render_template("index.html")

@io.on("sendMessage")
def send_message(msg):
    print(msg)
    emit('getMessage',msg,json=True,broadcast=True)