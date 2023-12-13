#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file Send.py
 @brief Switchbotに信号を送る
 @date $Date$


"""
# </rtc-template>

import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

#apiの設定
import json
import time
import hashlib
import hmac
import base64
import uuid
import requests
API_HOST = 'https://api.switch-bot.com/v1.1'


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
send_spec = ["implementation_id", "Send", 
         "type_name",         "Send", 
         "description",       "", 
         "version",           "1.0.0", 
         "vendor",            "Yoshiyuki Shin", 
         "category",          "Robot", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         "conf.default.Send_In0", "0",

         "conf.__widget__.Send_In0", "text",

         "conf.__type__.Send_In0", "short",

         ""]
# </rtc-template>

##
# カーテンを全開する。
#
# The initialize action (on CREATED->ALIVE transition)
# 
# @return RTC::ReturnCode_t
# 
#



# <rtc-template block="component_description">
##
# @class Send
# @brief Switchbotに信号を送る
# 
# 
# </rtc-template>
class Send(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_SendIn = OpenRTM_aist.instantiateDataType(RTC.TimedShort)
        """
        """
        self._SendInIn = OpenRTM_aist.InPort("SendIn", self._d_SendIn)


		


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
        """
        
         - Name:  Send_In0
         - DefaultValue: 0
        """
        self._Send_In0 = [0]
		
        # </rtc-template>


		 


    
    
    def onInitialize(self):
        # Bind variables and configuration variable
        self.bindParameter("Send_In0", self._Send_In0, "0")
		
        # Set InPort buffers
        self.addInPort("SendIn",self._SendInIn)
    
        # Set OutPort buffers
		
        # Set service provider to Ports
		
        # Set service consumers to Ports
		
        # Set CORBA Service Ports
		
        # open token
        self.token = '0ac894b6b710c87cc7845360aeadeea7eeb7c1f6de8cbad0d38f44c2c7c5f67329eba9cfc1fa8e48480ee73381bcdb37'
        # secret key
        self.secret = '84f376678cf65c590e87a8a6a6071397'
        self.device_id = 'C81008179DBC'

        nonce = uuid.uuid4()
        timestamp = int(round(time.time() * 1000))
        string_to_sign = f'{self.token}{timestamp}{nonce}'

        string_to_sign = bytes(string_to_sign, 'utf-8')
        self.secret = bytes(self.secret, 'utf-8')

        sign = base64.b64encode(hmac.new(self.secret, msg=string_to_sign, digestmod=hashlib.sha256).digest())
        print(f'Authorization: {self.token}')
        print(f't: {timestamp}')
        print(f'sign: {str(sign, "utf-8")}')
        print(f'nonce: {nonce}')

        self.session = requests.Session()
        self.session.headers['Authorization'] = self.token
        self.session.headers['Content-Type'] = 'application/json'
        self.session.headers['t'] = str(timestamp)
        self.session.headers['sign'] = str(sign, 'utf-8')
        self.session.headers['nonce'] = str(nonce)

        #open
        devices = self.session.post(f'{API_HOST}/devices/{self.device_id}/commands', json={
        'commandType': 'command',
        'command': 'turnOn',    
        'parameter': 'default',
        }).json()
        self.position=100
        print(devices)

        return RTC.RTC_OK
	
    ###
    ## カーテンを全部閉める。
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
	
    ###
    ##
    ## The activated action (Active state entry action)
    ##
    ## @param ec_id target ExecutionContext Id
    ## 
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onActivated(self, ec_id):
    #
    #    return RTC.RTC_OK
	
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
	
    ##
    # Judgmentからの信号を読み取り、switchbotカーテンに開閉命令を送信する。
    #
    # The execution action that is invoked periodically
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onExecute(self, ec_id):
        if self._SendInIn.isNew(): #新しいデータが来たか確認(self._入力ポート名In.isNew())
            self._d_SendIn = self._SendInIn.read() #値を読み込む(self._d_入力ポート名 = self._入力ポート名In.read())
            if self._d_SendIn.data > 100 or self._d_SendIn.data<0 : #要素が9より大きい時
                return RTC.RTC_ERROR #エラー状態に遷移   
            
            Discrimi =  self._d_SendIn.data # text = self._d_入力ポート名.data
            
            print(Discrimi)
            time.sleep(1)

            if(Discrimi != self.position):
                if Discrimi==0:
                    devices = self.session.post(f'{API_HOST}/devices/{self.device_id}/commands', json={
                    'commandType': 'command',
                    'command': 'turnOn',    
                    'parameter': 'default',
                    }).json()
                elif Discrimi==25:
                    devices = self.session.post(f'{API_HOST}/devices/{self.device_id}/commands', json={
                    'commandType': 'command',
                    'command': 'setPosition',
                    'parameter': '0,ff,25',#25%
                    }).json()
                elif Discrimi==50:
                    devices = self.session.post(f'{API_HOST}/devices/{self.device_id}/commands', json={
                    'commandType': 'command',
                    'command': 'setPosition',
                    'parameter': '0,ff,50',#50%
                    }).json()
                elif Discrimi==75:
                    devices = self.session.post(f'{API_HOST}/devices/{self.device_id}/commands', json={
                    'commandType': 'command',
                    'command': 'setPosition',
                    'parameter': '0,ff,75',#75%
                    }).json()
                elif Discrimi==100:
                    devices = self.session.post(f'{API_HOST}/devices/{self.device_id}/commands', json={
                    'commandType': 'command',
                    'command': 'turnOff',
                    'parameter': 'default',#100%
                    }).json()
                self.position = Discrimi

        return RTC.RTC_OK
	
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
	



def SendInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=send_spec)
    manager.registerFactory(profile,
                            Send,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    SendInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("Send" + args)

def main():
    # remove --instance_name= option
    argv = [i for i in sys.argv if not "--instance_name=" in i]
    # Initialize manager
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()

if __name__ == "__main__":
    main()

