import socketio
import eventlet
from flask import Flask, render_template

io = socketio.Server()
app = Flask(__name__)

@io.on('chat')
def chat_message(sid, data):
    print(data['username'] + ' said: ' + data["contents"])

if __name__ == '__main__':
    app = socketio.Middleware(io, app)
    eventlet.wsgi.server(eventlet.listen(('', 3000)), app)
