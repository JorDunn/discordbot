import json

class Config(object):
    token           = None
    default_channel = None

    def __init__(self, filename):
        fp = open(filename)
        contents = json.load(fp)
        self.token = contents['token']
        self.default_channel = contents['default_channel']
