from flask import Flask
import os
from flask import jsonify
import random as rnd
app=Flask(__name__)

@app.route('/')
def bot():
    return 'hello'

@app.route('/api/<name>')
def hey(name):
    message=[
        "hi,",
        "wellcome, ",
        "Fuck off, "
        ]
    return jsonify({
    "messages": [
    {"text": rnd.choice(message) + str(name)}
    ]
})
    
if __name__=="__main__":
    app.debug=True
    app.port=int(os.environ.get('PORT',5000))
    app.run()
