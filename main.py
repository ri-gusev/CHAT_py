from flask import Flask, render_template, request, g
from flask_socketio import SocketIO
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super key'
upload_folder = os.path.join('CHAT/static','CHAT/uploads')
app.config['UPLOAD'] = upload_folder
socketio = SocketIO(app)

def message_received(methods=['Get','Post']):
    print('Сообщение получено')
    
@app.route('/')
def chat():
    return render_template('chat.html')

@socketio.on('my event') # если произошло событие "my event"
def my_event(json, methods=['GET','POST']):
    print('Получено сообщение'+str(json))
    socketio.emit('my response',json, callback=message_received)
    
socketio.run(app,debug=True,host='0.0.0.0')