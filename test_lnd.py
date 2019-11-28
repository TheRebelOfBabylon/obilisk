import rpc_pb2 as ln
import rpc_pb2_grpc as lnrpc
import grpc
import os
import codecs

with open(os.path.expanduser('/Users/paulcote/Downloads/stuff/admin.macaroon'), 'rb') as f:

	macaroon_bytes = f.read()
	macaroon = codecs.encode(macaroon_bytes, 'hex')

os.environ["GRPC_SSL_CIPHER_SUITES"] = 'HIGH+ECDSA'

cert = open(os.path.expanduser('/Users/paulcote/Downloads/stuff/tls.cert'), 'rb').read()
creds = grpc.ssl_channel_credentials(cert)
channel = grpc.secure_channel('72.137.117.210:10009', creds)
stub = lnrpc.LightningStub(channel)

satoshi_amt=1000

ln_request = stub.AddInvoice(ln.Invoice(value=satoshi_amt,memo="Test"), metadata=[('macaroon', macaroon)])

ln_response=[]
ln_response.insert(0,str(ln_request.payment_request))
ln_response.insert(1,ln_request.r_hash)
ln_response[1] = codecs.encode(ln_response[1], 'base64')
ln_response[1] = ln_response[1].decode('utf-8')

print(ln_response)