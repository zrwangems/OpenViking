---
type: simulink-block
title: 'ADXL34x Accelerometer'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Sensors'
documentation_page: 'adxl34xaccelerometer'
documentation_source_path: 'ref/adxl34xaccelerometer.html'
language: en
---

# ADXL34x Accelerometer

## Ports

### Output

### **Acceleration** — Linear acceleration measured by ADXL34x sensor vector

This port outputs the linear acceleration (in
m/s2) along the
*x*-, *y*- and
*z*-axes as a 1-by-3 array.

**Data Types:** `double`

**Note**

It is observed that there are many faulty cloned ADXL345 sensors available in
the market, with Z axis raw output becoming unresponsive. Buy the sensor from a
genuine distributor to avoid this issue.

## Parameters

### **I2C module** — Module for communication `I2C_A` (default)

The I2C module to be used for communication to the ADXL34x sensor. The
number of I2C modules supported varies across different C2000 processors.
You can find the supported I2C modules corresponding to the processor (which
you selected for the Hardware Board parameter in the Simulink model) by
opening the Configuration Parameters dialog box and checking the I2C
specific tabs under **Target hardware resources**.

### **I2C address** — I2C address of ADXL34x sensor `0x53` (default) | `0x1D`

The I2C address of the ADXL34x sensor from which the block reads the
values.

The ADXL34x sensor can have two I2C addresses depending on the logic level
on pin ALT of the sensor.

| Pin Name | Pin State | I2C Address |
| --- | --- | --- |
| ALT | Low | 0x53 |
| High | 0x1D |

### **Data type** — Output data type for values from ADXL34x sensor `single` (default) | `double`

Select the data type of the sensor from which the block reads the
values.

Specify the output data type for the values read from ADXL34x sensor. The
default data type for C2000 board is `single`. Use this
parameter to change the values to `double`, if
required.

### **Sample time** — Time interval to read data `-1` (default) | positive integer

Specify how often this block reads the data from the ADXL34x sensor. When
you set this parameter to `-1`, Simulink determines the
best sample time for the block based on the block context within the
model.

### Advanced settings

### **Accelerometer range** — Full scale for measuring linear acceleration `±4g` (default) | `±2g` | `±8g` | `±16g`

Select the range of acceleration that the accelerometer can
measure.

### **Accelerometer output data rate** — Rate at which accelerometer data is sampled `12.5 Hz` (default) | `0.1 Hz` | `0.2 Hz` | `0.39 Hz` | `0.78 Hz` | `1.56 Hz` | `3.13 Hz` | `6.25 Hz` | `25 Hz` | `50 Hz` | `100 Hz` | `200 Hz` | `400 Hz` | `800 Hz` | `1600 Hz`

Select the output data rate at which accelerometer data is
sampled.

### **Enable data ready interrupt** — Enable interrupt when data is ready `off` (default) | `on`

If this option is selected, an interrupt is generated on pin INT1 or
INT2 of the sensor when data is ready, allowing you to trigger other
subsystems to perform any action.

### **Interrupt generate pin** — Pin to generate data ready interrupt `INT1` (default) | `INT2`

Select the interrupt generate pin to read accelerometer data.

#### Dependencies

To enable this parameter, select the **Enable data ready
interrupt** parameter.

## Libraries

C2000 Microcontroller Blockset / Sensors Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Sensors Simulink Support Package for Arduino Hardware / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022a**

## Description

Measure linear acceleration along axes of ADXL34x family of accelerometers

The ADXL34x Accelerometer block reads data from the ADXL34x family of
accelerometers (ADXL343, ADXL344, ADXL345, and ADXL346) with C2000 board.

You can use this block to measure linear acceleration along the
*X*, *Y* and *Z*-axes. The
block also provides the option to enable the data ready interrupt.

The block outputs acceleration as a 1-by-3 array.
