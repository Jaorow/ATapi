import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '372f00b7bafd40c0a89eda57d9bd3ed6',
}

params = urllib.parse.urlencode({
    # Request parameters
    'callback': '{string}',
    'tripid': '{string}',
    'vehicleid': '{string}',
})

try:
    conn = http.client.HTTPSConnection('api.at.govt.nz')
    conn.request("GET", "/realtime/legacy/?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
