---
type: simulink-block
title: 'BME68x Gas Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Environmental Sensors'
documentation_page: 'bme68xgassensor'
documentation_source_path: 'supportpkg/arduino_ref/bme68xgassensor.html'
language: en
---

# BME68x Gas Sensor

## Ports

### Output

### **Pressure** — Barometric air pressure scalar

The block outputs barometric air pressure in Pascal (Pa).

#### Dependencies

This output port appears only if you select the **Pressure
(Pa)** parameter.

**Data Types:** `single`

### **Temperature** — Ambient temperature scalar

The block outputs the ambient temperature in ℃.

#### Dependencies

This output port appears only if you select the **Temperature
(℃)** parameter.

**Data Types:** `single`

### **Humidity** — Relative humidity scalar

The block outputs the relative humidity in `%`.

#### Dependencies

This output port appears only if you select the **Humidity
(%)** parameter.

**Data Types:** `single`

### **IAQ** — Index for air quality scalar

The block outputs the index for indoor air quality in parts per million
(ppm).

#### Dependencies

This output port appears only if you select the **IAQ**
parameter.

**Data Types:** `single`

### **IAQStatus** — Status of IAQ values `0` | `1`

The block outputs the status of index for indoor air quality measurement.
`0` indicates that the IAQ data read is new, `1`
indicates that the IAQ data read is not new.

#### Dependencies

This output port appears only if you select **IAQ** and
**IAQStatus** parameters.

**Data Types:** `uint8`

### **eCO2** — Equivalent CO2 scalar

The **eCO2** port outputs the value for
equivalent CO2 of indoor air in parts per million (ppm).

#### Dependencies

This output port appears only if you select the
**eCO2** parameter.

**Data Types:** `single`

### **bVOC** — Breadth volatile organic compound concentration scalar

The **bVOC** port outputs the equivalent breadth volatile organic
compound concentration of indoor air in parts per million (ppm).

#### Dependencies

This output port appears only if you select the **bVOC**
parameter.

**Data Types:** `single`

## Parameters

### **I2C module** — I2C communication module `0` (default) | scalar

Specify the I2C module on the Arduino hardware to communicate with sensor peripherals. For more information on
the Arduino pin mapping and modules that hardware boards support, see Pin Mapping for Arduino Timer-Independent Blocks.

### **I2C address** — I2C address to communicate with sensor peripherals `0x77` (default) | `0x76`

The I2C addresses to communicate with the peripheral on the BME68x sensor are
decided by the state of the SD0 pin on the Arduino Mega 2560 board. This table provides
the I2C addresses corresponding to the pin and their state.

| Pin Name | Pin State | I2C address |
| --- | --- | --- |
| SD0 | 0 | 0x76 |
| 1 | 0x77 |

### **Mode** — Power mode of the sensor `Low power (ODR = 0.33Hz)` (default) | `Continuous (ODR = 1Hz)` | `Ultra low power (ODR = 3.3mHz)`

Select the power mode of the sensor based on the power supply you have.

### **Pressure (Pa)** — Set output port for reading pressure `on` (default) | `off`

Select this parameter to set **Pressure** as one of the output
ports.

### **Temperature (℃)** — Set output port for reading temperature `on` (default) | `off`

Select this parameter to set **Temperature** as one of the output
ports.

### **Humidity(%)** — Set output port for reading humidity `on` (default) | `off`

Select this parameter to set **Humidity** as one of the output
ports.

### **IAQ** — Set output port for reading index of air quality `on` (default) | `off`

Select this parameter to set **IAQ** as one of the output
ports.

### **IAQStatus** — Set output port for reading IAQ status `off` (default) | `on`

Select this parameter to set **IAQStatus** as one of the output
ports.

### **eCO2** — Set output port for reading equivalent carbon dioxide concentration `off` (default) | `on`

Select this parameter to set **eCO2** as one of the output
ports.

### **bVOC** — Set output port for reading breadth volatile organic compound concentration `off` (default) | `on`

Select this parameter to set **bVOC** as one of the output
ports.

### **Sample time** — Time interval to read data `-1` (default) | positive integer

Specify how often this block reads the data from the BME68x sensor. When you set
this parameter to -1, Simulink determines the best sample time for the block based on
the block context within the model.

## Libraries

Simulink Support Package for Arduino Hardware / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022b**

## Description

Measure barometric air pressure, relative humidity, ambient temperature, IAQ, eCO2, and bVOC from BME68x sensor

The BME68x Gas Sensor block measures barometric air pressure, relative
humidity, ambient temperature, index for air quality (IAQ), index for air quality status
(IAQStatus), equivalent carbon dioxide concentration (eCO2), and breath volatile organic
compound concentration (bVOC) using the BME68x Gas sensor interfaced with the Arduino® Mega 2560 boards.

**Note**

The BME68x Gas sensor supports reading data only from Arduino Mega 2560 boards.

**Note**

The BME68x Gas Sensor takes around `5` minutes to output the values for
index for air quality (IAQ).
