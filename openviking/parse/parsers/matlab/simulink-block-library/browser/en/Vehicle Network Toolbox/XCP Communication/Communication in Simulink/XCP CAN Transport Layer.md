---
type: simulink-block
title: 'XCP CAN Transport Layer'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'XCP Communication / Communication in Simulink'
documentation_page: 'xcpcantransportlayer'
documentation_source_path: 'ug/xcpcantransportlayer.html'
language: en
---

# XCP CAN Transport Layer

## Ports

Not documented in R2025b.

## Parameters

### **Device** — CAN device device list option

The CAN device, chosen from all connected CAN devices.

### **Bus speed** — Speed of CAN bus numeric

Speed of the CAN bus in bits per second. The default bus speed is the default
assigned by the selected device.

### **Sample time** — Simulation refresh rate `0.01` (default) | numeric

Simulation refresh rate, specified as the sampling time of the block during
simulation. This value defines the frequency at which the XCP CAN Transport Layer
subsystem and the underlying blocks run during simulation. For information about
simulation sample timing, see Timing in Hardware Interface Models. If the block is inside
a triggered subsystem or inherits a sample time, specify a value of
`-1`. You can also specify a MATLAB® variable for sample time. The default value is `0.01`
simulation seconds.

## Libraries

Vehicle Network Toolbox / XCP Communication / CAN Simulink Real-Time / XCP / CAN

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

The XCP communication blocks support code generation
with limited deployment portability that runs only on the host computer or Simulink
Real-Time™ targets.

Code generation requires a C++ compiler that is
compatible with the code generation target. For more information, see Supported and Compatible Compilers.

## Version History

**Introduced in R2013a**

## Description

Transport XCP messages via CAN

The XCP CAN Transport Layer subsystem uses the specified device to transport and receive
XCP messages.

Use this block with an XCP CAN Data Acquisition block to acquire and
analyze specific XCP messages. Use this block with an XCP CAN Data Stimulation
block to send specific information to modules.

### Other Supported Features

The XCP communication blocks support the use of Simulink® accelerator and rapid accelerator modes. Using this feature, you can speed up
the execution of Simulink models. For more information on this feature, see Acceleration (Simulink).
