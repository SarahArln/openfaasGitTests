import requests
import json
from print0 import print0

p = print0('33')

def handle(req):
    listener_ip = '10.0.0.123'
    database_ip = '10.0.0.123'
    openfaas_ip = 'http://10.0.0.123:31112/function/openfaas'
    data = {
        "ip": listener_ip,
        "device": "magician",
        "method": "suck on",
        "user": "siemens",
        "pwd": "siemens"
    }
    response1 = requests.get(url=openfaas_ip, data=json.dumps(data))
    data = {
        "ip": listener_ip,
        "device": "magician",
        "method": "suck off",
        "user": "siemens",
        "pwd": "siemens"
    }
    response2 = requests.get(url=openfaas_ip, data=json.dumps(data))


    return response1.text + '\n' + response2.text + '\n' + p.simple('236')