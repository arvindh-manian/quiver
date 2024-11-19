from flask import Flask, jsonify, send_file

from dao import fetch_file

app = Flask(__name__)

@app.route("/healthz")
def healthz():
    return jsonify({"status": "healthy"})

@app.route("/hls/<route>", methods=['GET'])
def fetch_m3a8(route):
    file = fetch_file(route)
    return file

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 