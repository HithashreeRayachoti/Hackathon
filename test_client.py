import requests
import random
import time

# Generate mock data
mock_data = [
    {"packet_size": random.randint(50, 1500), "timestamp": time.time() + i}
    for i in range(100)
]

# API URL
url = "http://127.0.0.1:5000/detect_anomalies"

# Send POST request
response = requests.post(url, json=mock_data)

# Print response
print(response.json())
