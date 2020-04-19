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

@app.route('/mess', methods=["GET"])
def verify():
    #webhook verification
    if request.args.get('hub.mode') == 'subscribe' and request.args.get('hub.challenge'):
        if not request.args.get('hub.verify_token') == 'Hello':
            return 'verification token mismatch', 403
        return request.args.get('hub.challenge'), 200
    return 'Hello World',200


    
if __name__=="__main__":
    app.debug=True
    app.port=int(os.environ.get('PORT',5000))
    app.run()
