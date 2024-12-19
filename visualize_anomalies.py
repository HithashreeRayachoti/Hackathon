import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest

# Step 1: Generate sample data
data = [
    {"timestamp": i, "packet_size": random.randint(50, 150), "anomaly": 0}
    for i in range(100)
]
# Add some anomalies (outliers in the data)
data[20]["packet_size"] = 300  # Anomalous point
data[20]["anomaly"] = 1
data[85]["packet_size"] = 5    # Another anomaly
data[85]["anomaly"] = 1

# Step 2: Convert to a DataFrame for easier handling
df = pd.DataFrame(data)

# Step 3: Use IsolationForest to detect anomalies
X = df[["packet_size", "timestamp"]]
clf = IsolationForest(contamination=0.05, random_state=42)
df["isolation_forest"] = clf.fit_predict(X)

# Mark anomalies detected by IsolationForest
df["isolation_forest_anomaly"] = df["isolation_forest"].apply(lambda x: 1 if x == -1 else 0)

# Step 4: Visualize traffic patterns
plt.figure(figsize=(10, 6))
sns.lineplot(x=df["timestamp"], y=df["packet_size"], label="Normal Traffic", color="blue")

# Highlight anomalies detected by IsolationForest
anomaly_points = df[df["isolation_forest_anomaly"] == 1]
plt.scatter(
    anomaly_points["timestamp"],
    anomaly_points["packet_size"],
    color="orange",
    label="IsolationForest Anomaly",
    s=100,
)

plt.title("Traffic Patterns with IsolationForest Anomalies")
plt.xlabel("Timestamp")
plt.ylabel("Packet Size")
plt.legend()
plt.show()
