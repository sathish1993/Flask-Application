from flask import Flask, render_template, request, url_for, redirect
from Blueprint.NLTKService.NLTKService import nltkmod
from Blueprint.NeuralService.NeuralService import neuralmod

app = Flask(__name__)
#Registering Blueprints under single application
app.register_blueprint(NLTKService.NLTKService.nltkmod)
app.register_blueprint(NeuralService.NeuralService.neuralmod)

#Homepage
@app.route('/')
def index():
	return render_template('index.html')

#calling NLTK with the user entered text
@app.route('/', methods = ['POST'])
def indexPOST():
	textInput = request.form['text']
	return redirect(url_for('NLTKService.doNLTK', text=textInput))	

