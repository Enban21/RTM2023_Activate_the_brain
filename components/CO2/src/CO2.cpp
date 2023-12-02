// -*- C++ -*-
// <rtc-template block="description">
/*!
 * @file  CO2.cpp
 * @brief ${rtcParam.description}
 *
 */
// </rtc-template>

#include "CO2.h"

// Module specification
// <rtc-template block="module_spec">
#if RTM_MAJOR_VERSION >= 2
static const char* const co2_spec[] =
#else
static const char* co2_spec[] =
#endif
  {
    "implementation_id", "CO2",
    "type_name",         "CO2",
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
CO2::CO2(RTC::Manager* manager)
    // <rtc-template block="initializer">
  : RTC::DataFlowComponentBase(manager),
    m_CO2inOut("CO2in", m_CO2in)
    // </rtc-template>
{
}

/*!
 * @brief destructor
 */
CO2::~CO2()
{
}



RTC::ReturnCode_t CO2::onInitialize()
{
  // Registration: InPort/OutPort/Service
  // <rtc-template block="registration">
  // Set InPort buffers
  
  // Set OutPort buffer
  addOutPort("CO2in", m_CO2inOut);

  
  // Set service provider to Ports
  
  // Set service consumers to Ports
  
  // Set CORBA Service Ports
  
  // </rtc-template>

  // <rtc-template block="bind_config">
  // </rtc-template>

  
  return RTC::RTC_OK;
}

/*
RTC::ReturnCode_t CO2::onFinalize()
{
  return RTC::RTC_OK;
}
*/


//RTC::ReturnCode_t CO2::onStartup(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t CO2::onShutdown(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t CO2::onActivated(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t CO2::onDeactivated(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t CO2::onExecute(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t CO2::onAborting(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t CO2::onError(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t CO2::onReset(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t CO2::onStateUpdate(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}


//RTC::ReturnCode_t CO2::onRateChanged(RTC::UniqueId /*ec_id*/)
//{
//  return RTC::RTC_OK;
//}



extern "C"
{
 
  void CO2Init(RTC::Manager* manager)
  {
    coil::Properties profile(co2_spec);
    manager->registerFactory(profile,
                             RTC::Create<CO2>,
                             RTC::Delete<CO2>);
  }
  
}
