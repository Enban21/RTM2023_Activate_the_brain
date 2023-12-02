#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file Judgment.py
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


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
judgment_spec = ["implementation_id", "Judgment", 
         "type_name",         "Judgment", 
         "description",       "", 
         "version",           "1.0.0", 
         "vendor",            "motizuki,kobayashi", 
         "category",          "test", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class Judgment
# @brief ${rtcParam.description}
# 
# LightとVoiceから来た情報を判断する
# 
# 
# </rtc-template>
class Judgment(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_LightIn = OpenRTM_aist.instantiateDataType(RTC.TimedFloat)
        """
        """
        self._LightInIn = OpenRTM_aist.InPort("LightIn", self._d_LightIn)
        self._d_VoiceIn = OpenRTM_aist.instantiateDataType(RTC.TimedWString)
        """
        """
        self._VoiceInIn = OpenRTM_aist.InPort("VoiceIn", self._d_VoiceIn)
        self._d_SendOut = OpenRTM_aist.instantiateDataType(RTC.TimedShort)
        """
        """
        self._SendOutOut = OpenRTM_aist.OutPort("SendOut", self._d_SendOut)


		


        # initialize of configuration-data.
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
        self.addInPort("LightIn",self._LightInIn)
        self.addInPort("VoiceIn",self._VoiceInIn)
		
        # Set OutPort buffers
        self.addOutPort("SendOut",self._SendOutOut)
		
        # Set service provider to Ports
		
        # Set service consumers to Ports
		
        # Set CORBA Service Ports
		
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
	
    ##
    #
    # The execution action that is invoked periodically
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onExecute(self, ec_id):
        if self._VoiceInIn.isNew(): #新しいデータが来たか確認(self._入力ポート名In.isNew())
            self._d_VoiceIn = self._VoiceInIn.read() #値を読み込む(self._d_入力ポート名 = self._入力ポート名In.read())
            text = self._d_VoiceIn.data # text = self._d_入力ポート名.data
            print(text)             

            if self._LightInIn.isNew():
                self._d_LightIn = self._LightInIn.read() #値を読み込む(self._d_入力ポート名 = self._入力ポート名In.read())
                number =  self._d_LightIn.data # text = self._d_入力ポート名.data
                print(number)  
                if text == "開いて" or text =="開けて" or  text =="カーテン開けて" or text =="カーテンを開けて" or text =="カーテンを全部開いて" or text =="カーテンを全て開けて" or text =="カーテン全て開いて":
                    self._d_SendOut.data = 0
                    self._SendOutOut.write()
                elif text ==  "少し開けて" or text =="少し開いて" or text =="少し開いて" or text =="ちょっと開けて" or text =="ちょっと開いて" or text =="カーテンを少し開けて" or text =="カーテンを少し開いて"  or text =="カーテン少し開けて" or text =="カーテン少し開いて":
                    self._d_SendOut.data = 75
                    self._SendOutOut.write()
                elif text ==  "カーテン閉めて" or text =="閉めて" or text =="カーテンを閉めて" or text =="カーテンを全部閉めて" or text =="カーテン全て閉めて":
                    self._d_SendOut.data = 100
                    self._SendOutOut.write()  
                elif text ==  "少し閉めてカーテン" or text =="少し閉めて" or text =="少しカーテンを閉めて" or text =="カーテンを少し閉めて" or text =="カーテン少し閉めて" or text =="少しカーテン閉めて":
                    self._d_SendOut.data = 25
                    self._SendOutOut.write()
                elif text == "解除" and number < 500:
                    self._d_SendOut.data = 0
                    self._SendOutOut.write()    
                elif text == "解除" and number < 650:
                    self._d_SendOut.data = 25
                    self._SendOutOut.write()    
                elif text == "解除" and number < 800:
                    self._d_SendOut.data = 50
                    self._SendOutOut.write()    
                elif text == "解除" and number < 1050:
                    self._d_SendOut.data = 75
                    self._SendOutOut.write()    
                elif text == "解除" and number >= 1050:
                    self._d_SendOut.data = 100
                    self._SendOutOut.write()                                    
    
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
	



def JudgmentInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=judgment_spec)
    manager.registerFactory(profile,
                            Judgment,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    JudgmentInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("Judgment" + args)

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

