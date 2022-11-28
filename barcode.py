import os
from flask import Flask, request
from pyzbar import pyzbar
import pdf2image
import json
from cfenv import AppEnv

env = AppEnv()

app = Flask(__name__)
# port = int(os.environ.get('PORT', 3000))
port = 3333

@app.route('/')
def hello():
    return f"Hello World ({env.name}, {env.port})"

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