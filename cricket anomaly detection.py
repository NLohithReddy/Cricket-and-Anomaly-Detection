import pandas as pd
from sklearn.ensemble import IsolationForest
import numpy as np

# Load the dataset from CSV
dataset = pd.read_csv('cricket_scores.csv')

# Assuming 'Overs' and 'Runs_Scored' are the columns in your dataset
# Extract the 'Overs' and 'Runs_Scored' columns
overs_scores = dataset[['Overs', 'Runs_Scored']]

# Convert the Pandas DataFrame to a NumPy array
data = overs_scores.to_numpy()

# Create and fit the Isolation Forest model
model = IsolationForest(contamination=0.1)  # Contamination is the expected proportion of anomalies
model.fit(data)

# Predict outliers/anomalies
predictions = model.predict(data)

# Print the predicted outliers (-1 indicates anomaly, 1 indicates normal)
print("Predictions:", predictions)

# Get indices of anomalies
anomaly_indices = np.where(predictions == -1)[0]
print("Anomaly indices:", anomaly_indices)

# Display the anomalies
print("Anomaly data:")
print(data[anomaly_indices])
