---
type: simulink-block
title: 'DC Motor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Actuators'
documentation_page: 'dcmotor'
documentation_source_path: 'vexv5/ref/dcmotor.html'
language: en
---

# DC Motor

## Ports

### Input

### **Port\_1** — Input analog signal that sets motor speed integer in [ –128 127]

The block input value can range from –128 to 127. The sign determines the
direction of rotation of the motor, and the amplitude determines the speed. A block
input value of `0` stops the motor.

**Data Types:** `double`

## Parameters

### **3-Wire Expander (smart port)** — Select the smart port that is used by 3-Wire Expander `None` (default) | `1` to `21`

If you are using a 3-Wire Expander, specify the smart port on VEX EDR V5 Robot Brain to which the expander is connected.

### **Port** — Select the 3-wire port connected to the DC motor A (default) | `A` to `H`

Select the 3-wire port on the VEX EDR V5 Robot Brain that is connected to the DC motor.

Do not assign the same port number to more than one DC Motor block
within the same model.

## Libraries

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Actuators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Represent connected DC motor and set motor speed

The DC Motor block represents a DC motor connected to a specified 3-wire
port on an VEX® EDR V5 Robot Brain. The input signal sets the speed of the motor. There are
eight 3-wire ports on the VEX EDR V5 Robot Brain that you can connect to DC motors.
