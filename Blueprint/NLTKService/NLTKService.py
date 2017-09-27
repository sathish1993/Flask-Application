from flask import Blueprint, jsonify, redirect, url_for
import SpellCheck as sp
from nltk import word_tokenize, Text, pos_tag
from Blueprint.NeuralService.NeuralService import neuralmod

nltkmod = Blueprint('NLTKService', __name__)

#Method to do spell check and call the proposed event
@nltkmod.route('/NLTKService/<text>')
def doNLTK(text):
	#Current registered events in system
	actionsRegistered = ['get', 'pay', 'transfer']
	#splitting the given sentence into words(tokens)
	tokens = word_tokenize(text)
	
	#spell check for every word and add the corrected word in word_list
	word_list = []
	for word in tokens:
		wordcheck = sp.correction(word)
		word_list.append(wordcheck)

	#convert list of strings to final corrected sentence
	finalText = ' '.join(word_list)

	#find the part of speech of each word in the corrected text
	tags = pos_tag(Text(word_tokenize(finalText)))

	#checking for any action event in the text
	proposedEvents = []
	for word,tag in tags:
		if tag.startswith('VB'):
			proposedEvents.append(word.title())

	#Iterate over proposed events and find if there are any proposed event under registered event
	actionEvents = []
	nltkCheck = 'false'
	for event in proposedEvents:	
		if event.lower() in actionsRegistered:
			#if any proposed event is under registered this would call our service API
			actionEvents.append(event.lower())
			nltkCheck = 'true'
		else:
			#if not add that to registered event for future
			print "Added the current event to registered actions -->" + event
			actionsRegistered.append(event)

	if(nltkCheck == 'true'):
		#return the processed result
		return jsonify(results = actionEvents)
	else:
		#if there are no proposed events or if it is a trivial sentence call chatter bot library or neural
		return redirect(url_for('NeuralService.fetchNeural', text=finalText))