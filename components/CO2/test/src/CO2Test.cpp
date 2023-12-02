// -*- C++ -*-
// <rtc-template block="description">
/*!
 * @file  CO2Test.cpp
 * @brief ${rtcParam.description} (test code)
 *
 */
// </rtc-template>

#include "CO2Test.h"

// Module specification
// <rtc-template block="module_spec">
#if RTM_MAJOR_VERSION >= 2
static const char* const co2_spec[] =
#else
static const char* co2_spec[] =
#endif
  {
    "implementation_id", "CO2Test",
    "type_name",         "CO2Test",
    "description",       "${rtcParam.description}",
    "version",           "1.0.0",
    "vendor",            "ISHIKAWA Y",
    "category",          "test",
    "activity_type",     "PERIODIC",
    "kind",              "DataFlowComponent",
    "max_instance",      "1",
    "language",          "C++",
    "lang_type",         "compile",
    ""
  };
// </rtc-template>

/*!
 * @brief constructor
 * @param manager Maneger Object
 */
CO2Test::CO2Test(RTC::Manager* manager)
    // <rtc-template block="initializer">
  : RTC::DataFlowComponentBase(manager),
    m_CO2inIn("CO2in", m_CO2in)

    // </rtc-template>
{
}

/*!
 * @brief destructor
 */
CO2Test::~CO2Test()
{
}



RTC::ReturnCode_t CO2Test::onInitialize()
{
  // Registration: InPort/OutPort/Service
  // <rtc-template block="registration">
  // Set InPort buffers
  addInPort("CO2in", m_CO2inIn);
  
  // Set OutPort buffer
  
  // Set service provider to Ports
  
  // Set service consumers to Ports
  
  // Set CORBA Service Ports
  
  // </rtc-template>

  // <rtc-template block="bind_config">
  // </rtc-template>
  
  return RTC::RTC_OK;
}

/*
RTC::ReturnCode_t CO2Test::onFinalize()
{
  return RTC::RTC_OK;
}
*/


//RTC::ReturnCode_t CO2Test::onStartup(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t CO2Test::onShutdown(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t CO2Test::onActivated(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t CO2Test::onDeactivated(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t CO2Test::onExecute(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t CO2Test::onAborting(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t CO2Test::onError(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t CO2Test::onReset(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t CO2Test::onStateUpdate(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t CO2Test::onRateChanged(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


bool CO2Test::runTest()
{
    return true;
}


extern "C"
{
 
  void CO2TestInit(RTC::Manager* manager)
  {
    coil::Properties profile(co2_spec);
    manager->registerFactory(profile,
                             RTC::Create<CO2Test>,
                             RTC::Delete<CO2Test>);
  }
  
}
