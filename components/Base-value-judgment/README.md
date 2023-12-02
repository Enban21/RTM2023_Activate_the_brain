# Base_value_judgment

## Overview

ModuleDescription

## Description

CO2から受け取ったデータをもとに計算を行う。受け取ったデータが基準値を超過しそうになると、LEDへと信号が出力される。信号を受け取った赤色LEDはゆっくりと点滅をする。その後、受け取ったデータが基準値を超過した場合、新たな信号が出力される。信号を受け取った赤色LEDが高速点滅する。<br/>警告確認後、喚気が行われ、受け取ったデータが基準値を下回ると、LEDからの信号出力が停止され、赤色LEDが消灯する。

### Input and Output



### Algorithm etc



### Basic Information

|  |  |
----|---- 
| Module Name | Base_value_judgment |
| Description | ModuleDescription |
| Version | 1.0.0 |
| Vendor | ISHUKAWA Y |
| Category | test |
| Comp. Type | STATIC |
| Act. Type | PERIODIC |
| Kind | DataFlowComponent |
| MAX Inst. | 1 |

### Activity definition

<table>
  <tr>
    <td rowspan="4">on_initialize</td>
    <td colspan="2">implemented</td>
    <tr>
      <td>Description</td>
      <td></td>
    </tr>
    <tr>
      <td>PreCondition</td>
      <td></td>
    </tr>
    <tr>
      <td>PostCondition</td>
      <td></td>
    </tr>
  </tr>
  <tr>
    <td>on_finalize</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_startup</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_shutdown</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td rowspan="4">on_activated</td>
    <td colspan="2">implemented</td>
    <tr>
      <td>Description</td>
      <td>CO2から受け取ったデータをもとに計算を行う。受け取ったデータが基準値を超過しそうになると、LEDへと信号が出力される。信号を受け取った赤色LEDはゆっくりと点滅をする。その後、受け取ったデータが基準値を超過した場合、新たな信号が出力される。信号を受け取った赤色LEDが高速点滅する。<br/>警告確認後、喚気が行われ、受け取ったデータが基準値を下回ると、LEDからの信号出力が停止され、赤色LEDが消灯する。</td>
    </tr>
    <tr>
      <td>PreCondition</td>
      <td></td>
    </tr>
    <tr>
      <td>PostCondition</td>
      <td></td>
    </tr>
  </tr>
  <tr>
    <td>on_deactivated</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td rowspan="4">on_execute</td>
    <td colspan="2">implemented</td>
    <tr>
      <td>Description</td>
      <td></td>
    </tr>
    <tr>
      <td>PreCondition</td>
      <td></td>
    </tr>
    <tr>
      <td>PostCondition</td>
      <td></td>
    </tr>
  </tr>
  <tr>
    <td>on_aborting</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_error</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_reset</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_state_update</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_rate_changed</td>
    <td colspan="2"></td>
  </tr>
</table>

### InPorts definition

#### CO2_In



<table>
  <tr>
    <td>DataType</td>
    <td>RTC::TimedShort</td>
    <td></td>
  </tr>
  <tr>
    <td>IDL file</td>
    <td colspan="2">BasicDataType.idl</td>
  </tr>
  <tr>
    <td>Number of Data</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Semantics</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Unit</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Occirrence frecency Period</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Operational frecency Period</td>
    <td colspan="2"></td>
  </tr>
</table>


### OutPorts definition

#### LED_Out



<table>
  <tr>
    <td>DataType</td>
    <td>RTC::TimedShort</td>
    <td></td>
  </tr>
  <tr>
    <td>IDL file</td>
    <td colspan="2">BasicDataType.idl</td>
  </tr>
  <tr>
    <td>Number of Data</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Semantics</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Unit</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Occirrence frecency Period</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Operational frecency Period</td>
    <td colspan="2"></td>
  </tr>
</table>


### Service Port definition


### Configuration definition


## Demo

## Requirement

## Setup

### Windows

### Ubuntu

## Usage

## Running the tests

## LICENCE




## References




## Author


