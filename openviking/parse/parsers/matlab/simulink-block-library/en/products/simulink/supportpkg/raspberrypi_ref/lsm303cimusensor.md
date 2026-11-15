---
type: simulink-block
title: 'LSM303C IMU Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sensors / IMU Sensors'
documentation_page: 'lsm303cimusensor'
documentation_source_path: 'supportpkg/raspberrypi_ref/lsm303cimusensor.html'
language: en
---

# LSM303C IMU Sensor

## Ports

### Output

### **Acceleration** — Linear acceleration measured by LSM303C sensor row vector

Linear acceleration (in m/s2) measured by LSM303C
sensor connected to Raspberry Pi board, along the x-, y- and z- axes, specified as a row vector
[x,y,z].

#### Dependencies

This output port appears only if you select the **Acceleration
(m/s2)** parameter.

**Data Types:** `double`

### **Magnetic Field** — Magnetic field strength measured by LSM303C sensor row vector

Magnetic field strength (in µT) measured by LSM303C sensor connected to
Raspberry Pi board, along the x-, y- and z- axes, specified as a row vector
[x,y,z].

#### Dependencies

This output port appears only if you select the **Magnetic Field
(µT)** parameter.

**Data Types:** `double`

### **Temperature** — Temperature measured by LSM303C sensor scalar

Temperature (in ℃) measured by LSM303C sensor connected to Raspberry Pi board.

#### Dependencies

This output port appears only if you select the **Temperature
(℃)** parameter.

**Data Types:** `double`

### **Acceleration Status** — Status of acceleration value `0` | `1`

Status of acceleration value along the three axes, specified as a row vector in
the order [z,y,x], to indicate if the data read is the new value or not.
`0` indicates that the data read is new and `1`
indicates that the data read is not new.

#### Dependencies

This output port appears only if you select the **Acceleration
Status** parameter.

**Data Types:** `Boolean`

### **Magnetic Field Status** — Status of magnetic field value `0` | `1`

Status of magnetic field value along the three axes, specified as a row vector in
the order [z,y,x], to indicate if the data read is the new value or not.
`0` indicates that the data read is new and `1`
indicates that the data read is not new.

#### Dependencies

This output port appears only if you select the **Magnetic Field
Status** parameter.

**Data Types:** `double`

## Parameters

#### Main Tab

### **I2C module** — Module for communication `1` (default)

Specify the module on the board that you are using for I2C communication.

### **Acceleration (m/s2)** — Set output port for reading acceleration `on` (default) | `off`

Select this parameter to set **Acceleration** as one of the output
ports.

### **Magnetic Field (µT)** — Set output port for reading magnetic field `on` (default) | `off`

Select this parameter to set **Magnetic Field** as one of the
output ports.

### **Temperature (℃)** — Set output port for reading temperature `on` (default) | `off`

Select this parameter to set **Temperature** as one of the output
ports.

### **Acceleration Status** — Set output port for obtaining acceleration status `off` (default) | `on`

Select this parameter to set **Acceleration Status** as one of the
output ports.

### **Magnetic Field Status** — Set output port for obtaining magnetic field status `off` (default) | `on`

Select this parameter to set **Magnetic Field Status** as one of
the output ports.

### **Sample time** — Time interval to read data `-1` (default) | positive integer

Specify how often this block reads the data from the LSM303 sensor. When you set
this parameter to -1, Simulink determines the best sample time for the block based on
the block context within the model.

#### Advanced Tab

### **Accelerometer range** — Full scale for measuring linear acceleration `±2g` (default) | `±4g` | `±8g`

Select the full scale for measuring linear acceleration (the range of acceleration
that the sensor needs to measure).

### **Accelerometer output data rate** — Rate at which accelerometer data is sampled `10 Hz` (default) | `50 Hz` | `100 Hz` | `200 Hz` | `400 Hz` | `800 Hz`

Select the output data rate at which accelerometer data is sampled, which also
determines the bandwidth.

### **Magnetometer range** — Full scale for measuring magnetic field `±16 gauss` (default)

Select the full scale for measuring magnetic field.

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

Measure linear acceleration, magnetic field strength, and temperature from LSM303C sensor

The LSM303C IMU Sensor block outputs the values of linear acceleration and
magnetic field strength along x-, y- and z- axes as measured by the LSM303C sensor connected
to Raspberry Pi® board. The block also outputs the temperature as read by the LSM303C
sensor.
