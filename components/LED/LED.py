#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file LED.py
 @brief ${rtcParam.description}
 @date $Date$


"""
# </rtc-template>

import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist
import RPi.GPIO as GPIO
#other-import

from Base_value_judgment import NORMAL, WARNING, CAUTION


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
led_spec = ["implementation_id", "LED", 
         "type_name",         "LED", 
         "description",       "${rtcParam.description}", 
         "version",           "1.0.0", 
         "vendor",            "ISHIKAWA Y", 
         "category",          "User Interface", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         ""]

LED_PIN = 12

# </rtc-template>

# <rtc-template block="component_description">
##
# @class LED
# @brief ${rtcParam.description}
# 
# Base-value-judgmentから信号を受け取り、赤色LEDを点滅させる
# 
# 
# </rtc-template>
class LED(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_LED_In = OpenRTM_aist.instantiateDataType(RTC.TimedShort)
        """
        """
        self._LED_InIn = OpenRTM_aist.InPort("LED_In", self._d_LED_In)


		


        # initialize of configuration-data.

        self.blink_frequency = 0.0
        self.is_bright = False

        # <rtc-template block="init_conf_param">
		
        # </rtc-template>


		 
    ##
    #
    # The initialize action (on CREATED->ALIVE transition)
    # 
    # @return RTC::ReturnCode_t
    # 
    #
    def onInitialize(self):
        # Bind variables and configuration variable
		
        # Set InPort buffers
        self.addInPort("LED_In",self._LED_InIn)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(LED_PIN, GPIO.OUT)
        GPIO.output(LED_PIN, GPIO.LOW)

        self.p = GPIO.PWM(LED_PIN, 500)
        self.p.start(0)
    

        return RTC.RTC_OK
	
    ###
    ## 
    ## The finalize action (on ALIVE->END transition)
    ## 
    ## @return RTC::ReturnCode_t
    #
    ## 
    #def onFinalize(self):
    #

    #    return RTC.RTC_OK
	
    ###
    ##
    ## The startup action when ExecutionContext startup
    ## 
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onStartup(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The shutdown action when ExecutionContext stop
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onShutdown(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ##
    #
    # The activated action (Active state entry action)
    #
    # @param ec_id target ExecutionContext Id
    # 
    # @return RTC::ReturnCode_t
    #
    #
    def onActivated(self, ec_id):
    
        return RTC.RTC_OK
	
    ###
    ##
    ## The deactivated action (Active state exit action)
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onDeactivated(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The execution action that is invoked periodically
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    def onExecute(self, ec_id):
        judgedvalue = self._LED_InIn.read()
        judgedvalue_data = judgedvalue.data

        if judgedvalue_data == NORMAL:
                self.is_bright= False
        else:
            self.is_bright = not self.is_bright
            self.p.ChangeDutyCycle(100 if self.is_bright else 0)
            self.blink_frequency = judgedvalue_data

        # self.speed_property に基いて点滅速度制御


        time.sleep(self.blink_frequency)

        print ("judgedvalue_data" , self.blink_frequency)


        return RTC.RTC_OK
	
    """    
    self.is_bright = not self.is_bright
    self.p.ChangeDutyCycle(100 if self.is_bright else 0)
    judgedvalue = self._LED_InIn.read()
    judgedvalue_data = judgedvalue.data
    # self.speed_property に基いて点滅速度制御
    if judgedvalue_data == NORMAL:
        self.blink_frequency = not self.is_bright
    elif judgedvalue_data == WARNING:
        self.blink_frequency = 0.5
    elif judgedvalue_data == CAUTION:
        self.blink_frequency = 2.0

        time.sleep(self.blink_frequency)

        print ("judgedvalue_data" , self.blink_frequency)
    """
    ###
    ##
    ## The aborting action when main logic error occurred.
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onAborting(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The error action in ERROR state
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onError(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The reset action that is invoked resetting
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onReset(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The state update action that is invoked after onExecute() action
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##

    ##
    #def onStateUpdate(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The action that is invoked when execution context's rate is changed
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onRateChanged(self, ec_id):
    #
    #    return RTC.RTC_OK
	



def LEDInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=led_spec)
    manager.registerFactory(profile,
                            LED,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    LEDInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("LED" + args)

def main():
    # remove --instance_name= option
    argv = [i for i in sys.argv if not "--instance_name=" in i]
    # Initialize manager
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()

def onFinalize(self):
    self.p.stop()
    GPIO.cleanup()
    return RTC.RTC_OK

if __name__ == "__main__":
    main()

