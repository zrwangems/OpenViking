---
type: simulink-block
title: 'BME280 Pressure Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sensors / Environmental Sensors'
documentation_page: 'bme280pressuresensor'
documentation_source_path: 'supportpkg/raspberrypi_ref/bme280pressuresensor.html'
language: en
---

# BME280 Pressure Sensor

## Ports

### Output

### **Pressure** — Barometric air pressure measured by BME280 sensor scalar

Barometric air pressure (in Pascal (Pa)) measured by a BME280 sensor that is
connected to Raspberry Pi board.

#### Dependencies

This output port appears only if you select the **Pressure
(Pa)** parameter.

**Data Types:** `double`

### **Temperature** — Temperature measured by BME280 sensor scalar

Temperature (in ℃) measured by BME280 sensor connected to Raspberry Pi board.

#### Dependencies

This output port appears only if you select the **Temperature
(℃)** parameter.

**Data Types:** `double`

### **Humidity** — Relative humidity measured by BME280 sensor scalar

Relative humidity (in %) measured by BME280 sensor connected to Raspberry Pi board.

#### Dependencies

This output port appears only if you select the **Humidity
(%)** parameter.

**Data Types:** `double`

### **Status** — Status of read values `0` | `1`

Status of read values from the BME280 sensor, to indicate if the data read is the
new value or not. The **Status** value of `0`
indicates that the data read is new and `1` indicates that the data
read is not new.

#### Dependencies

This output port appears only if you select the **Status**
parameter.

**Data Types:** `uint8`

## Parameters

### **I2C module** — Module for communication `1` (default)

Specify the module on the board that you are using for I2C communication.

### **I2C address** — I2C address of BME280 sensor `0x76` (default) | `0x77`

The I2C address used by BME280 sensor communicating with the Raspberry Pi board.

### **Pressure (Pa)** — Set output port for reading pressure `on` (default) | `off`

Select this parameter to set **Pressure** as one of the output
ports.

### **Temperature (℃)** — Set output port for reading temperature `on` (default) | `off`

Select this parameter to set **Temperature** as one of the output
ports.

### **Humidity (%)** — Set output port for reading humidity `on` (default) | `off`

Select this parameter to set **Humidity** as one of the output
ports.

### **Status** — Set output port for obtaining status of values read `off` (default) | `on`

Select this parameter to set **Status** as one of the output
ports.

### **Filter coefficient** — Filter coefficient for IIR filter `0` (default) | `2` | `4` | `8` | `16`

Specify filter coefficient for the IIR filter while reading pressure and temperature
values from BME280 sensor. Selecting a non-zero value for filter coefficient helps to
improve the step response and remove short-term fluctuations in the measured
values.

### **Stand by time** — Standby time to read values `0.5` (default) | `10` | `20` | `62.5` | `125` | `250` | `500` | `1000`

Specify the standby time (in ms) when the processor stays idle (inactive duration)
while reading values from BME280 sensor. The selection of this value affects the total
cycle time.

### **Pressure oversampling factor** — Oversampling factor for the measured pressure value `1` (default) | `2` | `4` | `8` | `16`

Specify the oversampling factor to reduce the noise for the pressure value read from
BME280 sensor. This value is a multiplication factor that affects measurement rate and
current consumption.

### **Humidity oversampling factor** — Oversampling factor for the measured humidity value `1` (default) | `2` | `4` | `8` | `16`

Specify the oversampling factor to reduce the noise for the humidity value read from
BME280 sensor. This value is a multiplication factor that affects measurement rate and
current consumption.

### **Temperature oversampling factor** — Oversampling factor for the measured humidity value `1` (default) | `2` | `4` | `8` | `16`

Specify the oversampling factor to reduce the noise for the temperature value read
from BME280 sensor. This value is a multiplication factor that affects measurement rate
and current consumption.

### **Data type** — Output data type for values from BME280 sensor `single` (default) | `double`

Specify the output data type for the values read from BME280 sensor. The default
data type for Raspberry Pi board is `single`. Use this parameter to change the
values to `double`, if required.

### **Sample time** — Time interval to read data `-1` (default) | positive integer

Specify how often this block reads the data from the BME280 sensor. When you set
this parameter to -1, Simulink determines the best sample time for the block based on
the block context within the model.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Sensors / Environmental Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022b**

## Description

Measure barometric air pressure, relative humidity, and temperature from BME280 sensor

The BME280 block outputs the values of barometric air pressure and relative
humidity as measured by the BME280 sensor connected to Raspberry Pi® board. The block also outputs the temperature as read by the BME280
sensor.
