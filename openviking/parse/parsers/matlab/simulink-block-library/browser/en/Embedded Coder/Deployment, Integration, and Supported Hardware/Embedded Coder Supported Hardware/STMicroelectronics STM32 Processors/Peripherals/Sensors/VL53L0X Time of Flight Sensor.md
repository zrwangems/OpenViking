---
type: simulink-block
title: 'VL53L0X Time of Flight Sensor'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Sensors'
documentation_page: 'vl53l0xtimeofflightsensor'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/vl53l0xtimeofflightsensor.html'
language: en
---

# VL53L0X Time of Flight Sensor

## Ports

### Output

### **Distance** — Object distance vector

The **Distance** port outputs the target object distance in
millimeters

**Data Types:** `uint16`

## Parameters

### **I2C module** — Module for communication `0` (default)

Specify the module on the board that you are using for I2C
communication.

### **I2C address** — I2C address of sensor `0x29` (default)

The I2C address of the VL53L0X sensor from which the block reads the values.
You can configure this value. The range of I2C address is from
`0x08` to `0x77`.

### **Ranging Mode** — Distance ranging mode of VL53L0X sensor `Default` (default) | `High accuracy` | `Long range` | `High speed`

Select the distance ranging mode for measuring the distance to the target
object. The four ranging modes available are shown in this table.

| Ranging mode | Timing budget | Typical max range | Typical application |
| --- | --- | --- | --- |
| Default | 30 ms | 1.2 m | standard |
| High accuracy | 200 ms | 2 m | precise measurement |
| Long range | 33 ms | 1.2 m | long ranging for dark conditions |
| High speed | 20 ms | 1.2 m | high speed where accuracy is not priority |

The timing budget is the time taken by the sensor to perform one range
measurement.

### **Sample time** — Time interval to read data `-1` (default) | positive integer

Specify how often this block reads the data from the VL53L0X sensor. When you
set this parameter to `-1`, Simulink® determines the best sample time for the block based on the block
context within the model.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / Sensors / IMU Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

Measure distance to a target object

The VL53L0X Time of Flight Sensor block measures the distance to a
target object for a complete field of view (FOV = 25 degrees). This block also provides the
option to select one of four ranging modes based on your requirements.

**Note**

XSHUT connection is required for VL53L0X sensor. Connect the XSHUT pin to vcc.
