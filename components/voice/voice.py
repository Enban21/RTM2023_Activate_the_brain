﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file voice.py
 @brief 開閉指示と照度センサーのon・offを送信できる
 @date $Date$


"""
# </rtc-template>

import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

#other-import
import speech_recognition as sr

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
voice_spec = ["implementation_id", "voice", 
         "type_name",         "voice", 
         "description",       "", 
         "version",           "1.0.0", 
         "vendor",            "Kobayasi", 
         "category",          "onseiwoyomitoru", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class voice
# @brief 開閉指示と照度センサーのon・offを送信できる
# 
# Voiceから送信される音声は開閉指示と照度センサーのON・OFFの2種類である。開閉指示
# は５段階で切る。詳しくは、始点から終点を１００％とすると、「開けて・閉めて」を詳
# しく言うと１００％、「半分開けて・閉めて」
# と言うと、５０% 「少し占めて・開けて」というと２５％開ける・閉める。
# また、照度センサーのON・OFFを切り替えることができる。「LOCKして」と言うと、照度
# データから開閉判断するのを停止する。「LOCK解除して」というと、開閉判断するのを再
# 開する。
# 
# Voiceから送信される音声は開閉指示と照度センサーのON・OFFの2種類である。開閉指示
# は５段階で切る。詳しくは、始点から終点を１００％とすると、「開けて・閉めて」を詳
# しく言うと１００％、「半分開けて・閉めて」
# と言うと、５０% 「少し占めて・開けて」というと２５％開ける・閉める。
# また、照度センサーのON・OFFを切り替えることができる。「LOCKして」と言うと、照度
# データから開閉判断するのを停止する。「LOCK解除して」というと、開閉判断するのを再
# 開する。
# 
# Voiceから送信される音声は開閉指示と照度センサーのON・OFFの2種類である。開閉指示
# は５段階で切る。詳しくは、始点から終点を１００％とすると、「開けて・閉めて」を詳
# しく言うと１００％、「半分開けて・閉めて」
# と言うと、５０% 「少し占めて・開けて」というと２５％開ける・閉める。
# また、照度センサーのON・OFFを切り替えることができる。「LOCKして」と言うと、照度
# データから開閉判断するのを停止する。「LOCK解除して」というと、開閉判断するのを再
# 開する。
# 
# 
# </rtc-template>
class voice(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_voice_out = OpenRTM_aist.instantiateDataType(RTC.TimedWString)
        """
        """
        self._voice_outOut = OpenRTM_aist.OutPort("voice_out", self._d_voice_out)


		


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
		
        # Set OutPort buffers
        self.addOutPort("voice_out",self._voice_outOut)


        # Set service provider to Ports
		
        # Set service consumers to Ports
		
        # Set CORBA Service Ports
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()	
		
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
        with self.microphone as source:
            print("ノイズを調整しています。")
            self.recognizer.adjust_for_ambient_noise(source)
            print("準備完了")     
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
    # Voiceから送信される音声は開閉指示と照度センサーのON・OFFの2種類である。開閉指
	# 示は５段階で切る。詳しくは、始点から終点を１００％とすると、「開けて・閉めて
	# 」を詳しく言うと１００％、「半分開けて・閉めて」
	# と言うと、５０% 「少し占めて・開けて」というと２５％開ける・閉める。
	# また、照度センサーのON・OFFを切り替えることができる。「LOCKして」と言うと、照
	# 度データから開閉判断するのを停止する。「LOCK解除して」というと、開閉判断する
	# のを再開する。
    #
    # The execution action that is invoked periodically
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #

    def onExecute(self, ec_id):
        with self.microphone as source:
            try:
                print("何か喋ってください")
                audio = self.recognizer.listen(source, phrase_time_limit=5)
                print("認識中")
                # 認識する言語を設定して結果を格納
                self.result = self.recognizer.recognize_google(audio, language='ja-JP')
                print(self.result)

                self._d_voice_out.data = self.result #self._d_アウトポート名.data = 送りたい変数 
                self._voice_outOut.write()   #self._アウトポート名Out.write() で、self._d_アウトポート名.dataに格納したデータを送信。
            
            except sr.RequestError as e:
                print("結果をリクエストできませんでした。")

            except sr.UnknownValueError as e:
                print("faild") 
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
	



def voiceInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=voice_spec)
    manager.registerFactory(profile,
                            voice,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    voiceInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("voice" + args)

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

