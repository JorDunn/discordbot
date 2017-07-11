import json

class Config(object):
    token           = None
    default_channel = None

    def __init__(self, filename):
        fp = open(filename)
        contents = json.load(fp)
        self.token = contents['token']
        self.default_channel = contents['default_channel']
        self.client_id = ['client_id']

    def get_token(self):
        return self.token

    def get_default_channel(self):
        return self.default_channel

    def get_client_id(self):
        return self.client_id
