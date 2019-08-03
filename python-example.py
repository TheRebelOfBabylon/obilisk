from flask import Flask, render_template, request

import BEMDAS_algo_v3
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    	return render_template('main_page.html')

@app.route('/hello', methods=['GET', 'POST'])
def hello():

	eqn=str(request.form['display'])
	eqn=BEMDAS_algo_v3.main(eqn)
	#json_string = "["
	#s=0

	#while s < len(eqn)-2:

		#json_string=json_string+str(eqn[s])+","
		#s=s+1

	#json_string = json_string+str(eqn[s+1])+"]"
	#json_string=json.dumps(eqn)
	#print(json_string)
	return render_template('greeting.html', display=eqn)

if __name__ == "__main__":
   	app.run()