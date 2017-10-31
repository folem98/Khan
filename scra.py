import urllib2
import json

def Ext_json_data(urlgraph):
    req = urllib2.urlopen(urlgraph)
    data = json.load(req)
    js = open('json1.json','wb')
    js.write(str(data))
    js.close()

print Ext_json_data("https://graph.facebook.com/v2.10/718663534998303?fields=posts&access_token=EAACEdEose0cBALG5J0aTKQIyoRgSfRenqESZBZA8TsKOwnYpgeiajt74RgrzilUCrtXt4ZCnKy2kCdf5xgez8pERXvM4FWnKf3hHaLFIw15TcXAakZBiGOjg6PlHRhZAH5hZBZBs0y1Ha2ntoWJohRqfZAqqPukhvkNU0Ve3ZBGZBWZBjENFLXgMSiEmqiBRlP9TOvTawEkfQbfXgZDZD")