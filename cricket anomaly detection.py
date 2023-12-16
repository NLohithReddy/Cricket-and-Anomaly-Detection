import pandas as pd
from sklearn.ensemble import IsolationForest
import numpy as np
dataset = pd.read_csv('cricket_scores.csv')
overs_scores = dataset[['Overs', 'Runs_Scored']]
data = overs_scores.to_numpy()
model = IsolationForest(contamination=0.1)  
model.fit(data)
predictions = model.predict(data)
print("Predictions:", predictions)
anomaly_indices = np.where(predictions == -1)[0]
print("Anomaly indices:", anomaly_indices)
print("Anomaly data:")
print(data[anomaly_indices])
