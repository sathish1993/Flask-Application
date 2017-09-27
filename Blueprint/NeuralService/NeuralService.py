from flask import Blueprint, jsonify
#import ChatterBot as chat

neuralmod = Blueprint('NeuralService', __name__)

#if trivial sentence, chatterbot to called
@neuralmod.route('/NeuralService/<text>')
def fetchNeural(text):
	greeting = ['hi', 'how are you', 'hello']
	if text in greeting:
		return jsonify('hello')
	else:
		return jsonify('I can not help you')	
