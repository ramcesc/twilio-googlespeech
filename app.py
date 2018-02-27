		
from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather, Say

application = Flask(__name__)

@application.route("/")
def hello():
    return("Hello World!")

@application.route("/welcome", methods=['GET', 'POST'])
def ans_call():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    #resp.say("Thank you for calling! Have a great day.", voice='alice')

    gather = Gather(
        input='speech', 
        timeout=3,
        hints='coconutt, chatbots',
        action = '/commands',)
    gather.play('https://storage.googleapis.com/coconutt-voz/bienvenido.mp3')
    resp.append(gather)    
    
    return(str(resp))
    
@application.route('/commands', methods=['GET', 'POST'])
def command():
    resp = VoiceResponse()

    if 'SpeechResult' in request.values:
        choice = request.values['SpeechResult']
        print(choice)

        if choice == 'coconutt' or 'coconut':
            resp.play('https://storage.googleapis.com/coconutt-voz/coconutt.mp3')
            return str(resp)
        elif choice == 'bots' or 'bot':
            resp.play('https://storage.googleapis.com/coconutt-voz/chatbot.mp3')
            return str(resp)
        else:
            resp.say('No te he entendido, te repito las opciones', language='es-MX')

    resp.redirect('/welcome')

    return(str(resp))

if __name__ == "__main__":
    application.run(debug=True)


