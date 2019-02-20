import pandas as pd
import datetime as dt
import requests
import time
import random
import json
import os

os.path

df = pd.read_csv(os.path.dirname(os.path.realpath(__file__)) + '/dataset.csv', usecols=[
    'Time', 'Device Address',
    'Flow(Category 1)', 'Flow(Category 2)', 'Flow(Category 3)',
    'Speed(Lane 1)', 'Speed(Lane 2)', 'Speed(Lane 3)'
], na_values=-1)

df['Time'] = pd.to_datetime(df['Time'])
df['Flow'] = df[['Flow(Category 1)', 'Flow(Category 2)', 'Flow(Category 3)']].sum(axis=1)
df['Speed'] = df[['Speed(Lane 1)', 'Speed(Lane 2)', 'Speed(Lane 3)']].mean(axis=1)
df['Pedestrians'] = (df['Flow']/10).round().astype(int)

df2 = df[['Time', 'Device Address', 'Flow', 'Speed', 'Pedestrians']].groupby(['Time', 'Device Address']).sum().unstack().fillna(0)

df3 = pd.DataFrame({
    'Vehicles': df2['Flow'][312],
    'Pedestrians': df2['Pedestrians'][312]
})

while True:

    for i, row in df3.iterrows():

        data = {
            'numberOfCars': int(row['Vehicles']),
            'numberOfFaces': int(row['Pedestrians']),
            'faceDetectionWeight': random.random(),
            'carDetectionWeight': random.random()
        }

        requests.post('http://172.20.0.2:8080/traffic_img_proc/action.dn', data={'json': json.dumps(data)})

        print(data)

        time.sleep(0.2)
