import json
from urllib2 import Request
def test(page_id,access_token):
    base = "https://graph.facebook.com/v2.4"
    node = "/"+page_id+"/feed"
    parameters = "/?access_token=%s" % access_token
    url = base+node+parameters
    data = json.loads(request_until_succeed(url))
    print json.dumps(data, indent=4, sort_keys=True)

test("718663534998303","EAACEdEose0cBAHH9BiQbHbZB2MPMVy3E6RcKkwFuoentPb0ZAnjkaGVnmCWHtQg4k1RbLYsT1y0Yj59JDuvkd8A0kluZAeGchVhTxvHpzV2HYdF1ib6GCAcZByb3mQCnZB4h1c6P5O9I82V0pjnkB00XviQvgH6laR2ZCGklTAyZBUnl7HOdbNroZB36VCvgbMboZBVo7ZB4ayMwZDZD")