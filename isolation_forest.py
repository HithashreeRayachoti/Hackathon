from sklearn.ensemble import IsolationForest




def isolation_forest_anomaly_detection(data):
    # Prepare the data for the model
    X = [[d['packet_size'], d['timestamp']] for d in data]
    
    # Initialize the Isolation Forest model
    clf = IsolationForest(contamination=0.01, random_state=42)  # Adjust contamination rate
    
    # Fit the model to the data
    clf.fit(X)
    
    # Predict anomalies (-1 = anomaly, 1 = normal)
    predictions = clf.predict(X)
    
    # Extract anomalies based on predictions
    anomalies = [data[i] for i, pred in enumerate(predictions) if pred == -1]
    
    return anomalies
