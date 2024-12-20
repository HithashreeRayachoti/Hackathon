import pandas as pd
import numpy as np
import re
from sklearn.ensemble import IsolationForest

# Load data into a DataFrame
df = pd.read_csv(r"C:\Users\hitha\Downloads\datasetnet.csv")


# Function to extract features from the 'Info' column
def extract_features(info):
    
    # Extracting flags (ACK, SYN, FIN)
    flag = 0
    if '[ACK]' in info:
        flag = 1
    elif '[SYN]' in info:
        flag = 2
    elif '[FIN]' in info:
        flag = 3
    
    # Extracting sequence and acknowledgment numbers
    seq_match = re.search(r'Seq=(\d+)', info)
    ack_match = re.search(r'Ack=(\d+)', info)
    seq_num = int(seq_match.group(1)) if seq_match else 0
    ack_num = int(ack_match.group(1)) if ack_match else 0
    
    # Extracting window size and length
    win_match = re.search(r'Win=(\d+)', info)
    len_match = re.search(r'Len=(\d+)', info)
    window_size = int(win_match.group(1)) if win_match else 0
    length = int(len_match.group(1)) if len_match else 0
    
    return [flag, seq_num, ack_num, window_size, length]

# Apply the extraction function to the 'Info' column
features = df['Info'].apply(extract_features)

# Create a new DataFrame with the extracted features
features_df = pd.DataFrame(features.tolist(), columns=[
    'Flag', 'Seq_Num', 'Ack_Num', 'Window_Size', 'Payload'
])

# Combine the features with the original DataFrame
df = pd.concat([df, features_df], axis=1)

# Display the final DataFrame
#print(df)
print(df)


data= df[['Length']]
# Initialize IsolationForest
iso_forest = IsolationForest(contamination=0.01)  # Contamination is the expected proportion of anomalies

# Fit the model
iso_forest.fit(data)
# Predict anomalies
predictions = iso_forest.predict(data)

# Add predictions as a new column in the DataFrame
df['Anomaly_len'] = predictions
# Filter and view rows that are anomalies
anomalies = df[df['Anomaly_len'] == -1]
print(anomalies)
import matplotlib.pyplot as plt

# Plot anomalies: Anomalies (-1) in red, Normal (1) in blue
plt.figure(figsize=(10, 4))
df_head=df.head(1000)
# Plotting normal points
plt.scatter(df_head[df_head['Anomaly_len'] == 1]['No.'], df_head[df_head['Anomaly_len'] == 1]['Length'], color='blue', label='Normal',linestyle='-', alpha=0.6)

# Plotting anomalies
plt.scatter(df_head[df_head['Anomaly_len'] == -1]['No.'], df_head[df_head['Anomaly_len'] == -1]['Length'], color='red', label='Anomaly', alpha=0.6)

# Labels and title
plt.title("Network Traffic Anomaly Detection")
plt.xlabel("Packet No.")
plt.ylabel("Length")
plt.legend()

# Show the plot
plt.show()
# Step 1: Round the 'Time' column to the nearest second
df['second'] = df['Time'].apply(lambda x: int(x))

# Step 2: Count the number of packets per second
packet_count_per_second = df.groupby('second')['No.'].count()

# Step 3: Calculate frequency (1 / count of packets per second)
df['freq'] = df['second'].map(lambda x: packet_count_per_second[x])

df.tail()
data2= df[['freq','Length']]
# Initialize IsolationForest
iso_forest = IsolationForest(contamination=0.01)  # Contamination is the expected proportion of anomalies

# Fit the model
iso_forest.fit(data2)
# Predict anomalies
predictions2 = iso_forest.predict(data2)

# Add predictions as a new column in the DataFrame
df['Anomaly_freq'] = predictions2
anomalies2 = df[df['Anomaly_freq'] == -1]
print(anomalies2)
plt.figure(figsize=(10, 4))
df_head=df.head(1000)
# Plotting normal points
plt.scatter(df_head[df_head['Anomaly_freq'] == 1]['No.'], df_head[df_head['Anomaly_freq'] == 1]['Length'], color='blue', label='Normal',linestyle='-', alpha=0.6)

# Plotting anomalies
plt.scatter(df_head[df_head['Anomaly_freq'] == -1]['No.'], df_head[df_head['Anomaly_freq'] == -1]['Length'], color='red', label='Anomaly', alpha=0.6)

# Labels and title
plt.title("Network Traffic Anomaly Detection")
plt.xlabel("Packet No.")
plt.ylabel("Length")
plt.legend()

# Show the plot
plt.show()
anomalous_ips = [
    "127.0.0.1", "169.254.1.1", "224.0.0.1", "192.168.1.255", 
    "192.168.1.0", "192.0.2.1", "240.0.0.1", "0.0.0.0", "255.255.255.255"
]

# Create 'ip_anomaly' column where Source or Destination IP is in the anomalous IP list
df['Anomaly_ip'] = df['Source'].isin(anomalous_ips) 

# Display the DataFrame
print(df)
df['Anomaly_final'] = df.apply(lambda row: 1 if row['Anomaly_ip'] == True or row['Anomaly_freq'] == -1 else 0, axis=1)

# Display the DataFrame
print(df)
plt.figure(figsize=(10, 4))
df_head=df.head(1000)
# Plotting normal points
plt.scatter(df_head[df_head['Anomaly_final'] == 0]['No.'], df_head[df_head['Anomaly_final'] == 0]['Length'], color='blue', label='Normal',linestyle='-', alpha=0.6)

# Plotting anomalies
plt.scatter(df_head[df_head['Anomaly_final'] == 1]['No.'], df_head[df_head['Anomaly_final'] == 1]['Length'], color='red', label='Anomaly', alpha=0.6)

# Labels and title
plt.title("Network Traffic Anomaly Detection")
plt.xlabel("Packet No.")
plt.ylabel("Length")
plt.legend()

# Show the plot
plt.show()
# Save the DataFrame to a CSV file
df.to_csv('C:\\Users\\admin\\Downloads\\Real-Time Network Traffic Anomaly Detection and Mitigation\\network_traffic_Test.csv', index=False)
