---
type: simulink-block
title: 'LIS3MDL Magnetometer Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sensors / IMU Sensors'
documentation_page: 'lis3mdlmagnetometersensor'
documentation_source_path: 'supportpkg/raspberrypi_ref/lis3mdlmagnetometersensor.html'
language: en
---

# LIS3MDL Magnetometer Sensor

## Ports

### Output

### **Magnetic Field** — Magnetic field strength measured by LIS3MDL sensor row vector

Magnetic field strength (in µT) measured by LIS3MDL sensor connected to
Raspberry Pi board, along the x-, y- and z- axes, specified as a row vector
[x,y,z].

#### Dependencies

This output port appears only if you select the **Magnetic Field
(µT)** parameter.

**Data Types:** `double`

### **Temperature** — Temperature measured by LIS3MDL sensor scalar

Temperature (in ℃) measured by LIS3MDL sensor connected to Raspberry Pi board.

#### Dependencies

This output port appears only if you select the **Temperature
(℃)** parameter.

**Data Types:** `double`

### **Status** — Status of magnetic and temperature measurements `-1` | `0` | `1`

Status of magnetic and temperature measurements, specified as a 1-by-2 vector.
`0` indicates that the data read is new, `1`
indicates that the data read is not new, and `-1` indicates that the
corresponding output is not selected.

#### Dependencies

This output port appears only if you select the **Status**
parameter.

**Data Types:** `int8`

## Parameters

#### Main Tab

### **Use onboard sensors** — Enable to use onboard sensors `on` (default) | `off`

Select this parameter to use onboard sensors.

### **I2C module** — Specify I2C module `2` (default) | `positive integer`

Specify the I2C module on the board. The I2C bus frequency, serial clock (SCL) pin
and serial data (SDA) pin are taken according to the corresponding I2C module entry in
the configuration parameters.

#### Dependencies

To enable this parameter, clear the **Use onboard sensors**
parameter.

### **Magnetic Field (µT)** — Set output port for reading magnetic field `on` (default) | `off`

Select this parameter to set **Magnetic Field** as one of the
output ports.

### **Temperature (℃)** — Set output port for reading temperature `on` (default) | `off`

Select this parameter to set **Temperature** as one of the output
ports.

### **Magnetic Field Status** — Set output port for obtaining magnetic field status `off` (default) | `on`

Select this parameter to set **Magnetic Field Status** as one of
the output ports.

### **Sample time** — Time interval to read data `-1` (default) | positive integer

Specify how often this block reads the data from the LIS3MDL sensor. When you set
this parameter to -1, Simulink determines the best sample time for the block based on
the block context within the model.

#### Advanced Tab

### **Magnetometer range** — Full scale for measuring magnetic range `±2g` (default) | `±4g` | `±8g`

Select the full scale for measuring linear acceleration (the range of acceleration
that the sensor needs to measure).

### **Magnetometer output data rate** — Rate at which magnetometer data is sampled `0.625 Hz` (default) | `1.25 Hz` | `2.5 Hz` | `5 Hz` | `10 Hz` | `20 Hz` | `40 Hz` | `80 Hz`

Select the output data rate at which magnetometer data is sampled.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Sensors / IMU Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022b**

## Description

Measure magnetic field strength and temperature from LIS3MDL Magnetometer sensor

The LIS3MDL Magnetometer Sensor block outputs the values of magnetic field
strength along x-, y- and z- axes as measured by the LIS3MDL Magnetometer sensor connected to
Raspberry Pi® board. The block also outputs the temperature as read by the LIS3MDL
Magnetometer sensor.
