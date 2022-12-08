import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'ddd5f1e9f37a4521912acb647024c7b1',
}

params = urllib.parse.urlencode({
    # Request parameters
    'filter[date]': '2022-12-08',
    # YYYY-MM-DD
})

try:
    conn = http.client.HTTPSConnection('api.at.govt.nz')
    conn.request("GET", "/gtfs/v3/stops?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))


f = open("all_stops.json", "w")
f.write(str(data))