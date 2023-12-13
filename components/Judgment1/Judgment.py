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
import re
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist


RE_OPEN_FULL  = re.compile("(カーテンを?)?( |　)?(全部|全て)?( |　)?開(い|け)て")
RE_OPEN_FEW   = re.compile("(カーテンを?)?( |　)?(少し|ちょっと)( |　)?開(い|け)て")
RE_CLOSE_FULL = re.compile("(カーテンを?)?( |　)?(全部|全て)?( |　)?閉(め|じ)て")
RE_CLOSE_FEW  = re.compile("(カーテンを?)?( |　)?(少し|ちょっと)( |　)?閉(め|じ)て")


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
        # 一度音声でのカーテン位置の調整をした場合、この変数を True にして、明るさでの調整をストップする
        # "解除" という音声が入力された場合に False にして、明るさでの調整を再開させる
        self.ignore_brightness = False
    
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
        # 最後にデータを書き込むため、self._d_SendOut.data を更新しない場合は即座に関数を終了する
        has_new_voice_input = self._VoiceInIn.isNew()
        if self.ignore_brightness or has_new_voice_input:  # 明るさを無視しているか、新しい音声の入力があるか
            """ 音声によるカーテンの位置調整
            """
            if not has_new_voice_input:
                # 新しい音声の入力がなければ終了する (明るさを無視しているなら、新しい音声の入力がない場合もある)
                return RTC.RTC_OK

            self._d_VoiceIn = self._VoiceInIn.read()  # 値を読み込む(self._d_入力ポート名 = self._入力ポート名In.read())
            voice_input: str = self._d_VoiceIn.data  # text = self._d_入力ポート名.data

            voice_input.replace('　', '')  # 全角スペースを消す
            voice_input.replace(' ', '')  # スペースを消す
            print("音声:", voice_input)

            if voice_input == "解除":
                self.ignore_brightness = False
                print(00)
                return RTC.RTC_OK  # 位置の調整は次呼び出されたときに行う
            elif RE_OPEN_FULL.fullmatch(voice_input):
                self._d_SendOut.data = 0
                print(0)
            elif RE_OPEN_FEW.fullmatch(voice_input):
                self._d_SendOut.data = 25
                print(25)
            elif RE_CLOSE_FULL.fullmatch(voice_input):
                self._d_SendOut.data = 100
                print(100)
            elif RE_CLOSE_FEW.fullmatch(voice_input):
                self._d_SendOut.data = 75
                print(75)
            else:
                return RTC.RTC_OK  # マッチしなければ何もせずに関数を終了する

            self._SendOutOut.write()
            self.ignore_brightness = True  # 音声による位置の調整を行った場合にのみ、明るさでの調整を無視する
        else:
            """ 明るさによるカーテンの位置調整
            self.follow_voice_input が False の場合にのみ行う
            """
            if not self._LightInIn.isNew():  # 明るさの入力がない場合は関数を終了する
                return RTC.RTC_OK
            
            self._d_LightIn = self._LightInIn.read()
            brightness = self._d_LightIn.data
            print("明るさ:", brightness)

            if brightness < 500:
                self._d_SendOut.data = 0
                print(0)
            elif brightness < 650:
                self._d_SendOut.data = 25
                print(25)
            elif brightness < 800:
                self._d_SendOut.data = 50
                print(50)
            elif brightness < 1050:
                self._d_SendOut.data = 75
                print(75)
            else:  # 明るさが 1050 以上
                self._d_SendOut.data = 100
                print(100)
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