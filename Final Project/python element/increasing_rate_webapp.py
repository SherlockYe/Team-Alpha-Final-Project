
import os
from flask import Flask, render_template, url_for, json,request
from datetime import date
import increasing_rate
app = Flask(__name__)

json_url = "timeseries.json"
data = json.load(open(json_url))


global state
state = {'country_name': " ",
         'start_date':" ",
		 'final_date':" ",
		 'start_date_year': " ",
		 'start_date_month': " ",
         'start_date_day': " ",
         'final_date_year': " ",
         'final_date_month': " ",
         'final_date_day': " ",
         'confirmed_difference': " ",
         'date_difference': " ",
         'date1': " ",
         'date2': " ",
         'average_rate': " ",
         'day_difference': " "}

@app.route('/')
@app.route('/main')
def main():
	print('in main')
	return render_template('hangman.html')

@app.route('/start')
def increasing_rate_play():
	global state
	print('inside start')
	return render_template("start.html",state=state)


@app.route('/increasing_rate_play',methods=['GET','POST'])
def rate():
	""" plays hangman game """
	global state
	if request.method == 'GET':
		return start()
	elif request.method == 'POST':
		state['country_name'] = request.form['country']
		start_date = request.form['start']
		final_date = request.form['final']
		start_date_year=int(start_date.split('-')[0])
		start_date_month=int(start_date.split('-')[1])
		start_date_day=int(start_date.split('-')[2])
		final_date_year=int(final_date.split('-')[0])
		final_date_month=int(final_date.split('-')[1])
		final_date_day=int(final_date.split('-')[2])
		for i in data:
			if i== state['country_name']:
				for x in data[i]:
					if x['date']==start_date:
						a=int(x['confirmed'])
					elif x['date']==final_date:
						b=int(x['confirmed'])
						break
	state['confirmed_difference']=b-a
	state['date1'] = date(start_date_year, start_date_month, start_date_day) 
	state['date2'] = date(final_date_year, final_date_month, final_date_day) 
	state['day_difference'] = increasing_rate.numOfDays( state['date1'],  state['date2']) 
	state['average_rate']=state['confirmed_difference']/state['day_difference']
	return render_template('increasing_rate_play.html',state=state)

@app.route('/about')
def about():
	global state
	
	return render_template("about.html",state=state)

if __name__ == '__main__':
    app.run('127.0.0.1',port=3000)