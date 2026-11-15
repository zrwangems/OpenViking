---
type: simulink-block
title: 'Distance Sensor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Sensors'
documentation_page: 'distancesensor'
documentation_source_path: 'vexv5/ref/distancesensor.html'
language: en
---

# Distance Sensor

## Ports

### Output

### **Distance** — Obstacle distance scalar

The **Distance** port outputs distance in meters.
Nominal range is around 2 meters.

**Data Types:** `double`

### **Velocity** — Approach velocity scalar

The **Velocity** port outputs relative velocity of
obstacle in meters per second.

#### Dependencies

To enable this port select **Velocity (m/s)**
parameter.

**Data Types:** `double`

### **Size** — Obstacle size scalar

The **Size** output indicates the obstacle size. It
ranges from 0 to 400, with larger values corresponding to larger
obstacle.

#### Dependencies

To enable this port select the **Size**
parameter.

**Data Types:** `double`

### **Confidence** — Confidence in distance measurement scalar

The **Confidence** indicates if an object is detected
within sensor's range and its value ranges from 0 to 63. Confidence
value drops to 0 when an object is beyond the sensor's range and the
value is 10 for distances below 0.2 meters.

#### Dependencies

To enable this port select the **Confidence**
parameter.

**Data Types:** `double`

## Parameters

### **Smart Port** — Smart Port to which VEX V5 Distance Sensor is connected 1 (default) | `1` to `21`

Select the smart port on the V5 robot to which the VEX V5 Distance sensor
is connected. There are 21 smart ports on the V5 robot.

### **Sample time** — Interval to read values from sensor `0.2` (default) | positive scalar | `-1`

Specify the sample time in seconds to determine how often the block reads
values from the sensor. When you specify this parameter as
`-1`, Simulink® determines the best sample time for the block based on the
block context within the model.

### Additional Outputs

### **Velocity (m/s)** — Approach velocity `off` (default) | `on`

Select this parameter to enable **Velocity** port.
For more information on the **Velocity** port, see
Velocity,

### **Size** — Obstacle size `off` (default) | `on`

Select this parameter to enable **Size** port. For
more information on the **Size** port, see Size,

### **Confidence** — Confidence in distance `on` (default) | `off`

Select this parameter to enable **Confidence** port.
For more information on the **Confidence** port, see
Confidence.

## Libraries

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

## Description

Read distance, velocity, and relative size of obstacle

The Distance Sensor block reads data from the Distance sensor that is
connected to the VEX® V5 Brain. You can use this block in your Simulink model to obtain
distance, velocity, relative size of obstacle, and confidence. Also, the sensor outputs
confidence in measuring distance.
