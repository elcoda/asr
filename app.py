from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# Placeholder import for Speechmatics real-time API
# from speechmatics import Speechmatics

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

# Using simple SocketIO server
socketio = SocketIO(app)

# Store current transcript to share with new clients
transcript_lines = []

@socketio.on('start_recognition')
def start_recognition():
    """Placeholder function to start ASR and stream results."""
    # In a real implementation, you would start microphone capture and
    # send audio to Speechmatics real-time API. Here we just emit a dummy line.
    line = 'Started recognition (demo).'
    transcript_lines.append(line)
    emit('transcript', line, broadcast=True)

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/view')
def view():
    return render_template('view.html')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5050)
