---
type: simulink-block
title: 'Barometer'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Sensors'
documentation_page: 'barometer'
documentation_source_path: 'beagleboneblue/ref/barometer.html'
language: en
---

# Barometer

## Ports

### Output

### **Pressure** — Air pressure around barometer vector

The **Pressure** port outputs the barometric air
pressure around the BMP280 barometer on the hardware. The air pressure
is output as a 1-by-1 array in pascal.

**Data Types:** `double`

## Parameters

### **Sample time** — Time interval to read values from barometer `0.1` (default) | `-1` | nonnegative real value

Specify how often the block reads values from the barometer, in seconds.
When you specify this parameter as `-1`, Simulink® determines the best sample time for the block based on the
block context within the model.

### Sensor Settings

### **Over sampling rate** — Rate at which values are sampled `8` (default) | `1` | `2` | `4` | `16`

Select a rate at which the barometer samples the air pressure values,
in Hertz.

### **IIR filter coefficient** — Coefficient of IIR filter `4` (default) | `Off` | `2` | `8` | `16`

Select a coefficient of the infinite impulse response (IIR) filter to
reduce the noise-related error in the sampled values.

## Libraries

Simulink Coder Support Package for BeagleBone Blue Hardware / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Measure barometric air pressure around the BMP280 sensor

The Barometer block measures the barometric air pressure around the
BMP280 barometer on the BeagleBone® Blue hardware, in pascal. The block outputs the pressure as a 1-by-1 array
of `double` data type.

If you simulate a model that contains the Barometer block without
connecting the hardware, the block outputs zeroes. For more information, see Block Produces Zeros or Does Nothing in Simulation.
