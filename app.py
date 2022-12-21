from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from game import Game

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

game = 'new_game'

@socketio.on('message')
def handle_message(data):
    global game 
    print('received message: ' + data['data'])
    if data['data'] == "START":
        game = Game()
        send(game.table)
    if data['data'] == "UP":
        game.move_up()
        send(game.table)
    if data['data'] == "DOWN":
        game.move_down()
        send(game.table)
    if data['data'] == "LEFT":
        game.move_left()
        send(game.table)
    if data['data'] == "RIGHT":
        game.move_right()
        send(game.table)

@app.route("/")
def main_page():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, '0.0.0.0', 8000)