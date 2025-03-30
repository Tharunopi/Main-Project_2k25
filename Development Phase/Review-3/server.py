from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.json
    print("📥 Received Data:", data)
    return jsonify({"status": "success", "message": "Data received!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
