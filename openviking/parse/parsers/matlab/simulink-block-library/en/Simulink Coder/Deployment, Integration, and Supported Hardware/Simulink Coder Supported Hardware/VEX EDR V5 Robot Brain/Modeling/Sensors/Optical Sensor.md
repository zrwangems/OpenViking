---
type: simulink-block
title: 'Optical Sensor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Sensors'
documentation_page: 'opticalsensor'
documentation_source_path: 'vexv5/ref/opticalsensor.html'
language: en
---

# Optical Sensor

## Ports

### Output

### **Proximity** — Proximity of reflected infrared scalar

This port sensor measures the amount of reflected Infrared energy from
an obstacle. The value of Proximity ranges from 0-255 with higher values
indicating closeness to sensor. The nominal range of sensor is
10cm.

**Data Types:** `double`

### **HSB** — Hue, saturation, and brightness of object vector

This port represents the Hue, Saturation, Brightness/Value scale
(HSB/HSV). The value for Hue ranges from `0` to
`360` with `0` corresponding to
red color. The value `120` corresponds to green and
value `240` corresponds to blue. The Saturation and
Brightness value ranges from `0` to
`1`.

#### Dependencies

To enable this port select the **HSB (Hue, Saturation,
Brightness)** parameter.

**Data Types:** `double`

### **RGB** — Red, Green, Blue vector

This port represents the color of the object in Red,Blue,Blue (RGB)
scale.

#### Dependencies

To enable this port select the **RGB (Red, Green,
Blue)** parameter.

**Data Types:** `double`

## Parameters

### **Smart Port** — Smart Port to which VEX V5 Inertial Sensor is connected 1 (default) | `1` to `21`

Select the smart port on the V5 robot to which the VEX V5 inertial sensor
is connected. There are 21 smart ports on the V5 robot.

### **LED Power (%)** — Brightness of the LED light 1 (default) | `0` to `100`

The value ranges from 0 to 100 and the LED brightness increases with
increase in the value.

### **Sample time** — Interval to read values from sensor `0.2` (default) | `-1` | positive scalar

Specify the sample time in seconds to determine how often the block reads
values from the sensor. When you specify this parameter as
`-1`, Simulink® determines the best sample time for the block based on the
block context within the model.

### Additional Outputs

### **HSB (Hue, Saturation, Brightness)** — Hue, Saturation, and Brightness of object `on` (default) | `off`

Select this parameter to enable **HSB** port. For
more information, see HSB.

### **RBG (Red, Blue, Green)** — Color of object `off` (default) | `on`

Select this parameter to enable **RGB** port. For
more information on the **RGB** port, see RGB.

**Data Types:** `double`

## Libraries

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

## Description

Read proximity, color, and brightness

The Optical Sensor block reads data from the optical sensor that is
connected to the VEX® V5 Brain. You can use this block in your Simulink model to measure color,
brightness, and proximity to an object from optical sensor.
