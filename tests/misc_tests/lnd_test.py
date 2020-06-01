import rpc_pb2 as ln
import rpc_pb2_grpc as lnrpc
import grpc
import os
import codecs
import psutil
import numpy as np 

#formalities
with open(os.path.expanduser('/Users/paulcote/gocode/dev/alice/data/chain/bitcoin/simnet/admin.macaroon'), 'rb') as f:

	macaroon_bytes = f.read()
	macaroon = codecs.encode(macaroon_bytes, 'hex')

os.environ["GRPC_SSL_CIPHER_SUITES"] = 'HIGH+ECDSA'

cert = open(os.path.expanduser('/Users/paulcote/Library/Application Support/Lnd/tls.cert'), 'rb').read()
creds = grpc.ssl_channel_credentials(cert)
channel = grpc.secure_channel('localhost:10001', creds)
stub = lnrpc.LightningStub(channel)


request = stub.AddInvoice(ln.Invoice(value=125, memo="yeet"), metadata=[('macaroon', macaroon)])
print(request.payment_request)