email = input("Email: ")
token = input("Token: ")

def con1():
    email = input("Email: ")
    url = "https://api-auth.prod.birdapp.com/api/v1/auth/email"
    body = {"email": email}
    headers = {
    "User-Agent":"Bird/4.53.0 (co.bird.Ride; build:24; iOS 12.4.1) Alamofire/4.53.0",
    "Device-Id":"92737878-4382-4A41-9366-5524D3518CEC",
    "Platform":"ios",
    "App-Version":"4.53.0",
    "Content-Type":"application/json"
    }

def con2():
    token = input("Token: ")
    url = "https://api-auth.prod.birdapp.com/api/v1/auth/magic-link/use"
    headers = {
    "User-Agent":"Bird/4.53.0 (co.bird.Ride; build:24; iOS 12.4.1) Alamofire/4.53.0",
    "Device-Id":"92737878-4382-4A41-9366-5524D3518CEC",
    "Platform":"ios",
    "App-Version":"4.53.0",
    "Content-Type":"application/json"
    }
    body = {"token":token}