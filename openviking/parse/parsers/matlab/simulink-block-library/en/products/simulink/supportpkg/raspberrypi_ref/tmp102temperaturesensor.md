---
type: simulink-block
title: 'TMP102 Temperature Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sensors / Environmental Sensors'
documentation_page: 'tmp102temperaturesensor'
documentation_source_path: 'supportpkg/raspberrypi_ref/tmp102temperaturesensor.html'
language: en
---

# TMP102 Temperature Sensor

## Ports

### Output

### **Temperature** — Ambient temperature in degree Celsius scalar

The port outputs ambient temperature that the TMP102 sensor reads in degree
Celsius.

**Data Types:** `double`

## Parameters

### Main

### **I2C module** — I2C communication module `1` (default) | scalar

Specify the I2C module on the Raspberry Pi® hardware to communicate with the TMP102 sensor.

To enable the secondary I2C bus on your Raspberry Pi hardware, follow the steps as mentioned in Enable Secondary I2C Bus of Raspberry Pi Hardware.

### **I2C address** — I2C peripheral address `0x48` (default) | `0x49` | `0x4A` | `0x4B`

Specify the I2C peripheral device address from which you want to read the TMP102
temperature data.

You can connect up to four TMP102 temperature sensors to your Raspberry Pi hardware. The I2C address for the sensor connection is dependent on the
state of the ADD0 pin of the sensor. This table provides the I2C addresses and their
corresponding ADD0 pin connection details.

| Raspberry Pi Pin Connection | I2C Address |
| --- | --- |
| GND | 0x48 |
| VCC | 0x49 |
| SDA | 0x4A |
| SCL | 0x4B |

### **Sample time** — Time frequency `1` (default) | positive integer

Specify the frequency at which the block reads the temperature values from the
TMP102 sensor.

### Advanced

### **Temperature alert limits (oC)** — Temperature threshold limits for sensor [`16`,`60`] (default) | scalar

Enter the minimum and maximum temperature threshold limits to generate a signal on
the alert pin of the TMP102 sensor when the ambient temperature equals or exceeds the
maximum threshold value.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Sensors / Environmental Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024b**

## Description

Read ambient temperature in degree Celsius using TMP102 temperature sensor

Use the TMP102 Temperature Sensor block to read ambient temperature values
from a TMP102 sensor, in degree Celsius.
