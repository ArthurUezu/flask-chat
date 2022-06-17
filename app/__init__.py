from flask.app import Flask
from flask.templating import render_template
from flask_socketio import SocketIO,emit
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
io = SocketIO(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
db = SQLAlchemy(app)

from app.models.message import Message
@app.route('/')
def index():
    messages_db = Message.query.order_by(Message.date).all()
    return render_template("index.html",messages=messages_db)

@io.on("sendMessage")
def send_message(msg):
    message = Message(name=msg['nome'],message=msg['mensagem'],color=msg['cor'])
    db.session.add(message)
    db.session.commit()
    emit('getMessage',msg,json=True,broadcast=True)
