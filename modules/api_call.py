#!/usr/bin/python
import hashlib, hmac, requests, datetime

class ApiCall():

    def __init__(self, base_url, endpoint, auth_tokens, request_parameters):
        self.base_url = base_url
        self.endpoint = endpoint
        self.params = auth_tokens
        self.date_time = self.get_today_date_time_format()
        self.hmac = self.get_hmac()
        self.parse_request_parameters(request_parameters)
        self.payload = self.build_authentication()

    def call(self):
        return requests.get(self.base_url + self.endpoint, headers = self.payload, verify=False).json()

    def build_authentication(self):
        return {
            'DTAPI-Token': self.params['public_key'],
            'DTAPI-Date': self.date_time,
            'DTAPI-Signature': self.hmac.hexdigest()
        }

    def get_today_date_time_format(self):
        return datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%S')

    def get_hmac(self):
        return hmac.new(self.params['private_key'], self.endpoint + "\n" + self.params['public_key'] + "\n" +
                        self.date_time, hashlib.sha1)

    def parse_request_parameters(self, request_parameters):
        return_val = '?'

        for parameter in request_parameters:
            return_val += '='.join((str(parameter), str(request_parameters[parameter]))) + '&'

        if len(return_val) > 0:
            return_val = return_val[:-1]

        return return_val