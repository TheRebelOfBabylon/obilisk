from app import app, db
from app.models import User
from flask import Flask, render_template, request

import BEMDAS_algo_v3_prod
import json
import rpc_pb2 as ln
import rpc_pb2_grpc as lnrpc
import grpc
import codecs
import os

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

with open(os.path.expanduser('/Users/paulcote/Downloads/stuff/admin.macaroon'), 'rb') as f:

	macaroon_bytes = f.read()
	macaroon = codecs.encode(macaroon_bytes, 'hex')

os.environ["GRPC_SSL_CIPHER_SUITES"] = 'HIGH+ECDSA'

cert = open(os.path.expanduser('/Users/paulcote/Downloads/stuff/tls.cert'), 'rb').read()
creds = grpc.ssl_channel_credentials(cert)
channel = grpc.secure_channel('72.137.117.210:10009', creds)
stub = lnrpc.LightningStub(channel)

@app.route('/', methods=['GET', 'POST'])
def form():
    	return render_template('main_page.html')

@app.route('/bitcoin', methods=['GET', 'POST'])
def btc_form():

	return render_template('bitcoin.html')

@app.route('/about', methods=['GET', 'POST'])
def abt_form():

	return render_template('about.html')

@app.route('/shop', methods=['GET', 'POST'])
def shop_form():

	return render_template('shop.html')

@app.route('/how_to', methods=['GET', 'POST'])
def how_to_form():

	return render_template('how_to.html')

@app.route('/result', methods=['GET', 'POST'])
def hello():

	eqn=str(request.form['display'])

	try:
	
		eqn=BEMDAS_algo_v3_prod.main(eqn)

	except:

		err_msg = "There was an error calculating the equation. Please check equation formatting or submit a bug to info@obilisk.app."
		print(err_msg)
		return render_template('error.html', display=err_msg)

	else:

		solution = eqn[0]
		ans = eqn[1]
		ans.insert(0,"The final answer is")

		#finding the last entry in eqn array
		mem_tot=solution[len(solution)-1] # in bytes

		print(mem_tot, "bytes")
		url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

		parameters = {

  			'symbol':'BTC',
  			'convert':'CAD'

		}

		headers = {

  			'Accepts': 'application/json',
  			'X-CMC_PRO_API_KEY': '93dfb645-5ccb-4b27-82ab-7f3599f9e044'

		}

		session = Session()
		session.headers.update(headers)

		try:

			response = session.get(url, params=parameters)
			data = json.loads(response.text)
			satoshi_amt = int(round((10**8)*0.25/data["data"]["BTC"]["quote"]["CAD"]["price"]))

		except (ConnectionError, Timeout, TooManyRedirects) as e:

			print(e)
			satoshi_amt = int(round(mem_tot*0.00007284))

		print(satoshi_amt, "Sats")

		try:

			ln_request = stub.AddInvoice(ln.Invoice(value=satoshi_amt,memo=str(request.form['display'])), metadata=[('macaroon', macaroon)])

		except:

			err_msg = "There was an error communicating with the BTC/LN network. Please contact the administrator at info@obilisk.app."
			print(err_msg)
			return render_template('error.html', display=err_msg)

		else:
			
			ln_response=[]
			ln_response.insert(0,str(ln_request.payment_request))
			ln_response.insert(1,ln_request.r_hash)
			ln_response[1] = codecs.encode(ln_response[1], 'base64')
			ln_response[1] = ln_response[1].decode('utf-8')

			#turning solution into a string format

			sol = ""
	
			for i in range (0,len(solution)-1):

				sol += str(solution[i]) + ";"
		
			#code to write equation, invoice and r_hash to database
			u = User(equation=str(sol), invoice=str(ln_response[0]), r_hash=str(ln_response[1]))
			db.session.add(u)
			db.session.commit()
 
			print(ln_response)

			return render_template('greeting.html', answer=ans, display=ln_response[0])

@app.route('/check', methods=['GET', 'POST'])
def check():

	invo=str(request.form['invoice_text'])

	#code to query database for invoice and r_hash
	u = User.query.filter_by(invoice=invo).first()

	r_hash_base64 = u.r_hash.encode('utf-8')
	r_hash_bytes = codecs.decode(r_hash_base64, 'base64')
	ln_check = stub.LookupInvoice(ln.PaymentHash(r_hash=r_hash_bytes), metadata=[('macaroon', macaroon)])
	print("state: ",ln_check.state)

	if ln_check.state == 0:
	
		return render_template('greeting.html', display=u.invoice)

	else:

		#retransforming solution string into solution array

		solution = []
		db_sol = u.equation
		sol_cnt = 0
		temp=""

		for i in range(0,len(db_sol)):

			if db_sol[i] == ";":

				solution.insert(sol_cnt, temp)
				temp=""
				sol_cnt = sol_cnt+1

			else:

				temp = temp+str(db_sol[i])
				

		return render_template('solution.html', display=solution)

if __name__ == "__main__":
   	app.run(ssl_context=('cert.pem','key.pem'))