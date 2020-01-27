import requests
import json

def POST():
    url = "https://api-auth.prod.birdapp.com/api/v1/auth/email"
    body = {"email":"birdscanner@armyspy.com"}
    headers = {
    "User-Agent":"Bird/4.53.0 (co.bird.Ride; build:24; iOS 12.4.1) Alamofire/4.53.0",
    "Device-Id":"92737878-4382-4A41-9366-5524D3518CEC",
    "Platform":"ios",
    "App-Version":"4.53.0",
    "Content-Type":"application/json"
    }
    rp = requests.post(url, data=json.dumps(body), headers=headers)
    print(rp.content)

POST()
