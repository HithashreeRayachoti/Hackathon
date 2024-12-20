from fastapi import FastAPI
from pydantic import BaseModel
from data import *
from typing import List

app = FastAPI()

# Define a Pydantic model for the request body
class TrafficData(BaseModel):
    data: List[List[float]]  # Assuming traffic_data is a list of lists (you can adjust the type as needed)

# Define a Pydantic model for the response body
class AnomalyResponse(BaseModel):
    anomalies: List[int]  # Assuming anomalies is a list of indices or boolean flags

@app.post("127.0.0.1/api/analyze", response_model=AnomalyResponse)
async def detect_anomalies(traffic_data: TrafficData):
    # Call the Isolation Forest function
    anomalies = iso_forest(traffic_data.data)
    
    # Return the anomalies in the response format
    return AnomalyResponse(anomalies=anomalies)
import uvicorn
uvicorn.run(app, host="0.0.0.0", port=8000)
# To run the app, you would use: uvicorn <filename>:app --reload