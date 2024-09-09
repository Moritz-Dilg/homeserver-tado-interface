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
        self.PIN_I_TARGET_1=5
        self.PIN_I_ZONE_2=6
        self.PIN_I_TARGET_2=7
        self.PIN_I_ZONE_3=8
        self.PIN_I_TARGET_3=9
        self.PIN_I_ZONE_4=10
        self.PIN_I_TARGET_4=11
        self.PIN_I_ZONE_5=12
        self.PIN_I_TARGET_5=13
        self.PIN_I_ZONE_6=14
        self.PIN_I_TARGET_6=15
        self.PIN_I_ZONE_7=16
        self.PIN_I_TARGET_7=17
        self.PIN_I_ZONE_8=18
        self.PIN_I_TARGET_8=19
        self.PIN_I_ZONE_9=20
        self.PIN_I_TARGET_9=21
        self.PIN_I_ZONE_10=22
        self.PIN_I_TARGET_10=23
        self.PIN_I_ZONE_11=24
        self.PIN_I_TARGET_11=25
        self.PIN_I_ZONE_12=26
        self.PIN_I_TARGET_12=27
        self.PIN_I_ZONE_13=28
        self.PIN_I_TARGET_13=29
        self.PIN_I_ZONE_14=30
        self.PIN_I_TARGET_14=31
        self.PIN_I_ZONE_15=32
        self.PIN_I_TARGET_15=33
        self.PIN_I_ZONE_16=34
        self.PIN_I_TARGET_16=35
        self.PIN_I_ZONE_17=36
        self.PIN_I_TARGET_17=37
        self.PIN_I_ZONE_18=38
        self.PIN_I_TARGET_18=39
        self.PIN_I_ZONE_19=40
        self.PIN_I_TARGET_19=41
        self.PIN_I_ZONE_20=42
        self.PIN_I_TARGET_20=43
        self.PIN_O_EXCEPTION=1
        self.PIN_O_ACTUAL_1=2
        self.PIN_O_TARGET_1=3
        self.PIN_O_HUMIDITY_1=4
        self.PIN_O_ACTUAL_2=5
        self.PIN_O_TARGET_2=6
        self.PIN_O_HUMIDITY_2=7
        self.PIN_O_ACTUAL_3=8
        self.PIN_O_TARGET_3=9
        self.PIN_O_HUMIDITY_3=10
        self.PIN_O_ACTUAL_4=11
        self.PIN_O_TARGET_4=12
        self.PIN_O_HUMIDITY_4=13
        self.PIN_O_ACTUAL_5=14
        self.PIN_O_TARGET_5=15
        self.PIN_O_HUMIDITY_5=16
        self.PIN_O_ACTUAL_6=17
        self.PIN_O_TARGET_6=18
        self.PIN_O_HUMIDITY_6=19
        self.PIN_O_ACTUAL_7=20
        self.PIN_O_TARGET_7=21
        self.PIN_O_HUMIDITY_7=22
        self.PIN_O_ACTUAL_8=23
        self.PIN_O_TARGET_8=24
        self.PIN_O_HUMIDITY_8=25
        self.PIN_O_ACTUAL_9=26
        self.PIN_O_TARGET_9=27
        self.PIN_O_HUMIDITY_9=28
        self.PIN_O_ACTUAL_10=29
        self.PIN_O_TARGET_10=30
        self.PIN_O_HUMIDITY_10=31
        self.PIN_O_ACTUAL_11=32
        self.PIN_O_TARGET_11=33
        self.PIN_O_HUMIDITY_11=34
        self.PIN_O_ACTUAL_12=35
        self.PIN_O_TARGET_12=36
        self.PIN_O_HUMIDITY_12=37
        self.PIN_O_ACTUAL_13=38
        self.PIN_O_TARGET_13=39
        self.PIN_O_HUMIDITY_13=40
        self.PIN_O_ACTUAL_14=41
        self.PIN_O_TARGET_14=42
        self.PIN_O_HUMIDITY_14=43
        self.PIN_O_ACTUAL_15=44
        self.PIN_O_TARGET_15=45
        self.PIN_O_HUMIDITY_15=46
        self.PIN_O_ACTUAL_16=47
        self.PIN_O_TARGET_16=48
        self.PIN_O_HUMIDITY_16=49
        self.PIN_O_ACTUAL_17=50
        self.PIN_O_TARGET_17=51
        self.PIN_O_HUMIDITY_17=52
        self.PIN_O_ACTUAL_18=53
        self.PIN_O_TARGET_18=54
        self.PIN_O_HUMIDITY_18=55
        self.PIN_O_ACTUAL_19=56
        self.PIN_O_TARGET_19=57
        self.PIN_O_HUMIDITY_19=58
        self.PIN_O_ACTUAL_20=59
        self.PIN_O_TARGET_20=60
        self.PIN_O_HUMIDITY_20=61

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
            self.set_zone_name(1, value)
        elif index == self.PIN_I_ZONE_2:
            self.set_zone_name(2, value)
        elif index == self.PIN_I_ZONE_3:
            self.set_zone_name(3, value)
        elif index == self.PIN_I_ZONE_4:
            self.set_zone_name(4, value)
        elif index == self.PIN_I_ZONE_5:
            self.set_zone_name(5, value)
        elif index == self.PIN_I_ZONE_6:
            self.set_zone_name(6, value)
        elif index == self.PIN_I_ZONE_7:
            self.set_zone_name(7, value)
        elif index == self.PIN_I_ZONE_8:
            self.set_zone_name(8, value)
        elif index == self.PIN_I_ZONE_9:
            self.set_zone_name(9, value)
        elif index == self.PIN_I_ZONE_10:
            self.set_zone_name(10, value)
        elif index == self.PIN_I_ZONE_11:
            self.set_zone_name(11, value)
        elif index == self.PIN_I_ZONE_12:
            self.set_zone_name(12, value)
        elif index == self.PIN_I_ZONE_13:
            self.set_zone_name(13, value)
        elif index == self.PIN_I_ZONE_14:
            self.set_zone_name(14, value)
        elif index == self.PIN_I_ZONE_15:
            self.set_zone_name(15, value)
        elif index == self.PIN_I_ZONE_16:
            self.set_zone_name(16, value)
        elif index == self.PIN_I_ZONE_17:
            self.set_zone_name(17, value)
        elif index == self.PIN_I_ZONE_18:
            self.set_zone_name(18, value)
        elif index == self.PIN_I_ZONE_19:
            self.set_zone_name(19, value)
        elif index == self.PIN_I_ZONE_20:
            self.set_zone_name(20, value)
        elif index == self.PIN_I_TARGET:
            self.set_zone(1, value)
        pass
    
    def set_zone_name(self, zone_id, zone_name):
        self.zone_names[zone_name] = zone_id
        try:
            self.update_zones()
        except:
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
                elif zone_id == 2:
                    self.set_output_zone_states(self.PIN_O_ACTUAL_2, actual, target, humidity)
                elif zone_id == 3:
                    self.set_output_zone_states(self.PIN_O_ACTUAL_3, actual, target, humidity)
                elif zone_id == 4:
                    self.set_output_zone_states(self.PIN_O_ACTUAL_4, actual, target, humidity)
                elif zone_id == 5:
                    self.set_output_zone_states(self.PIN_O_ACTUAL_5, actual, target, humidity)
                elif zone_id == 6:
                    self.set_output_zone_states(self.PIN_O_ACTUAL_6, actual, target, humidity)
                elif zone_id == 7:
                    self.set_output_zone_states(self.PIN_O_ACTUAL_7, actual, target, humidity)
                elif zone_id == 8:
                    self.set_output_zone_states(self.PIN_O_ACTUAL_8, actual, target, humidity)
                elif zone_id == 9:
                    self.set_output_zone_states(self.PIN_O_ACTUAL_9, actual, target, humidity)
                elif zone_id == 10:
                    self.set_output_zone_states(self.PIN_O_ACTUAL_10, actual, target, humidity)
                elif zone_id == 11:
                    self.set_output_zone_states(self.PIN_O_ACTUAL_11, actual, target, humidity)
                elif zone_id == 12:
                    self.set_output_zone_states(self.PIN_O_ACTUAL_12, actual, target, humidity)
                elif zone_id == 13:
                    self.set_output_zone_states(self.PIN_O_ACTUAL_13, actual, target, humidity)
                elif zone_id == 14:
                    self.set_output_zone_states(self.PIN_O_ACTUAL_14, actual, target, humidity)
                elif zone_id == 15:
                    self.set_output_zone_states(self.PIN_O_ACTUAL_15, actual, target, humidity)
                elif zone_id == 16:
                    self.set_output_zone_states(self.PIN_O_ACTUAL_16, actual, target, humidity)
                elif zone_id == 17:
                    self.set_output_zone_states(self.PIN_O_ACTUAL_17, actual, target, humidity)
                elif zone_id == 18:
                    self.set_output_zone_states(self.PIN_O_ACTUAL_18, actual, target, humidity)
                elif zone_id == 19:
                    self.set_output_zone_states(self.PIN_O_ACTUAL_19, actual, target, humidity)
                elif zone_id == 20:
                    self.set_output_zone_states(self.PIN_O_ACTUAL_20, actual, target, humidity)

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