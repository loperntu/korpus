#-*-coding:utf8-*-
#驗證PTT
import urllib2, base64

class PreemptiveBasicAuthHandler(urllib2.HTTPBasicAuthHandler):
    def http_request(self, req):
        url = req.get_full_url()
        realm = None
        user, pw = self.passwd.find_user_password(realm, url)
        if pw:
            raw = "%s:%s" % (user, pw)
            auth = 'Basic %s' % base64.b64encode(raw).strip()
            req.add_unredirected_header(self.auth_header, auth)
        return req

    https_request = http_request

api_url = "http://lopen.linguistics.ntu.edu.tw/PTT/api/"
username = "aberlope"
password = "aberlope2014"

auth_handler = PreemptiveBasicAuthHandler()
auth_handler.add_password(realm=None, uri=api_url, user=username, passwd=password)
opener = urllib2.build_opener(auth_handler)
urllib2.install_opener(opener)


from bosonnlp import BosonNLP
import json

# 驗證boson
nlp = BosonNLP('eUFC3Asa.2489.XKcPdOpVomie')

# Getting all the posts from joke (就可版) from 2014-01-01 to 2014-02-01
joke = urllib2.urlopen('http://lopen.linguistics.ntu.edu.tw/PTT/api/article/joke/from/2014-01-01/to/2014-02-01').read()
joke = json.loads(joke)


testdata = joke[603]['content'].split('\n')

# Sentiment analysis
print '\n[測試資料]\n----------'
for i in testdata:
    print i
print '----------'

print 'Sentiment analysis\n----------'
for i in testdata:
    print i, nlp.sentiment(i)

## 命名實體識別 NER
# 時間，地點，人民，組織，公司，產品

print '\n[命名實體識別]\n-----
for i in testdata:
    print i, nlp.ner(i)
