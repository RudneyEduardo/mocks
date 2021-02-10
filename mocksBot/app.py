from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Tela inicial'


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if 'teste' in incoming_msg:
        msg.body(f'Você digitou: {incoming_msg}')
        responded = True

    if not responded:
        msg.body("Você não digitou 'teste'") 
    
    return str(resp)


if __name__ == '__main__':
    app.run(debug=True)