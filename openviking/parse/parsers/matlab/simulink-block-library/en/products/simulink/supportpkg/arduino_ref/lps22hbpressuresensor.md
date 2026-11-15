---
type: simulink-block
title: 'LPS22HB Pressure Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Environmental Sensors'
documentation_page: 'lps22hbpressuresensor'
documentation_source_path: 'supportpkg/arduino_ref/lps22hbpressuresensor.html'
language: en
---

# LPS22HB Pressure Sensor

## Ports

### Output

### **Pressure** — Barometric air pressure as measured by LPS22HB sensor scalar

The block outputs the barometric air pressure in Pascals (Pa).

#### Dependencies

This output port appears only if you select the **Pressure
(Pa)** parameter.

**Data Types:** `double`

### **Temperature** — Temperature measured by LPS22HB sensor scalar

Temperature (in ℃) measured by LPS22HB sensor connected to Arduino board.

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

### **I2C address** — Peripheral addresses to communicate with sensors `0x5C` (default) | `0x5D`

The peripheral addresses to communicate with the LPS22HB sensor are decided by the
state of the SA0 pin on the hardware board. This table provides the peripheral addresses
corresponding to the pin and their state.

| Pin Name | Pin State | Peripheral Address |
| --- | --- | --- |
| SA0 | 0 | 0x5C |
| 1 | 0x5D |

### **Pressure (Pa)** — Set output port for reading pressure `on` (default) | `off`

Select this parameter to set **Pressure** as one of the output
ports.

### **Temperature (℃)** — Set output port for reading temperature `on` (default) | `off`

Select this parameter to set **Temperature** as one of the output
ports.

### **Status** — Set output port for obtaining status `off` (default) | `on`

Select this parameter to set **Status** as one of the output
ports.

### **Output data rate (ODR)** — Rate at which pressure data is sampled `1 Hz` (default) | `10 Hz` | `25 Hz` | `50 Hz` | `75 Hz`

Select the output data rate at which pressure data is sampled, which also determines
the bandwidth.

### **Enable low pass filter** — Enable low pass filter for pressure data `off` (default) | `on`

Enable the low pass filter for reading pressure values.

### **Select the bandwidth** — Bandwidth of low pass filter `ODR/9` (default) | `ODR/20`

Select the required bandwidth of the low pass filter.

#### Dependencies

This parameter appears only if you select the **Enable low pass
filter** parameter.

### **Sample time** — Time interval to read data `-1` (default) | positive integer

Specify how often this block reads the data from the LPS22HB sensor. When you set
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

Measure barometric air pressure and temperature from LPS22HB sensor

The LPS22HB Pressure Sensor block measures barometric air pressure using
the LPS22HB pressure sensor interfaced with the Arduino® hardware. This sensor comprises of a sensing element to measure the absolute
pressure. The block also measures the temperature from the embedded temperature sensor in
LPS22HB Sensor.

You can also select an output data rate in the block, and use the low pass filter option
for filtering the measured pressure values.

**Note**

If you are using Arduino Nano 33 BLE Sense hardware, which always includes an embedded
sensor, reading data from a breakout board containing LPS22HB sensor is not supported.
