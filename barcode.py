import os
from flask import Flask, request, jsonify
from pyzbar import pyzbar
import pdf2image
import json
from cfenv import AppEnv
from sap import xssec

env = AppEnv()
uaa_service = env.get_service(name='barcode-docker-xsuaa').credentials

app = Flask(__name__)
# port = int(os.environ.get('PORT', 3000))
port = 3333

@app.route('/')
def hello():

	auth_header = request.headers.get('Authorization')

	if not auth_header:
		return "Errore: nessun header autorizzativo!", 403

	auth_token = auth_header.split(" ")[1]
	security_context = xssec.create_security_context(auth_token, uaa_service)

	isAuthorized = security_context.check_scope(f"{uaa_service['xsappname']}.read")

	return f"Benvenuto {security_context.get_logon_name()}, {isAuthorized}"

@app.route("/barcode", methods=['POST'])
def barcode():
	images = pdf2image.convert_from_bytes(
		request.get_data(),
		dpi=400,
		first_page=1,
		last_page=1,
		grayscale=True
	)
	decoded = pyzbar.decode(images[0])
	
	ret = []
	for item in decoded:
		ret.append({
			"value": item.data.decode("utf-8")
		})

	return json.dumps({"values": ret})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)