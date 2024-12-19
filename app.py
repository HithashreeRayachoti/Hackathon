from flask import Flask, request, jsonify
from isolation_forest import isolation_forest_anomaly_detection

app = Flask(__name__)

@app.route('/detect_anomalies', methods=['POST'])
def detect_anomalies():
    # Parse incoming JSON data
    traffic_data = request.json
    
    # Call the Isolation Forest function
    anomalies = isolation_forest_anomaly_detection(traffic_data)
    
    return jsonify({"anomalies": anomalies})

if __name__ == '__main__':
    app.run(debug=True)
