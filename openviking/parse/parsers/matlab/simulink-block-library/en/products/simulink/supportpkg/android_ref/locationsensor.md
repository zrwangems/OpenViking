---
type: simulink-block
title: 'Location Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Sensors'
documentation_page: 'locationsensor'
documentation_source_path: 'supportpkg/android_ref/locationsensor.html'
language: en
---

# Location Sensor

## Ports

### Output

### **Lat** — Latitude data of device scalar

The block outputs the latitudinal data of the device.

**Data Types:** `double`

### **Lon** — Longitude data of device scalar

The block outputs the longitudinal data of the device.

**Data Types:** `double`

### **Alt** — Altitude data of device scalar

The block outputs the altitude data of the device.

**Data Types:** `double`

## Parameters

### **Sample time** — Time interval of sampling `0.1` (default) | nonnegative scalar

Specify a discrete time interval, in seconds, at which the block reads the GPS
sensor of the device and outputs the data.

**Note**

Smaller values for **Sample time** require the processor to
complete the same number of instructions in less time, which can cause task
overruns.

## Libraries

Simulink Support Package for Android Devices / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014a**

## Description

Measure global positioning system data

Use the Location Sensor block to read GPS data of the device and output its
latitude, longitude, and altitude.

The GPS measurements are referenced to the most recent revision of the World Geodetic
System (WGS84). GPS sensor accuracy is typically measured in meters. When converting latitude
and longitude from decimal degrees to meters, the decimal degree values are considered to
within 6 decimal places only. For example, at the equator, 0.000001 degrees is approximately
11.1 centimeters.

**Note**

GPS must be enabled on the device. If any of these conditions occur, this block outputs
zeros.

- GPS is disabled on the device.
- The device does not contain a GPS sensor.
- Simulating without a device

For more information, see Block Produces Zeros or Does Nothing in Simulation.
