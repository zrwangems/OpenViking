---
type: simulink-block
title: 'Ultrasonic Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Sensor Blocks'
documentation_page: 'ultrasonicsensor'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/ultrasonicsensor.html'
language: en
---

# Ultrasonic Sensor

## Ports

### Output

### **Distance** — Distance between ultrasonic sensor and nearest object in front of sensor scalar

The block outputs the distance between the ultrasonic sensor connected to the EV3
brick and the nearest object in front of the sensor. The block outputs the distance in
centimeters.

When the nearest object is beyond the maximum range of the ultrasonic sensor, the
block outputs the maximum value, 255. When the object is placed beyond the range of
sensor detection, the port outputs 0.

**Data Types:** `uint8`

## Parameters

### **EV3 brick input port** — Input port number of EV3 brick `1` (default) | `2` | `3` | `4`

Select the EV3 brick input port to which the ultrasonic sensor is connected. Avoid
assigning multiple devices to the same input port.

### **Sample time** — Time interval at which block reads sensor values `0.1` (default) | positive integer

Specify the frequency of how often the block reads sensor values connected to the
EV3 brick. Shorter sample times, such as `0.01`, may produce unreliable
measurements.

Smaller sample times require the processor to complete the same number of
instructions in less time, which can cause task overruns.

## Libraries

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2012a**

## Description

Measure distance between ultrasonic sensor connected to EV3 brick and nearest object

Use the Ultrasonic Sensor block to measure the distance between the
ultrasonic sensor connected to the EV3 brick and the nearest object in front of the sensor.
The sensor can detect objects from approximately 5 to 255 centimeters away. The block measures
approximate distances from the object. For greater precision, calibrate the sensor output
values against physical measurements.

The distance from which the sensor first detects an approaching object depends on these factors.

- The ultrasonic reflectance of the object, which is a function of the object’s size
  and composition. The sensor detects large hard objects from a greater distance than
  small soft ones. For example, the sensor might detect a pane of glass at 255 cm and a
  hand puppet at 150 cm.
- The angle of incidence of the object relative to the sensor. The sensor detects
  objects directly in front of it at greater distances than objects off to the
  sides.

During simulations without hardware, this block emits zeros. See Block Produces Zeros or Does Nothing in Simulation.
