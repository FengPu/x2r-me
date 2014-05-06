import requests
def testUri(uri):
    status = ""
    test = ""
    try:
        status = requests.get(uri).status_code 
    except:
        status = "except" 
    if str(status) == "200" or str(status) == "303":
        test = "1"
    else:
        test = "0"
    return test

print testUri("http://www.google.com"), type(testUri("http://www.google.com"))
print testUri("http://jpp.no-ip.org")
print testUri("http://jpp.on-ip.orgrt")
