from flask import Flask, jsonify, send_file, request

from dao import fetch_file
import logging
import os

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

if not os.path.exists('/app/cache'):
    os.makedirs('/app/cache')

# Configure logging
# logging.basicConfig(filename='/app/access.log', level=logging.INFO, 
#                     format='%(asctime)s %(levelname)s %(message)s',
#                     filemode='w+')


@app.route("/healthz")
def healthz():
    return jsonify({"status": "healthy"})

@app.route("/hls/<path:route>", methods=['GET'])
def fetch_m3a8(route):
    # Log the access    
    file = fetch_file(app, route)
    return file

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)