---
type: simulink-block
title: 'HTS221 Humidity Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Environmental Sensors'
documentation_page: 'hts221humiditysensor'
documentation_source_path: 'supportpkg/arduino_ref/hts221humiditysensor.html'
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

Temperature (in ℃) measured by HTS221 sensor connected to Arduino board.

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

### **I2C module** — I2C communication module `0` (default) | scalar

Specify the I2C module on the Arduino hardware to communicate with sensor peripherals. For more information on
the Arduino pin mapping and modules that hardware boards support, see Pin Mapping for Arduino Timer-Independent Blocks.

### **I2C address** — Peripheral address to communicate with sensor `0x5F` (default) | scalar

The peripheral address for the HTS221 sensor to communicate with the Arduino hardware.

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

Simulink Support Package for Arduino Hardware / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021a**

## Description

Measure relative humidity and temperature from HTS221 sensor

The HTS221 Humidity Sensor block measures relative humidity and ambient
temperature using the HTS221 humidity sensor interfaced with the Arduino® hardware. This sensor comprises of a sensing element to measure the relative
humidity and temperature.

You can also select an output data rate for the measured values in the block.

**Note**

If you are using Arduino Nano 33 BLE Sense hardware, which always includes an embedded
sensor, reading data from a breakout board containing HTS221 sensor is not supported.
