# coding: UTF-8

import urllib
import urllib2
import ssl
import json
import time

##!!!!##################################################################################################
#### Own written code can be placed above this commentblock . Do not change or delete commentblock! ####
########################################################################################################
##** Code created by generator - DO NOT CHANGE! **##

class Tado_interface12345(hsl20_4.BaseModule):

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
        self.PIN_O_BATTERY_1=5
        self.PIN_O_DEBUG_1=6
        self.PIN_O_DEBUG_2=7
        self.PIN_O_DEBUG_3=8
        self.PIN_O_DEBUG_4=9
        self.PIN_O_DEBUG_5=10
        self.PIN_O_DEBUG_6=11
        self.PIN_O_DEBUG_7=12
        self.PIN_O_DEBUG_8=13
        self.PIN_O_DEBUG_9=14
        self.PIN_O_DEBUG_10=15

########################################################################################################
#### Own written code can be placed after this commentblock . Do not change or delete commentblock! ####
###################################################################################################!!!##

    def on_init(self):
        self.access_token = None
        self.refresh_token = None
        self.expires_at = None

    def on_input_value(self, index, value):
        if index == self.PIN_I_TRIGGER:
            self.get_current_state()
        elif index in [self.PIN_I_EMAIL, self.PIN_I_PASSWORD]:
            pass
        elif index == self.PIN_I_ZONE_1:
            pass
        elif index == self.PIN_I_TARGET:
            pass
        pass
    
    def get_current_state(self):
        try:
            if self.access_token == None or self.refresh_token == None:
                self.get_access_token()
            if self.expires_at >= time.time():
                pass
        except:
            pass
    
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

        [auth, status_auth] = self.fetch("https://auth.tado.com/oauth/token", body=payload, bodyType="x-www-form-urlencoded")
        if status_auth != 200:
            raise Exception("Error authenticating user")
        
        self.access_token = auth["access_token"]
        self.refresh_token = auth["refresh_token"]
        self.expires_at = time.time() + auth["expires_in"]

    def fetch(self, url, body = None, bodyType = None, access_token = None):
        """
        Fetch resources from the provided URL   

        :param url: The URL to fetch the resource from (http and https)
        :type url: string
        :param body: The request body
        :type body: dict or None
        :param body_type: The type of the request body (`None` or `x-www-form-urlencoded`)
        :type body_type: string or None
        :param access_token: Authenticate with the OAuth2.0 authentication flow and a Bearer token
        :type access_token: string or None

        :return: The response body and status
        :rtype: [JSON or None, number]
        """

        # Build a SSL Context to disable certificate verification.
        ctx = ssl._create_unverified_context()
        # Build a http request and add an authorization header or a form data body
        request = urllib2.Request(url)
        if access_token != None:
            request.add_header("Authorization", "Bearer " + access_token)
        if bodyType == "x-www-form-urlencoded":
            data = urllib.urlencode(body)
            data = data.encode("ascii")
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