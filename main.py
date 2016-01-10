import bottle
from bottle import request
from bottle import static_file
from mailer import build_message, send_email
from bottle import error


import cgitb


cgitb.enable(display=0, logdir="/")

@error(500)
def error500(error):
    return "Oops! Something went wrong and we couldn't send your message."

@bottle.route('/assets/<path:path>') #route for static files and css etc
def callback(path):
    return static_file(path, root='./matrimony/assets/')

@bottle.route('/') # Home Page
def rh_index():
    return bottle.template('matrimony/index')

@bottle.route('/mailer', method='POST') # Home Page
def mailer():
    try:
        message = build_message()
        send_email(message['user'], message['pwd'], message['recipient'], message['subject'], message['body'])
        return "Thank you, your RSVP has been sent!"
    except:
        return error500


bottle.debug(True)
bottle.run(host="localhost", port="8000")