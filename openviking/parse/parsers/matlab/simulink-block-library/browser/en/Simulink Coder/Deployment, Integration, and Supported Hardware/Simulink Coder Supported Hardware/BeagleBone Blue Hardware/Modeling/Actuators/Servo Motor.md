---
type: simulink-block
title: 'Servo Motor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Actuators'
documentation_page: 'servomotor'
documentation_source_path: 'beagleboneblue/ref/servomotor.html'
language: en
---

# Servo Motor

## Ports

### Input

### **Port\_1** — Input signal that sets shaft position of servo motor scalar

The input range is between `0` and `180`. For
`0` input, the shaft is at 0 degrees, while for the input of
`180` the shaft is at 180 degrees. Out of range values, such as
`-5` or `200`, to the block input has the same
effect as sending the minimum or maximum input values.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## Parameters

### **Motor Channel** — Select motor channel for servo motor 1 (default) | `1` to `10`

Select the motor channel or pin on the BeagleBone Blue hardware that is connected to the servo motor.

To open the pin map, click **View pin map** button.

Assign a unique channel number for more than one Servo Motor block within a model.

## Libraries

Simulink Coder Support Package for BeagleBone Blue Hardware / Actuators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Set shaft position of servo motor

The Servo Motor block represents a servo motor connected to a specified motor channel on
BeagleBone® Blue hardware. Set the shaft position of the servo motor from
`0` to `180` degrees.
