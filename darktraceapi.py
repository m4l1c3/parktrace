import os
from modules.api_call import ApiCall

base_url = os.environ['darktraceapibaseurl']

params = {
    'private_key': os.environ['darktraceprivate'],
    'public_key': os.environ['darktracepublic']
}

metrics = ApiCall(base_url, '/metrics', params, {"cid": 1})
response = metrics.call()

model_breaches_options = {
    "fulldevicedetails": "true",
    "expandenums": "true",
    "includebreachurl": "true"
}

model_breaches = ApiCall(base_url, '/modelbreaches', params, model_breaches_options).call()
# breaches = model_breaches.call()

string = 'butt'
