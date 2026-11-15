---
type: simulink-block
title: 'BMM150 Magnetometer'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sensors / IMU Sensors'
documentation_page: 'bmm150magnetometer'
documentation_source_path: 'supportpkg/raspberrypi_ref/bmm150magnetometer.html'
language: en
---

# BMM150 Magnetometer

## Ports

### Output

### **Magnetic Field** — Magnetic field strength measured by a BMM150 sensor row vector

Magnetic field strength (in µT) measured by a BMM150 sensor connected to
Raspberry Pi board, along the x-, y- and z- axes, specified as a row vector
[x,y,z].

**Data Types:** `double`

### **Magnetic Field Status** — Status of magnetic field value `0` | `1`

Status of magnetic field `0` indicates that the data read is new
and `1` indicates that the data read is not new.

#### Dependencies

This output port appears only if you select the **Status**
parameter.

**Data Types:** `int8`

## Parameters

### **I2C module** — Module for communication `1` (default)

Specify the module on the board that you are using for I2C communication.

### **I2C address** — I2C address of BMM150 sensor `0x13` (default) | `0x10` | `0x11` | `0x12`

The I2C address used by BMM150 sensor communicating with the Raspberry Pi processor. The default parameter value (`0x13`)
corresponds to the value mentioned in the `Schematics` section of the
BOOSTXL-SENSORS BoosterPackTM Plug-in Module User's
Guide.

### **Status** — Set output port for obtaining magnetic field status `on` (default) | `off`

Select this parameter to set **Magnetic Field Status** as one of
the output ports.

### **Preset value** — Preset value for the operating condition of BMM150 sensor `Low power` (default) | `Regular` | `Enhanced` | `High accuracy`

Specify the preset value for the operating condition of BMM150 sensor while reading
the values. The selection of one of the four preset values affects the electrical
characteristics (like supply current) and the required output accuracy with respect to
ODR and output noise.

### **Data type** — Output data type for values from BMM150 sensor `single` (default) | `double`

Specify the output data type for the values read from BMM150 sensor. The default
data type for Raspberry Pi processors is `single`. Use this parameter to change the
values to `double`, if required.

### **Sample time** — Time interval to read data `-1` (default) | positive integer

Specify how often this block reads the data from the BMM150 sensor. When you set
this parameter to -1, Simulink determines the best sample time for the block based on
the block context within the model.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Sensors / IMU Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022b**

## Description

Measure magnetic field from BMM150 sensor

The BMM150 block outputs the values of magnetic field along x-, y- and z-
axes as measured by the BMM150 sensor connected to Raspberry Pi® board.
