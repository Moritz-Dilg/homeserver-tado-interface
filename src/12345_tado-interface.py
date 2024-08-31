# coding: UTF-8
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
        pass

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
        pass
