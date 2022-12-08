import http.client, urllib.request, urllib.parse, urllib.error, base64
from datetime import datetime


class AT:

    def __init__(self, thisKey = None) -> None:
        self.key = thisKey

    def getDate():
        return datetime.now().date()



    def all_stops(self,date = getDate()):
        """Must pass in date as YYYY-MM-DD"""


        headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': f'{self.key}',
        }

        params = urllib.parse.urlencode({
            # Request parameters
            'filter[date]': f'{date}',
            # YYYY-MM-DD
        })

        try:
            conn = http.client.HTTPSConnection('api.at.govt.nz')
            conn.request("GET", "/gtfs/v3/stops?%s" % params, "{body}", headers)
            response = conn.getresponse()
            data = response.read()
            # print(data)
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))

        return data
    
    def route(self,route_type = 2):
        """
        1 = tram
        2 = subway
        3 = buss
        4 = ferry
        5 + is Relevant in nz
        """

        headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': f'{self.key}',
        }

        params = urllib.parse.urlencode({
            # Request parameters
            'filter[route_type]': route_type,
        })

        try:
            conn = http.client.HTTPSConnection('api.at.govt.nz')
            conn.request("GET", "/gtfs/v3/routes?%s" % params, "{body}", headers)
            response = conn.getresponse()
            data = response.read()
            # print(data)
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
        
        return data
    
    def stop_by_id(self,id):
        
        headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': f'{self.key}',
        }

        params = urllib.parse.urlencode({
        })

        try:
            conn = http.client.HTTPSConnection('api.at.govt.nz')
            conn.request("GET", f"/gtfs/v3/stops/{id}?%s" % params, "{body}", headers)
            response = conn.getresponse()
            data = response.read()
            # print(data)
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))

        return data


    def combined_data(self):

        headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': f'{self.key}',
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

    def stops_by_trip_id(self,trip_id):

        headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': f'{self.key}',
        }

        params = urllib.parse.urlencode({
        })

        try:
            conn = http.client.HTTPSConnection('api.at.govt.nz')
            conn.request("GET", "/gtfs/v3/trips/{id}/stops?%s" % params, "{body}", headers)
            response = conn.getresponse()
            data = response.read()
            print(data)
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))

        return data


a = AT("ddd5f1e9f37a4521912acb647024c7b1")
print(a.stops_by_trip_id('1033-32504-52500-2-d16dbfbd'))
