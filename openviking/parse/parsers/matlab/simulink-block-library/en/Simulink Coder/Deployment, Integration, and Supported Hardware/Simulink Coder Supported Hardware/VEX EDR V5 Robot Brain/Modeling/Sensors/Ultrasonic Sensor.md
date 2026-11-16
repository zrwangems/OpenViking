---
type: simulink-block
title: 'Ultrasonic Sensor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Sensors'
documentation_page: 'ultrasonicsensor'
documentation_source_path: 'vexv5/ref/ultrasonicsensor.html'
language: en
---

# Ultrasonic Sensor

## Ports

### Output

### **Port\_1** — Distance read from the Echo port of the Ultrasonic sensor centimeters

The distance (in cm) as read from the Echo port of the Ultrasonic Sensor connected
to VEX V5 Robot Brain.

**Data Types:** `double`

## Parameters

### **3-Wire Expander (smart port)** — Select the smart port that is used by 3-Wire Expander `None` (default) | `1` to `21`

If you are using a 3-Wire Expander, specify the smart port on VEX® EDR V5 Robot Brain to which the expander is connected.

### **OUTPUT (Echo port)** — 3-wire port to which the Output port of Optical Shaft Encoder is connected A (default) | `C` | `E` | `G`

Select the 3-wire port of VEX V5 Robot Brain to which the Echo port (output) of
Ultrasonic sensor is connected. To know the output port, click the **What is
INPUT and OUTPUT?** button.

After you select the **OUTPUT (Echo port)** in the block, the
consecutive 3-wire port is assumed to be connected to the INPUT (Ping port) of the
ultrasonic sensor. For example, if you select `A` as the
**OUTPUT (Echo port)**, it is assumed that
`B` is connected to the INPUT (Ping) port of the ultrasonic
sensor.

### **Sample time** — Interval at which the block reads values `0.2` (default) | positive scalar | -1

Enter the time interval at which the block reads values from the ultrasonic
sensor.

When you set this parameter to `-1`, Simulink® determines the best sample time for the block based on the block context
within the model.

## Libraries

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Represent connected Ultrasonic sensor and measure distance to object

The Ultrasonic Sensor block represents an Ultrasonic Sensor that is
connected to the 3-wire ports of VEX EDR V5 Robot Brain, and measure the distance to the
object in the path of the robot. The block enables the object detection when the object is in
the range of 3 to 300 centimeters (cm) from the sensor. The block outputs a value 0 for an
object that is farther than 300 cm.
