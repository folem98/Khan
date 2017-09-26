import urllib2
import json

def Ext_json_data(urlgraph):
    req = urllib2.urlopen(urlgraph)
    data = json.load(req)
    js = open('json.json','wb')
    js.write(str(data))
    js.close()

print Ext_json_data("https://graph.facebook.com/v2.10/718663534998303?fields=posts&access_token=EAACEdEose0cBAM1u1QmSMsE8WTKKufIXTVkuHQy0dJQhsvZBzZBCZBJM4JKJY2E98SwK2DKZCBZAi7ZCKsLlwu82sVBHT8C7IfZBLRq0xAyUNgKROBHRdSFn6IxAEqairoL1STed8P6Pnm05qr3FwZCFjy6z1G2OoMJRYBcXfXZBKvqjkyEit8K7dkZCu0piWART8ZD")