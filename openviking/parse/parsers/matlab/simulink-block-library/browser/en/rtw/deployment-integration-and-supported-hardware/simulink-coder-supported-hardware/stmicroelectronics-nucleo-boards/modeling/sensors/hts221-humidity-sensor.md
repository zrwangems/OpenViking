---
type: simulink-block
title: 'HTS221 Humidity Sensor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Sensors'
documentation_page: 'hts221humiditysensor'
documentation_source_path: 'nucleo/ref/hts221humiditysensor.html'
language: en
---

# HTS221 Humidity Sensor

## Ports

### Output

### **Humidity** — Relative humidity as measured by HTS221 sensor scalar

The block outputs the relative humidity in percentage (%).

#### Dependencies

This output port appears only if you select the **Humidity
(%)** parameter.

**Data Types:** `double`

### **Temperature** — Temperature measured by HTS221 sensor scalar

#### Dependencies

This output port appears only if you select the **Temperature
(℃)** parameter.

**Data Types:** `double`

### **Status** — Status of pressure and temperature measurements `0` | `1` | `-1`

Status of pressure and temperature measurements, specified as a 1-by-2 vector.
`0` indicates that the data read is new, `1`
indicates that the data read is not new, and `-1` indicates that the
corresponding output is not selected.

#### Dependencies

This output port appears only if you select the **Status**
parameter.

**Data Types:** `int8`

## Parameters

### **I2C module** — Specify I2C module `2` (default) | `positive integer`

Specify the I2C module on the board. The I2C bus frequency, serial clock (SCL) pin
and serial data (SDA) pin are taken according to the corresponding I2C module entry in
the configuration parameters.

### **Humidity (%)** — Set output port for reading humidity `on` (default) | `off`

Select this parameter to set **Humidity** as one of the output
ports.

### **Temperature (℃)** — Set output port for reading temperature `on` (default) | `off`

Select this parameter to set **Temperature** as one of the output
ports.

### **Status** — Set output port for obtaining status `off` (default) | `on`

Select this parameter to set **Status** as one of the output
ports.

### **Output data rate (ODR)** — Rate at which humidity and temperature data is sampled `1 Hz` (default) | `7 Hz` | `12.5 Hz`

Select the output data rate at which humidity data is sampled.

### **Sample time** — Time interval to read data `-1` (default) | positive integer

Specify how often this block reads the data from the HTS221 sensor. When you set
this parameter to -1, Simulink determines the best sample time for the block based on
the block context within the model.

## Libraries

Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

## Description

Measure relative humidity and temperature from HTS221 sensor

The HTS221 Humidity Sensor block measures relative humidity and ambient
temperature using the HTS221 humidity sensor interfaced with the Nucleo/STM32L475-Discovery
board. This sensor comprises of a sensing element to measure the relative humidity and
temperature.

You can also select an output data rate for the measured values in the block.
