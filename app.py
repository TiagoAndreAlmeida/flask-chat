from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def hello():
  return render_template('home.html')

@socketio.on('connect')
def handle_connection(json):
  socketio.emit('geral', {
    "user": {
      "name": "Bot Legal =D"
    },
    "message": "o usuário {} entrou no chat".format(json["name"])
  })

@socketio.on('geral')
def handle_my_custom_event(data):
  print(data)
  socketio.emit('geral', data)

@socketio.on('message')
def handle_my_custom_event(json):
  print('received json: ' + str(json))
  send(json["data"], broadcast=True)

if __name__ == "__main__":
  socketio.run(app, debug=True)