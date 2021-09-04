from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def hello():
  return render_template('home.html')

@socketio.on('connect')
def handle_my_custom_event(json):
  print('User connected: ' + str(json))

@socketio.on('message')
def handle_my_custom_event(json):
  print('received json: ' + str(json))
  send(json["data"], broadcast=True)

if __name__ == "__main__":
  socketio.run(app, debug=True)