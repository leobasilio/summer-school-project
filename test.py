import requests
 
data = {
    'numberOfCars': 'a',
    'numberOfFaces': 'b',
    'faceDetectionWeight':3,
    'carDetectionWeight': 3
}

requests.post('http://localhost', json=data)
