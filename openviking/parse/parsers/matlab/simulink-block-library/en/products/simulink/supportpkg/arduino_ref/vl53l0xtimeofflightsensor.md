---
type: simulink-block
title: 'VL53L0X Time of Flight Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Motor and Vehicle Sensors'
documentation_page: 'vl53l0xtimeofflightsensor'
documentation_source_path: 'supportpkg/arduino_ref/vl53l0xtimeofflightsensor.html'
language: en
---

# VL53L0X Time of Flight Sensor

## Ports

### Output

### **Distance** — Object distance vector

The **Distance** port outputs the target object
distance in millimeters

**Data Types:** `uint16`

## Parameters

### **I2C module** — I2C communication module `0` (default) | scalar

Specify the I2C module on the Arduino® hardware to communicate with sensor peripherals. For more
information on the Arduino pin mapping and modules that hardware boards support, see
Pin Mapping for Arduino Timer-Independent Blocks.

### **I2C address** — I2C address of sensor `0x29` (default)

The I2C address of the VL53L0X sensor from which the block reads the
values. You can configure this value. The range of I2C address is from
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

Specify how often this block reads the data from the VL53L0X sensor. When
you set this parameter to `-1`, Simulink determines the
best sample time for the block based on the block context within the
model.

## Libraries

Simulink Support Package for Arduino Hardware / Sensors Simulink Support Package for Raspberry Pi Hardware / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022a**

## Description

Measure distance to a target object

The VL53L0X Time of Flight Sensor block measures the distance to a
target object for a complete field of view (FOV = 25 degrees). This block also provides
the option to select one of four ranging modes based on your requirements.

**Note**

XSHUT connection is required for VL53L0X sensor. Connect the XSHUT pin to
vcc.

**Note**

The Monitor and Tune action (External mode) to tune parameter values of the
Simulink model is not supported, if the VL53L0X sensor is connected to boards such
as Arduino Uno, which have low memory.
