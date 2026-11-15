---
type: simulink-block
title: 'Ultrasonic Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sensors / IMU Sensors'
documentation_page: 'ultrasonicsensor'
documentation_source_path: 'supportpkg/raspberrypi_ref/ultrasonicsensor.html'
language: en
---

# Ultrasonic Sensor

## Ports

### Output

### **Distance** — Distance between ultrasonic sensor and nearest object in front of sensor scalar

The port outputs the distance between the ultrasonic sensor connected
to the hardware and the nearest object in front of the sensor. The block
outputs the distance in meters. If the object is placed beyond the range
of sensor detection, the port outputs `0`.

**Data Types:** `double`

## Parameters

### **Board** — Board to connect the ultrasonic sensor `Pi 4 Model B` (default) | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 2 Model B` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Compute Module 4` | `Pi Zero 2 W` | `Pi 5 Model`

Select the Raspberry Pi® hardware board to which the ultrasonic sensor is connected.
For information about the digital pin numbers on the hardware, click
**View pin map**.

### **Number of signal pins** — Number of signal pins on ultrasonic sensor `2` (default) | `1`

Select the number of signal pins on the ultrasonic sensor to send and
receive sound waves.

- `1` — If the ultrasonic sensor has
  only one signal pin, SIG, select `1`.
- `2` — If the ultrasonic sensor has
  two separate signal pins, Trig and Echo, select
  `2`.

### **Trigger pin** — Digital pin connected to Trig pin `GPIO 23` (default) | `GPIO 4` | `GPIO 17` | `GPIO 27` | `GPIO 22` | `GPIO 10` | `GPIO 9` | `GPIO 11` | `GPIO 14` | `GPIO 15` | `GPIO 18` | `GPIO 24` | `GPIO 25` | `GPIO 8` | `GPIO 7`

Select the digital pin on the hardware to which the Trig pin of the
ultrasonic sensor is connected. For information about the digital pin
numbers on the hardware, click **View pin map**.

#### Dependencies

The **Trigger pin** parameter appears only when you
set the **Number of signal pins** parameter to
`2`.

### **Echo pin** — Digital pin connected to Echo pin `GPIO 24` (default) | `GPIO 4` | `GPIO 17` | `GPIO 27` | `GPIO 22` | `GPIO 10` | `GPIO 9` | `GPIO 11` | `GPIO 14` | `GPIO 15` | `GPIO 18` | `GPIO 23` | `GPIO 25` | `GPIO 8` | `GPIO 7`

Select the digital pin on the hardware to which the Echo pin of the
ultrasonic sensor is connected. For information about the digital pin
numbers on the hardware, click **View pin map**.

#### Dependencies

The **Echo pin** parameter appears only when you set
the **Number of signal pins** parameter to
`2`.

### **Signal pin** — Digital pin connected to SIG pin `GPIO 23` (default) | `GPIO 4` | `GPIO 17` | `GPIO 27` | `GPIO 22` | `GPIO 10` | `GPIO 9` | `GPIO 11` | `GPIO 14` | `GPIO 15` | `GPIO 18` | `GPIO 24` | `GPIO 25` | `GPIO 8` | `GPIO 7`

Select the digital pin on the hardware to which the SIG pin of the
ultrasonic sensor is connected. For information about the digital pin
numbers on the hardware, click **View pin map**.

#### Dependencies

The **Signal pin** parameter appears only when you
set the **Number of signal pins** parameter to
`1`.

### **Sample time** — Interval to read distance using ultrasonic sensor `0.1` (default) | `-1` | any nonnegative value

Specify how often the block reads distance using the ultrasonic sensor,
measured in seconds.

When specifying **Sample time**, verify these settings to
avoid task overrun:

1. The **Sample time** parameter must be equal to
   the model base rate. To view the model base rate, select **Display** > **Sample Time**  > **All** on the model toolbar. In the Sample Time Legend dialog
   box, the value corresponding to the red box is the base rate of the model.
2. The **Sample time** parameter and the model base
   rate must be greater than the total time required by the sensor to
   transmit and receive the sound wave. For example, if the object is
   placed 0.1 meters away from the sensor, the **Sample
   time** parameter specified must be greater than
   `0.000301` seconds.

   For information on how to calculate the travel time of the sound
   wave, see Calculate Travel Time of Sound Wave.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022b**

## Description

Measure distance between ultrasonic sensor and object

The Ultrasonic Sensor block outputs the distance between the ultrasonic
sensor connected to the hardware and the nearest object in front of the sensor. The
block outputs the distance as a double-precision value, in meters. If the object is
placed beyond the range of sensor detection, the block outputs `0`.

If you simulate a model that contains the Ultrasonic Sensor block
without connecting the hardware, the block outputs zeros. For more information, see
Block Produces Zeros or Does Nothing in Simulation.
