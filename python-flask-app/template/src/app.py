from flask import Flask, jsonify, render_template, send_from_directory
import datetime
import socket
import random

dev_excuses = [
    "It worked on my machine.",
    "I thought I fixed that.",
    "I thought git would merge that.",
    "That's just a warning, not an error.",
    "You must have a corrupted database.",
    "It was working yesterday.",
    "I didn't write that part of the code.",
    "Test is for weak people.",
    "That's a hardware problem.",
    "I can't reproduce the problem.",
    "The client must have done something wrong.",
    "I have never seen that before.",
    "Specification was not clear.",
    "I did not have enought time for documentation.",
    "The code is the documentation.",
    "Copy passed was faster.",
    "Why should I have update my branch before merging ?",
    "I think my code have been erased with last forced push, cherry-pick or merge"
]

app = Flask(__name__)

@app.route('/')
def home():
    """home"""
    return render_template(
        'index.html',
        dev_excuse=random.choice(dev_excuses)
    )

@app.route('/api/json/v1/info')
def info():
    """get time, hostname and blabla"""
    return jsonify({
    	'time': datetime.datetime.now().strftime("%I:%M:%S%p on %A %d %B, %Y"),
    	'hostname': socket.gethostname(),
        'fqdn': socket.getfqdn(),
        'message': 'You are doing great, little human! <3',
        'deployed_on': 'localhost 4 the moment'
    })

@app.route('/api/html/v1/grettings')
def details():    
    """say hello in html"""

    if datetime.datetime.now().hour > 21:
        return '<h1>hello world, good night</1>'
    elif datetime.datetime.now().hour > 19:
        return '<h1>hello world, enjoy the rest of your evening</1>'
    elif datetime.datetime.now().hour > 16:
        return '<h1>hello world, have a pleasant evening</1>'
    elif datetime.datetime.now().hour > 12:
        return '<h1>hello world, good afternoon</1>'
    elif datetime.datetime.now().hour > 11:
        return '<h1>hello world, good noon</1>'
    elif datetime.datetime.now().hour > 10:
        return '<h1>hello world, have a nice late morning</1>'
    elif datetime.datetime.now().hour > 5:
        return '<h1>hello world, good morning</1>'
    else:
        return '<h1>hello world, have a nice dawn</1>'

@app.route('/api/json/v1/grettings')
def json_details():
    """say hello in json"""

    if datetime.datetime.now().hour > 19:
        return jsonify({ 'msg' : 'hello world, good night' })
    elif datetime.datetime.now().hour > 16:
        return jsonify({ 'msg' : 'hello world, good evening' })
    elif datetime.datetime.now().hour > 12:
        return jsonify({ 'msg' : 'hello world, good afternoon' })
    elif datetime.datetime.now().hour > 11:
        return jsonify({ 'msg' : 'hello world, good noon' })
    elif datetime.datetime.now().hour > 5:
        return jsonify({ 'msg' : 'hello world, goog morning' })
    else:
        return jsonify({ 'msg' : 'hello world, good dawn :)' })

@app.route('/api/json/v1/healthz')
def health():
    """get health status"""
	# Do an actual check here
    return jsonify({'status': 'up'}), 200

@app.route('/images-front/<filename>')
def images_frontend(filename):
    return send_from_directory('templates/img', filename)

if __name__ == '__main__':
    #app.run()
    ## from anywhere :]
    app.run(host="0.0.0.0")
