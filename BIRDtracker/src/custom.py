import requests, json

def Post3(_url, _body, _headers):
    rp = requests.post(_url, data=json.dumps(_body), headers=_headers)
    print(rp.content)
    print("")
def Post2(_url, _body):
    rp = requests.post(_url, data=json.dumps(_body))
    print(rp.content)
    print("")
def GET(_url,  _headers):
    rg = requests.get(_url, headers=_headers)
    print(rg.content)
    print("")