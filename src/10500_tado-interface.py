# coding: iso-8859-15

import urllib
import urllib2
import ssl
import json
import time

##!!!!##################################################################################################
#### Own written code can be placed above this commentblock . Do not change or delete commentblock! ####
########################################################################################################
##** Code created by generator - DO NOT CHANGE! **##

class Tado_interface10500(hsl20_4.BaseModule):

    def __init__(self, homeserver_context):
        hsl20_4.BaseModule.__init__(self, homeserver_context, "tado_interface")
        self.FRAMEWORK = self._get_framework()
        self.LOGGER = self._get_logger(hsl20_4.LOGGING_NONE,())
        self.PIN_I_TRIGGER=1
        self.PIN_I_EMAIL=2
        self.PIN_I_PASSWORD=3
        self.PIN_I_ZONE_1=4
        self.PIN_I_TARGET=5
        self.PIN_O_EXCEPTION=1
        self.PIN_O_ACTUAL_1=2
        self.PIN_O_TARGET_1=3
        self.PIN_O_HUMIDITY_1=4
        self.PIN_O_DEBUG_1=5
        self.PIN_O_DEBUG_2=6
        self.PIN_O_DEBUG_3=7
        self.PIN_O_DEBUG_4=8
        self.PIN_O_DEBUG_5=9
        self.PIN_O_DEBUG_6=10
        self.PIN_O_DEBUG_7=11
        self.PIN_O_DEBUG_8=12
        self.PIN_O_DEBUG_9=13
        self.PIN_O_DEBUG_10=14

########################################################################################################
#### Own written code can be placed after this commentblock . Do not change or delete commentblock! ####
###################################################################################################!!!##

    def on_init(self):
        self.access_token = None
        self.refresh_token = None
        self.expires_at = None
        self.home_id = None
        self.zone_names = {}
        self.tado_id_to_zone_id = {}

    def on_input_value(self, index, value):
        if index == self.PIN_I_TRIGGER:
            self.get_current_state()
        elif index in [self.PIN_I_EMAIL, self.PIN_I_PASSWORD]:
            pass
        elif index == self.PIN_I_ZONE_1:
            self.zone_names[value] = 1
            try:
                self.update_zones()
            except:
                pass
        elif index == self.PIN_I_TARGET:
            self.set_zone(1, value)
        pass

    def set_zone(self, zone_id, temperature):
        tado_id = list(self.tado_id_to_zone_id.keys())[list(self.tado_id_to_zone_id.values()).index(zone_id)]

        if not self.home_id:
            self.get_home_id()
        
        payload = {
        	"termination": {
        		"typeSkillBasedApp": "NEXT_TIME_BLOCK"
        	},
        	"setting":{
        		"type": "HEATING",
        		"power": "ON",
        		"temperature": {
        			"celsius": temperature
        			},
                "isBoost":False
            }
        }
        [response, status] = self.fetch("https://my.tado.com/api/v2/homes/" + str(self.home_id) + "/zones/" + str(tado_id) + "/overlay?ngsw-bypass=true", method="PUT", body=payload, bodyType="JSON", access_token=self.access_token)
        if status != 200:
            self._set_output_value(self.PIN_O_EXCEPTION, 6)
            raise Exception("Error setting target temperature")

    def update_zones(self):
        self.validate_access_token()

        if not self.home_id:
            self.get_home_id()
        
        [zones, status] = self.fetch("https://my.tado.com/api/v2/homes/" + str(self.home_id) + "/zones?ngsw-bypass=true", method="GET", access_token=self.access_token)
        if status != 200:
            self._set_output_value(self.PIN_O_EXCEPTION, 3)
            raise Exception("Error retrieving zones information")
        
        for i in range(len(zones)):
                if zones[i]["name"] in self.zone_names:
                    self.tado_id_to_zone_id[zones[i]["id"]] = self.zone_names[zones[i]["name"]]

    def get_home_id(self):
        self.validate_access_token()

        [me, status] = self.fetch("https://my.tado.com/api/v2/me", method="GET", access_token=self.access_token)
        if status != 200:
            raise Exception("Error retrieving user information")
        
        self.home_id = me["homes"][0]["id"]

    def validate_access_token(self):
        if self.access_token == None:
            self.get_access_token()
        if self.expires_at <= time.time():
            self.refresh_access_token()
    
    def get_current_state(self):
        try:
            self.validate_access_token()

            if not self.home_id:
                self.get_home_id()

            [zoneStates, status] = self.fetch("https://my.tado.com/api/v2/homes/" + str(self.home_id) + "/zoneStates", method="GET", access_token=self.access_token)

            if status != 200:
                self._set_output_value(self.PIN_O_EXCEPTION, 2)
                raise Exception("Error retrieving zone states")
            
            zoneStates = zoneStates["zoneStates"]
            for tado_id in self.tado_id_to_zone_id:
                zone_id = self.tado_id_to_zone_id[tado_id]
                current_zone = zoneStates[str(tado_id)]
                actual = current_zone["sensorDataPoints"]["insideTemperature"]["celsius"]
                target = current_zone["setting"]["temperature"]["celsius"]
                humidity = current_zone["sensorDataPoints"]["humidity"]["percentage"]

                if zone_id == 1:
                    self.set_output_zone_states(self.PIN_O_ACTUAL_1, actual, target, humidity)

        except:
            pass
    
    def set_output_zone_states(self, zone_actual_pin_id, actual, target, humidity):
        self._set_output_value(zone_actual_pin_id, actual)
        self._set_output_value(zone_actual_pin_id + 1, target)
        self._set_output_value(zone_actual_pin_id + 2, humidity)

    def refresh_access_token(self):
        if self.refresh_token == None:
            self.get_access_token()
        
        payload = {
    	    "client_id": "tado-web-app",
    	    "client_secret": "wZaRN7rpjn3FoNyF5IFuxg9uMzYJcvOoQ8QWiIqS3hfk6gLhVlG57j5YNoZL2Rtc",
	        "grant_type": "refresh_token"
        }
        payload["refresh_token"] = self.refresh_token

        [auth, status_auth] = self.fetch("https://auth.tado.com/oauth/token", body=payload, bodyType="x-www-form-urlencoded", method="POST")
        if status_auth != 200:
            raise Exception("Error regenerating access token")
        
        self.access_token = auth["access_token"]
        self.refresh_token = auth["refresh_token"]
        self.expires_at = time.time() + auth["expires_in"]
    
    def get_access_token(self):
        username = self._get_input_value(self.PIN_I_EMAIL)
        password = self._get_input_value(self.PIN_I_PASSWORD)

        if username == "" or password == "":
            self._set_output_value(self.PIN_O_EXCEPTION, 1)
            raise Exception("No username or password provided")
        
        payload = {
    	    "client_id": "tado-web-app",
    	    "client_secret": "wZaRN7rpjn3FoNyF5IFuxg9uMzYJcvOoQ8QWiIqS3hfk6gLhVlG57j5YNoZL2Rtc",
	        "grant_type": "password"
        }
        payload["username"] = username
        payload["password"] = password

        [auth, status_auth] = self.fetch("https://auth.tado.com/oauth/token", body=payload, bodyType="x-www-form-urlencoded", method="POST")
        if status_auth != 200:
            raise Exception("Error authenticating user")
        
        self.access_token = auth["access_token"]
        self.refresh_token = auth["refresh_token"]
        self.expires_at = time.time() + auth["expires_in"]

    def fetch(self, url, method = None, body = None, bodyType = None, access_token = None):
        """
        Fetch resources from the provided URL   

        :param url: The URL to fetch the resource from (http and https)
        :type url: string
        :param method: The method the fetch the resource with (`GET`, `POST`, `PUT`, or `DELETE`)
	    :type method: string
        :param body: The request body
        :type body: dict or None
        :param body_type: The type of the request body (`None`, `x-www-form-urlencoded` or `JSON`)
        :type body_type: string or None
        :param access_token: Authenticate with the OAuth2.0 authentication flow and a Bearer token
        :type access_token: string or None

        :return: The response body and status
        :rtype: [JSON or None, number]
        """

        # Build a SSL Context to disable certificate verification.
        ctx = ssl._create_unverified_context()
        # Build a http request and add an authorization header or a form data body
        request = request_method(url, method=method)
        if access_token != None:
            request.add_header("Authorization", "Bearer " + access_token)
        if bodyType == "x-www-form-urlencoded":
            data = urllib.urlencode(body)
            data = data.encode("ascii")
            request.add_data(data)
        elif bodyType == "JSON":
            request.add_header('Content-Type', 'application/json')
            data = json.dumps(body)
            data = data.encode('ascii')
            request.add_data(data)

        try:
            # Open the URL
            response = urllib2.urlopen(request, context=ctx)
        except urllib2.HTTPError as e:
            if e.code == 401:
                self._set_output_value(self.PIN_O_EXCEPTION, 4)
            return [None, e.code]
        except urllib2.URLError as e:
            self._set_output_value(self.PIN_O_EXCEPTION, 5)
            return [None, -1]
        else:
            # Return the response if the request was successful
            response_data = response.read()
            return [json.loads(response_data), 200]

class request_method(urllib2.Request):
    def __init__(self, url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None):
        urllib2.Request.__init__(self, url, data, headers, origin_req_host, unverifiable)
        self.method = method

    def get_method(self):
        if self.method:
            return self.method

        return urllib2.Request.get_method(self)