from app import app, db
from app.models import User
from flask import Flask, render_template, request

import BEMDAS_algo_v3
import json
import rpc_pb2 as ln
import rpc_pb2_grpc as lnrpc
import grpc
import codecs
import os

with open(os.path.expanduser('/Users/paulcote/Downloads/admin.macaroon'), 'rb') as f:

	macaroon_bytes = f.read()
	macaroon = codecs.encode(macaroon_bytes, 'hex')

os.environ["GRPC_SSL_CIPHER_SUITES"] = 'HIGH+ECDSA'

cert = open(os.path.expanduser('/Users/paulcote/Downloads/tls.cert'), 'rb').read()
creds = grpc.ssl_channel_credentials(cert)
channel = grpc.secure_channel('72.137.117.210:10009', creds)
stub = lnrpc.LightningStub(channel)

@app.route('/', methods=['GET', 'POST'])
def form():
    	return render_template('main_page.html')

@app.route('/result', methods=['GET', 'POST'])
def hello():

	eqn=str(request.form['display'])
	eqn=BEMDAS_algo_v3.main(eqn)

	#finding the last entry in eqn array
	mem_tot=eqn[len(eqn)-1] # in bytes

	print(mem_tot, "bytes")
	satoshi_amt = round(mem_tot*0.00007284) #current price per byte is 0.00007284 sats/byte
	print(satoshi_amt, "Sats")

	ln_request = stub.AddInvoice(ln.Invoice(value=satoshi_amt, memo=str(request.form['display'])), metadata=[('macaroon', macaroon)])
	ln_response=[]
	ln_response.insert(0,str(ln_request.payment_request))
	ln_response.insert(1,ln_request.r_hash)
	ln_response[1] = codecs.encode(ln_response[1], 'base64')
	ln_response[1] = ln_response[1].decode('utf-8')

	#turning solution into a string format

	solution = ""
	
	for i in range (0,len(eqn)-1):

		solution = solution + eqn[i] + ";"
		

	#code to write equation, invoice and r_hash to database
	u = User(equation=str(solution), invoice=str(ln_response[0]), r_hash=str(ln_response[1]))
	db.session.add(u)
	db.session.commit()
 
	print(ln_response)

	return render_template('greeting.html', display=ln_response[0])

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