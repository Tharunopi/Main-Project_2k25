from flask import Flask, request, jsonify
import streamlit as st
app = Flask(__name__)

li = []
@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.json
    print("📥 Received Data:", data)
    li.append(data["distance_history"])
    return jsonify({"status": "success", "message": "Data received!"})

@app.route('/get_all_data', methods=['GET'])
def get_all_data():
    return jsonify({"status": "success", "data": li})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

