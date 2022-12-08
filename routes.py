import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'ddd5f1e9f37a4521912acb647024c7b1',
}

params = urllib.parse.urlencode({
    # Request parameters
    'filter[route_type]': 3,
})

try:
    conn = http.client.HTTPSConnection('api.at.govt.nz')
    conn.request("GET", "/gtfs/v3/routes?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

f = open("routes.json", "w")
f.write(str(data))