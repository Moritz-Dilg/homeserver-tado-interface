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

class Tado_interface14670(hsl20_4.BaseModule):

    def __init__(self, homeserver_context):
        hsl20_4.BaseModule.__init__(self, homeserver_context, "tado_interface")
        self.FRAMEWORK = self._get_framework()
        self.LOGGER = self._get_logger(hsl20_4.LOGGING_NONE,())
        self.PIN_I_TRIGGER=1
        self.PIN_I_EMAIL=2
        self.PIN_I_PASSWORD=3
        self.PIN_I_ZONE_1=4
        self.PIN_I_ZONE_2=5
        self.PIN_I_ZONE_3=6
        self.PIN_I_ZONE_4=7
        self.PIN_I_ZONE_5=8
        self.PIN_I_ZONE_6=9
        self.PIN_I_ZONE_7=10
        self.PIN_I_ZONE_8=11
        self.PIN_I_ZONE_9=12
        self.PIN_I_ZONE_10=13
        self.PIN_I_ZONE_11=14
        self.PIN_I_ZONE_12=15
        self.PIN_I_ZONE_13=16
        self.PIN_I_ZONE_14=17
        self.PIN_I_ZONE_15=18
        self.PIN_I_ZONE_16=19
        self.PIN_I_ZONE_17=20
        self.PIN_I_ZONE_18=21
        self.PIN_I_ZONE_19=22
        self.PIN_I_ZONE_20=23
        self.PIN_I_TARGET_1=24
        self.PIN_I_TARGET_2=25
        self.PIN_I_TARGET_3=26
        self.PIN_I_TARGET_4=27
        self.PIN_I_TARGET_5=28
        self.PIN_I_TARGET_6=29
        self.PIN_I_TARGET_7=30
        self.PIN_I_TARGET_8=31
        self.PIN_I_TARGET_9=32
        self.PIN_I_TARGET_10=33
        self.PIN_I_TARGET_11=34
        self.PIN_I_TARGET_12=35
        self.PIN_I_TARGET_13=36
        self.PIN_I_TARGET_14=37
        self.PIN_I_TARGET_15=38
        self.PIN_I_TARGET_16=39
        self.PIN_I_TARGET_17=40
        self.PIN_I_TARGET_18=41
        self.PIN_I_TARGET_19=42
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
        self.first_trigger = True

    def on_input_value(self, index, value):
        try:
            if index == self.PIN_I_TRIGGER:
                # Set the zone names that are provided as fixed values at the first time this logic block is triggered
                if self.first_trigger == True:
                    self.first_trigger = False
                    self.set_all_zone_names()

                self.get_current_state()
            elif index in [self.PIN_I_EMAIL, self.PIN_I_PASSWORD]:
                pass
            elif index in range(self.PIN_I_ZONE_1, self.PIN_I_ZONE_20 + 1):
                self.set_zone_name(index - self.PIN_I_ZONE_1 + 1, value)
            elif index in range(self.PIN_I_TARGET_1, self.PIN_I_TARGET_20 + 1):
                self.set_zone_temperature(index - self.PIN_I_TARGET_1 + 1, value)
            
        except exception as e:
            self._set_output_value(self.PIN_O_EXCEPTION, e.get_error_code())
    
    def set_all_zone_names(self):
        for i in range(self.PIN_I_ZONE_1, self.PIN_I_ZONE_20 + 1):
            self.zone_names[self._get_input_value(i)] = i - self.PIN_I_ZONE_1 + 1
        self.update_zone_ids()


    def set_zone_name(self, zone_id, zone_name):
        self.zone_names[zone_name] = zone_id
        self.update_zone_ids()

    def set_zone_temperature(self, zone_id, temperature):
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
            raise set_temperature_exception("Error setting target temperature")

    def update_zone_ids(self):
        self.validate_access_token()

        if not self.home_id:
            self.get_home_id()
        
        [zones, status] = self.fetch("https://my.tado.com/api/v2/homes/" + str(self.home_id) + "/zones?ngsw-bypass=true", method="GET", access_token=self.access_token)
        if status != 200:
            raise zone_id_exception("Error retrieving zones information")
        
        for i in range(len(zones)):
                if zones[i]["name"] in self.zone_names:
                    self.tado_id_to_zone_id[zones[i]["id"]] = self.zone_names[zones[i]["name"]]

    def get_home_id(self):
        self.validate_access_token()

        [me, status] = self.fetch("https://my.tado.com/api/v2/me", method="GET", access_token=self.access_token)
        if status != 200:
            raise home_id_exception("Error retrieving user information")
        
        self.home_id = me["homes"][0]["id"]

    def validate_access_token(self):
        if self.access_token == None:
            self.get_access_token()
        if self.expires_at <= time.time():
            self.refresh_access_token()
    
    def get_current_state(self):
        self.validate_access_token()
        
        if not self.home_id:
            self.get_home_id()
        
        [zoneStates, status] = self.fetch("https://my.tado.com/api/v2/homes/" + str(self.home_id) + "/zoneStates", method="GET", access_token=self.access_token)
        if status != 200:
            raise zone_state_exception("Error retrieving zone states")
        
        zoneStates = zoneStates["zoneStates"]
        for tado_id in self.tado_id_to_zone_id:
            zone_id = self.tado_id_to_zone_id[tado_id]
            current_zone = zoneStates[str(tado_id)]
        
            actual = current_zone["sensorDataPoints"]["insideTemperature"]["celsius"]
            target = current_zone["setting"]["temperature"]["celsius"]
            humidity = current_zone["sensorDataPoints"]["humidity"]["percentage"]
            self.set_output_zone_states(3 * zone_id - 1, actual, target, humidity)
    
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
            raise authentication_exception("Error regenerating access token")
        
        self.access_token = auth["access_token"]
        self.refresh_token = auth["refresh_token"]
        self.expires_at = time.time() + auth["expires_in"]
    
    def get_access_token(self):
        username = self._get_input_value(self.PIN_I_EMAIL)
        password = self._get_input_value(self.PIN_I_PASSWORD)

        if username == "" or password == "":
            self._set_output_value(self.PIN_O_EXCEPTION, 1)
            raise no_credentials_exception("No username or password provided")
        
        payload = {
    	    "client_id": "tado-web-app",
    	    "client_secret": "wZaRN7rpjn3FoNyF5IFuxg9uMzYJcvOoQ8QWiIqS3hfk6gLhVlG57j5YNoZL2Rtc",
	        "grant_type": "password"
        }
        payload["username"] = username
        payload["password"] = password

        [auth, status_auth] = self.fetch("https://auth.tado.com/oauth/token", body=payload, bodyType="x-www-form-urlencoded", method="POST")
        if status_auth != 200:
            raise authentication_exception("Error authenticating user")
        
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
                raise unauthorized_request_exception("Unauthorized request")
            
            raise unknown_exception("Code: " + str(e.code) + " - " + e.reason)
        except urllib2.URLError as e:
            raise unknown_exception(e.reason)
        else:
            # Return the response if the request was successful
            response_data = response.read()
            return [json.loads(response_data), 200]

class exception(Exception):
    def get_error_code(self):
        return "I-00"

class unknown_exception(exception):
    def get_error_code(self):
        return "I-01: " + self.message
class no_credentials_exception(exception):
    def get_error_code(self):
        return "E-11"

class authentication_exception(exception):
    def get_error_code(self):
        return "I-12"
    
class unauthorized_request_exception(exception):
    def get_error_code(self):
        return "E-13"

class zone_state_exception(exception):
    def get_error_code(self):
        return "I-21"
    
class home_id_exception(exception):
    def get_error_code(self):
        return "I-22"

class zone_id_exception(exception):
    def get_error_code(self):
        return "I-23"

class set_temperature_exception(exception):
    def get_error_code(self):
        return "I-24"
    
class request_method(urllib2.Request):
    def __init__(self, url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None):
        urllib2.Request.__init__(self, url, data, headers, origin_req_host, unverifiable)
        self.method = method

    def get_method(self):
        if self.method:
            return self.method

        return urllib2.Request.get_method(self)