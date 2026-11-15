---
type: simulink-block
title: 'LPS25h Pressure Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sense HAT'
documentation_page: 'lps25hpressuresensor'
documentation_source_path: 'supportpkg/raspberrypi_ref/lps25hpressuresensor.html'
language: en
---

# LPS25h Pressure Sensor

## Ports

### Output

### **Pressure** — Barometric air pressure output port scalar

The barometric air pressure measured in hectoPascal (hPa) from
the Pressure sensor.

**Data Types:** `double`

### **Temp** — Ambient temperature output port scalar

The ambient temperature output measured in degree Celsius (C)
from the Pressure sensor.

**Data Types:** `double`

## Parameters

### **Board** — Raspberry Pi hardware board `Pi 2 Model B` (default) | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Pi 4 Model B` | `Pi Zero 2 W` | `Compute Module 4` | `Pi 5 Model`

Select your Raspberry Pi hardware board. You can find this information on the target
hardware, product packaging, or product documentation.

### **Sensor output data rate (ODR)** — Rate at which the sensor measures data 12.5 Hz (default) | 1 Hz | 7 Hz

The rate at which the Pressure sensor measures barometric air
pressure and the ambient temperature.

### **Sample time** — Frequency at which data is measured data is read from Pressure sensor 0.1 (default) | scalar

Specify how often this block reads the measured data from the
Pressure sensor.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Sense HAT

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017a**

## Description

Measure barometric air pressure and ambient temperature

Measure barometric air pressure and ambient temperature using
the Pressure sensor on board Raspberry Pi® SenseHAT.
