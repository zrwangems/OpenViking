---
type: simulink-block
title: 'HTS221 Humidity Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sense HAT'
documentation_page: 'hts221humiditysensor'
documentation_source_path: 'supportpkg/raspberrypi_ref/hts221humiditysensor.html'
language: en
---

# HTS221 Humidity Sensor

## Ports

### Output

### **Humidity** — Relative humidity output port scalar

The relative humidity measured in percentage from the Humidity
sensor.

**Data Types:** `double`

### **Temperature** — Ambient temperature output port scalar

The ambient temperature measured in degree Celsius from the
Humidity sensor.

**Data Types:** `double`

## Parameters

### **Board** — Model of the Raspberry Pi board to which the SenseHAT is connected `Pi 2 Model B` (default) | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Pi 4 Model B` | `Pi Zero 2 W` | `Compute Module 4` | `Pi 5 Model`

Select the Raspberry Pi hardware to which the SenseHAT is
connected.

### **Sensor output data rate (ODR)** — Rate at which the sensor measures data 12.5 Hz (default) | 1 Hz | 7 Hz

The rate at which the Humidity sensor measures relative humidity
and ambient temperature.

### **Sample time** — Frequency at which data is measured data is read from Humidity sensor 0.1 (default) | scalar

Specify how often this block reads the measured data from the
Humidity sensor.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Sense HAT

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2007a**

## Description

Measure relative humidity and ambient temperature from Humidity sensor

Measure the relative humidity and the ambient temperature using the Humidity sensor (HTS221)
on board Raspberry Pi® SenseHAT.
