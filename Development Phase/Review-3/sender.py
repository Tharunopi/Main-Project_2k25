import requests
server_url = "http://127.0.0.1:5001/receive_data"

for i in range(1, 100):
    data_to_send = {
    "distance_history": i+1,
    "pixel_distance_history": i+2
    }
    response = requests.post(server_url, json=data_to_send)
    print(response.json())


