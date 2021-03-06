from flask import Flask, request,jsonify


app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
