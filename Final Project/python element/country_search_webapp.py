import os
from flask import Flask, render_template, url_for, json,request
import country_search
app = Flask(__name__)

json_url = "timeseries.json"
data = json.load(open(json_url))


global state
state = {'country_name': " ",
         'date': " ",
         'result': " "}

@app.route('/')
@app.route('/main')
def main():
	print('in main')
	return render_template('hangman_country_search.html')

@app.route('/start')
def country_search_play():
	global state
	print('inside start')
	return render_template("country_search_start.html",state=state)


@app.route('/country_search_play',methods=['GET','POST'])
def info():
	global state
	if request.method == 'GET':
		return start()
	elif request.method == 'POST':
		state['country_name'] = request.form['country']
		date = request.form['date']
		for i in data:
			if i == state['country_name']:
				for x in data[i]:
					if x['date']==date:
						y=x
						state['result']=y
	return render_template('country_search_play.html',state=state)

@app.route('/about')
def about():
	global state
	
	return render_template("about.html",state=state)

if __name__ == '__main__':
    app.run('localhost',port=3400)