import numpy as np
import pandas as pd
from sklearn import preprocessing
import scipy.stats as stats

data = pd.read_csv("heart_disease_patients.csv")
print(data)
variabel = ('age','trestbps','chol','thalach','oldpeak')
dataMiss = data.isna().sum()

print(dataMiss)

data = data.dropna()

print(data)
data = data[(np.abs(stats.zscore(data)) < 3).all(axis=1)]

outliers = []
def detect_outlier(data):

    threshold = 3
    mean_1 = np.mean(data)
    std_1 = np.std(data)

    for y in data:
        z_score= (y - mean_1)/std_1
        if np.abs(z_score) > threshold:
            outliers.append(y)
    return outliers

for var in variabel:
    outlier_datapoints = detect_outlier(data[var])
    print("Outlier ", var, " = ", outlier_datapoints)

print()
z_scores = stats.zscore(data)
abs_z_scores = np.abs(z_scores)
filtered_entries = (abs_z_scores < 3).all(axis=1)
new_data = data[filtered_entries]

print(new_data)
print(data.isna().sum())
# Baca Data
df = pd.DataFrame(data)
print(df)

# Normalisasi data
min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(df)
df_normalized = pd.DataFrame(np_scaled)

# Pembacaan data setelah dinormalisasi
print("\nData hasil normalisasi:\n", df_normalized)
