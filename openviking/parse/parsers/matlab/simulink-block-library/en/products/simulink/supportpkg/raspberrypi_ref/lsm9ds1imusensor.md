---
type: simulink-block
title: 'LSM9DS1 IMU Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sense HAT'
documentation_page: 'lsm9ds1imusensor'
documentation_source_path: 'supportpkg/raspberrypi_ref/lsm9ds1imusensor.html'
language: en
---

# LSM9DS1 IMU Sensor

## Ports

### Output

### **AngVelocity** — Angular velocity along each axis as measured by the Gyroscope vector

The angular velocity as a `[1x3]` vector. Each
value represents the measurement of the angular velocity in degrees
per second (dps) along the X, Y, and Z axes.

**Data Types:** `double`

### **Accel** — Acceleration along each axis as measured by the Accelerometer vector

The block outputs the acceleration as a `[1x3]` vector.
Each value represents the measurement of the acceleration in `g
(9.8 m/s2)` along the X, Y, and
Z axes.

**Data Types:** `double`

### **MagField** — Strength of the magnetic field along each axis as measured by the Magnetometer vector

The block outputs the magnetic field as a `[1x3]` vector.
Each value represents the measurement of the magnetic field in micro
Tesla`(μT)` along the X, Y, and Z axes.

## Parameters

### **View Axis Information** — Button to view the axes information of the LSM9DS1 IMU Sensor button

Click this button to view the X, Y, and Z axis of the LSM9DS1 IMU Sensor
with respect to SenseHAT.

### **Board** — Model of the Raspberry Pi board to which the SenseHAT is connected `Pi 3 Model B+` (default) | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 2 Model B` | `Pi 3 Model B` | `Pi Zero W` | `Pi 4 Model B` | `Pi 5 Model`

Select the Raspberry Pi hardware to which the SenseHAT is
connected.

### **Active sensors** — Active sensors on Raspberry Pi SenseHAT `Accelerometer, Gyroscope and Magnetometer` (default) | `Accelerometer and Gyroscope` | `Accelerometer and Magnetometer` | `Gyroscope and Magnetometer` | `Accelerometer` | `Gyroscope` | `Magnetometer`

Select active sensors to measure angular velocity, acceleration,
magnetic field, or a combination of these measurements as per your
requirements.

Each active sensor is provided with a set of parameters under
the Advanced settings that you can configure to obtain the required
behavior.

### **Accelerometer – Output data rate** — Rate of measurement of acceleration 119 Hz (default) | 10 Hz | 50 Hz | 238 Hz | 476 Hz | 952 Hz

Select the rate at which you want the Accelerometer to measure
the acceleration.

### **Accelerometer – Full scale range** — Sensitivity of the Accelerometer +/- 2g (default) | +/- 4g | +/- 8g | +/- 16g

Select the required sensitivity for measurement of acceleration.
The upper and the lower limits of what the sensor can measure. In
general, for all the sensors, you get a more precise measurement out
of a sensor with a low full-scale range.

### **Accelerometer – Bandwidth** — Frequency range for sensor operation 50 Hz (default) | 105 Hz | 211 Hz | 408 Hz

Set the bandwidth for the low-pass filter associated with measurement of acceleration. Refer
to the LSM9DS1 data sheet for further information.

### **Gyroscope – Output data rate** — Rate of measurement of angular velocity 119 Hz (default) | 14.9 Hz | 59.5 Hz | 238 Hz | 476 Hz | 952 Hz

Select the rate at which you want the Gyroscope to measure the
angular velocity.

### **Gyroscope – Full scale range** — Sensitivity of the Gyroscope 245 dps (default) | 500 dps | 2000 dps

Select the required sensitivity for measurement of angular velocity.
The upper and the lower limits of what the sensor can measure. In
general, for all the sensors, you get a more precise measurement out
of a sensor with a low full-scale range.

### **Gyroscope – Bandwidth mode** — Frequency range for sensor operation 0 (default) | 1 | 2 | 3

Select the desired bandwidth mode to set the cut-off frequency
for the low-pass filter associated with the Gyroscope. Refer to the
table for the information about the cut-off frequencies.

Refer to the LSM9DS1 data sheet for further information.

### **Gyroscope - Enable high pass filter** — Option to enable high pass filter for Gyroscope operation off (default) | on

Select this check box to enable the high pass filter for Gyroscope
operation.

### **Gyroscope – High pass filter mode** — Mode of operation for Gyroscope High pass filter 0 (default) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

Select the High pass filter mode to set the desired cut-off
frequencies for the high pass filter. Refer the table given to select
the desired cut-off frequency.

Refer to the LSM9DS1 data sheet for further information.

### **Magnetometer – Output data rate** — Rate of measurement of magnetic field 40 Hz (default) | 0.625 Hz | 1.25 Hz | 2.5 Hz | 5 Hz | 10 Hz | 20 Hz | 80 Hz

Select the rate at which you want the Magnetometer to measure the magnetic
field.

### **Magnetometer – Full scale range** — Sensitivity of the Magnetometer +/- 4 gauss (default) | +/- 8 gauss | +/- 12 gauss | +/- 16 gauss

Select the required sensitivity for measurement of magnetic
field. The upper and the lower limits of what the sensor can measure.
In general, for all the sensors, you get a more precise measurement
out of a sensor with a low full-scale range.

### **Sample time** — Frequency at which data is read from the active sensors 0.1 (default) | scalar

Specify how often this block reads the data from the active
sensors.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Sense HAT

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017a**

## Description

Measure linear acceleration, angular rate and magnetic field along X, Y, and Z axes

Measure the linear acceleration, angular rate, and magnetic
field using the 9–DoF IMU (Inertial Measurement Unit) sensor
on board Raspberry Pi® SenseHAT.

The IMU sensor (LSM9DS1) comprises accelerometer, gyroscope,
and a magnetometer. Using this block, you can measure the inertial
motion of the Raspberry Pi on top of which the SenseHAT is connected.

Choose the desired active sensor(s) to measure angular velocity, acceleration, magnetic field,
or a combination of these measurements.

The block outputs acceleration as [1x3] vector values of double
data type in ‘g’ (9.8 m/s^2), angular rate as [1x3]
vector values of double data type in ‘degrees per second’
(dps), and magnetic field as [1x3] vector values of double data type
in micro Tesla (µT).

You can optionally apply specific advanced settings to customize
the sensor behavior according to your needs.

The axis information of the IMU sensor on SenseHAT is as shown.
