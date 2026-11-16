---
type: simulink-block
title: 'LPS22HB Pressure Sensor'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Sensors'
documentation_page: 'lps22hbpressuresensorblock'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/lps22hbpressuresensorblock.html'
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

Temperature (in ℃) measured by LPS22HB sensor connected to STM32
processor.

#### Dependencies

This output port appears only if you select the **Temperature
(℃)** parameter.

**Data Types:** `double`

### **Status** — Status of pressure and temperature measurements `0` | `1` | `-1`

Status of pressure and temperature measurements, specified as a 1-by-2
vector. `0` indicates that the data read is new,
`1` indicates that the data read is not new, and
`-1` indicates that the corresponding output is not
selected.

#### Dependencies

This output port appears only if you select the
**Status** parameter.

**Data Types:** `int8`

## Parameters

### **I2C module** — Specify I2C module `2` (default) | `positive integer`

Specify the I2C module on the board. The I2C bus frequency, serial clock (SCL)
pin and serial data (SDA) pin are taken according to the corresponding I2C module
entry in the configuration parameters.

### **I2C address** — Peripheral addresses to communicate with sensor peripherals `0x5C` (default) | `0x5D`

The peripheral addresses to communicate with the LPS22HB sensor are decided by
the state of the SA0 pin on the hardware board. This table provides the peripheral
addresses corresponding to the pin and their state.

| Pin Name | Pin State | Peripheral Address |
| --- | --- | --- |
| SA0 | 0 | 0x5C |
| 1 | 0x5D |

### **Pressure (Pa)** — Set output port for reading pressure `on` (default) | `off`

Select this parameter to set **Pressure** as one of the output
ports.

### **Temperature (℃)** — Set output port for reading temperature `on` (default) | `off`

Select this parameter to set **Temperature** as one of the
output ports.

### **Status** — Set output port for obtaining status `off` (default) | `on`

Select this parameter to set **Status** as one of the output
ports.

### **Output data rate (ODR)** — Rate at which pressure data is sampled `1 Hz` (default) | `10 Hz` | `25 Hz` | `50 Hz` | `75 Hz`

Select the output data rate at which pressure data is sampled, which also
determines the bandwidth.

### **Enable low pass filter** — Enable low pass filter for pressure data `off` (default) | `on` |

Enable the low pass filter for reading pressure values.

### **Select the bandwidth** — Bandwidth of low pass filter `ODR/9` (default) | `ODR/20`

Select the required bandwidth of the low pass filter.

#### Dependencies

This parameter appears only if you select the **Enable low pass
filter** parameter.

### **Sample time** — Time interval to read data `-1` (default) | positive integer

Specify how often this block reads the data from the LPS22HB sensor. When you
set this parameter to -1, Simulink determines the best sample time for the block
based on the block context within the model.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Embedded Coder Support Package for STMicroelectronics STM32 Processors / Sensors / Environmental Sensors Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Sensors Simulink Support Package for Arduino Hardware / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

Measure barometric air pressure and temperature from LPS22HB sensor

The LPS22HB Pressure Sensor block measures barometric air pressure using
the LPS22HB pressure sensor interfaced with the STM32 Processor. This sensor comprises of a
sensing element to measure the absolute pressure. The block also measures the temperature
from the embedded temperature sensor in LPS22HB Sensor.

You can also select an output data rate in the block, and use the low pass filter option
for filtering the measured pressure values.
