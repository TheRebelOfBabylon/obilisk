from flask import Flask, render_template, request

import BEMDAS_algo_v3
import json
import rpc_pb2 as ln
import rpc_pb2_grpc as lnrpc
import grpc
import codecs
import os

with open(os.path.expanduser('/Users/paulcote/gocode/dev/alice/data/chain/bitcoin/simnet/admin.macaroon'), 'rb') as f:

	macaroon_bytes = f.read()
	macaroon = codecs.encode(macaroon_bytes, 'hex')

os.environ["GRPC_SSL_CIPHER_SUITES"] = 'HIGH+ECDSA'

cert = open(os.path.expanduser('/Users/paulcote/Library/Application Support/Lnd/tls.cert'), 'rb').read()
creds = grpc.ssl_channel_credentials(cert)
channel = grpc.secure_channel('localhost:10001', creds)
stub = lnrpc.LightningStub(channel)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    	return render_template('main_page.html')

@app.route('/result', methods=['GET', 'POST'])
def hello():

	eqn=str(request.form['display'])
	eqn=BEMDAS_algo_v3.main(eqn)
	
	mem_tot=eqn[1] # in bytes
	satoshi_amt = round(mem_tot*0.0000103) #current price per byte is 0.0000103 sats/byte
	print(satoshi_amt, "Sats")

	ln_request = stub.AddInvoice(ln.Invoice(value=satoshi_amt, memo=str(request.form['display'])), metadata=[('macaroon', macaroon)])
	ln_response=[]
	ln_response.insert(0,str(ln_request.payment_request))
	print(ln_response)

	return render_template('greeting.html', display=ln_response)

if __name__ == "__main__":
   	app.run(ssl_context=('cert.pem','key.pem'))