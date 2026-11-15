---
type: simulink-block
title: 'CCS811 Air Quality Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Environmental Sensors'
documentation_page: 'ccs811airqualitysensor'
documentation_source_path: 'supportpkg/arduino_ref/ccs811airqualitysensor.html'
language: en
---

# CCS811 Air Quality Sensor

## Ports

### Output

### **eCO2** — Equivalent CO2 scalar

The **eCO2** port outputs the
value for equivalent CO2 of indoor air in parts
per million (ppm).

**Data Types:** `single` | `double`

### **eTVOC** — Total volatile organic compound concentration scalar

The **eTVOC** port outputs the equivalent total
volatile organic compound concentration of indoor air in parts per
billion (ppb).

**Data Types:** `single` | `double`

### **Status** — Status of values read for eCO2 and eTVOC `0` | `1`

Status of the values `0` indicates that the data read
for eCO2 and eTVOC is new and
`1` indicates that the data read is not new.

**Data Types:** `uint8`

## Parameters

### **I2C module** — I2C communication module `0` (default) | scalar

Specify the I2C module on the Arduino® hardware to communicate with sensor peripherals. For more
information on the Arduino pin mapping and modules that hardware boards support, see
Pin Mapping for Arduino Timer-Independent Blocks.

### **I2C address** — I2C address of sensor `0x5A` (default) | `0x5B`

The I2C address of the CCS811 sensor from which the block reads the
values.

The I2C address of the CCS811 sensor from which the block reads the
values. The CCS811 sensor can have two I2C addresses depending on the logic
level on pin ADDR of the sensor.

| Pin Name | Pin State | I2C Address |
| --- | --- | --- |
| ADDR | Low | 0x5A |
| High | 0x5B |

### **Data acquisition interval (s)** — Intervals for data acquisition `1` (default) | `0.25` | `10` | `60`

Select the data acquisition interval in seconds for the sensor to read
data. For example, if you select value `1`, then the sensor
reads values every `1` second.

### **Specify environmental conditions** — Environmental conditions `Mask dialog` (default) | `External sensor`

Select the option to specify the source of environmental inputs for the
sensor while reading data.

### **Humidity (%)** — Humidity input to CCS811 sensor `50` (default) | `positive integer`

Humidity in percentage provided as an input to CCS811 sensor connected to
Arduino hardware.

#### Dependencies

This parameter appears only if you select `Mask
dialog` for **Specify environmental
conditions** parameter.

### **Temperature (oC)** — Temperature input to CCS811 sensor `25` (default) | `positive integer`

Temperature (in ℃) provided as an input to CCS811 sensor connected to
Arduino hardware.

#### Dependencies

This parameter appears only if you select `Mask
dialog` for **Specify environmental
conditions** parameter.

### **Enable data ready interrupt** — Enable interrupt when data is ready `off` (default) | `on`

If this option is selected, an interrupt is generated on pin nINT of the
sensor when data is ready, allowing you to trigger other subsystems to
perform any action.

### **Data type** — Type of output data `double` (default) | `single`

Select the data type for output.

### **Sample time** — Time interval to read data `-1` (default) | positive integer

Specify how often this block reads the data from the CCS811 sensor. When
you set this parameter to -1, Simulink determines the best sample time for
the block based on the block context within the model.

## Libraries

Simulink Support Package for Arduino Hardware / Sensors Simulink Support Package for Raspberry Pi Hardware / Sensors / Environmental Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022a**

## Description

Measure equivalent CO 2 (eCO 2 ) and the equivalent total volatile organic compound concentration (eTVOC)

The CCS811 Air Quality Sensor block measures the equivalent
CO2 (eCO2) and the equivalent total
volatile organic compound concentration (eTVOC) for indoor air quality monitoring. This
block also provides the option to provide temperature and humidity data to enable
compensation (either by specifying the humidity and temperature values or by interfacing
CCS811 with an external sensor).
