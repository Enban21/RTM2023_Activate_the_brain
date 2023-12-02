#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file Base_value_judgmentTest.py
 @brief ModuleDescription
 @date $Date$


"""
# </rtc-template>

from __future__ import print_function
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist


# Import Service implementation class
# <rtc-template block="service_impl">

import Base_value_judgment

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
base_value_judgmenttest_spec = ["implementation_id", "Base_value_judgmentTest", 
         "type_name",         "Base_value_judgmentTest", 
         "description",       "ModuleDescription", 
         "version",           "1.0.0", 
         "vendor",            "ISHUKAWA Y", 
         "category",          "test", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class Base_value_judgmentTest
# @brief ModuleDescription
# 
# CO2から受け取ったデータをもとに計算を行う。受け取ったデータが基準値を超過しそう
# になると、LEDへと信号が出力される。信号を受け取った赤色LEDはゆっくりと点滅をする
# 。その後、受け取ったデータが基準値を超過した場合、新たな信号が出力される。信号を
# 受け取った赤色LEDが高速点滅する。
# 警告確認後、喚気が行われ、受け取ったデータが基準値を下回ると、LEDからの信号出力
# が停止され、赤色LEDが消灯する。
# 
# 
# </rtc-template>
class Base_value_judgmentTest(OpenRTM_aist.DataFlowComponentBase):
    
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_LED_Out = OpenRTM_aist.instantiateDataType(RTC.TimedShort)
        """
        """
        self._LED_OutIn = OpenRTM_aist.InPort("LED_Out", self._d_LED_Out)
        self._d_CO2_In = OpenRTM_aist.instantiateDataType(RTC.TimedShort)
        """
        """
        self._CO2_InOut = OpenRTM_aist.OutPort("CO2_In", self._d_CO2_In)


        


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
        self.addInPort("LED_Out",self._LED_OutIn)
        
        # Set OutPort buffers
        self.addOutPort("CO2_In",self._CO2_InOut)
        
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
    
    #    ##
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
        # CO2から受け取ったデータをもとに計算を行う。受け取ったデータが基準値を超過しそ
	# うになると、LEDへと信号が出力される。信号を受け取った赤色LEDはゆっくりと点滅
	# をする。その後、受け取ったデータが基準値を超過した場合、新たな信号が出力され
	# る。信号を受け取った赤色LEDが高速点滅する。
	# 警告確認後、喚気が行われ、受け取ったデータが基準値を下回ると、LEDからの信号出
	# 力が停止され、赤色LEDが消灯する。
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
    
    #    ##
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
    
        return RTC.RTC_OK
    
    ###
    ##
    ## The aborting action when main logic error occurred.
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    #    #
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
    
    def runTest(self):
        return True

def RunTest():
    manager = OpenRTM_aist.Manager.instance()
    comp = manager.getComponent("Base_value_judgmentTest0")
    if comp is None:
        print('Component get failed.', file=sys.stderr)
        return False
    return comp.runTest()

def Base_value_judgmentTestInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=base_value_judgmenttest_spec)
    manager.registerFactory(profile,
                            Base_value_judgmentTest,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    Base_value_judgmentTestInit(manager)
    Base_value_judgment.Base_value_judgmentInit(manager)

    # Create a component
    comp = manager.createComponent("Base_value_judgmentTest")

def main():
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager(True)

    ret = RunTest()
    mgr.shutdown()

    if ret:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()

