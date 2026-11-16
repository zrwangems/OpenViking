---
type: simulink-block
title: 'Encoder'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC4x / Peripheral Management / AURIX TC4x'
documentation_page: 'encoder'
documentation_source_path: 'infineonaurix/ref/encoder.html'
language: en
---

# Encoder

## Ports

### Input

### **msg** — SoC Blockset simulation message `scalar`

The block converts this input SoC Blockset™ message into encoder position and outputs it in
**ticks** port during simulation.

#### Dependencies

To view this port, select the **Enable simulation
port** parameter and set the port type as **SoC
Data (Message based)**.

### **sig** — Simulink based simulation signal `scalar` | `vector`

The simulation-only Simulink® signal input acts as pass-through with the output of the
Encoder block during simulation.

#### Dependencies

To enable this port, select the **Enable simulation
port** parameter and set the port type as
**Signal**.

### **offset\_in** — Enable to add motor offset `scalar`

The offset\_in port enables you to dynamically add the offset in raw
position with respective to the motor if required.

#### Dependencies

To enable this port, select the **Enable offset
inport** parameter.

**Data Types:** `int32`

### **rate\_in** — Enable to change data rate `scalar`

The rate\_in ports enables you to change the rate at which the data is
sampled at run time in seconds.

#### Dependencies

To enable this port, select the **Enable refresh rate
inport** parameter.

**Data Types:** `Float32`
### Output

### **ticks** — Encoder position in count `scalar`

The ticks port outputs the encoder position in count as an
`int32` value.

**Data Types:** `int32`

### **dir** — Current motor direction `scalar`

The dir port outputs the current direction of the motor as one of the following:

- `0` - Clockwise direction
- `1` - Counter clockwise direction

#### Dependencies

To enable this port, select the **Enable direction
port** parameter.

**Data Types:** `Boolean`

### **speed** — Mechanical speed of motor `scalar`

The speed port outputs the mechanical speed (in rad/s) of the motor as
an `float32` value.

#### Dependencies

To enable this port, select the **Enable speed
port** parameter.

**Data Types:** `float32`

### **offset\_out** — Motor position offset `scalar`

The offset\_out port outputs the offset in raw position with respective
to the motor as an **int32** value.

#### Dependencies

To enable this port, select the **Enable offset
outport** parameter.

**Data Types:** `int32`

### **rate** — Encoder update period `scalar`

The rate port outputs the rate at which the data is sampled (in
seconds) as an `float32` value.

#### Dependencies

To enable this port, select the **Enable rate
outport** parameter.

**Data Types:** `float32`

## Parameters

### Inputs

### **Enable offset inport** — Select to enable offset input port `off` (default) | `on`

Enable this parameter to dynamically add the offset in raw position
with respective to the motor.

### **Enable refresh rate inport** — Select to enable refresh rate inport `off` (default) | `on`

Enable this parameter to refresh the rate at which the data is
sampled.

### **Enable simulation port** — Enable peripheral simulation ports in the block `off` (default) | `on`

Select this parameter to enable peripheral simulation
capability.

### **Port Type** — Specify the type of peripheral simulation port `SoC Data (Message based)` (default) | `Signal`

Select this parameter to configure either the SoC compatible or the
simulink signal based simulation ports to enable peripheral simulation
capability.

#### Dependencies

To view this parameter, select the **Enable simulation
port** parameter.

### Outputs

### **Enable direction port** — Select to enable direction output port `off` (default) | `on`

Enable this parameter to output the current direction of the
motor.

### **Enable speed port** — Select to enable speed output port `off` (default) | `on`

Enable this parameter to output the mechanical speed (in rad/s) of the
motor.

### **Enable offset outport** — Select to enable offset output port `off` (default) | `on`

Enable this parameter to output the offset in raw position with
respective to the motor.

### **Enable refresh rate outport** — Select to enable rate output port `off` (default) | `on`

Enable this parameter to output the rate at which the data is sampled
in seconds.

### **Sample time** — Frequency at which block samples the input pin `0.0001` (default) | `scalar` | `vector`

Specify in seconds how often the block should read the pin
value.

When you specify this parameter as `-1`, Simulink determines the best sample time for the block based on the
block context within the model.

## Libraries

Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / AURIX TC4x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022b**

## Description

Measures rotation of motor in ticks

Measures the rotation of the motor in ticks.

The ticks port outputs the encoder ticks count as an `int32`
value.

The **dir** port, when enabled, outputs the direction of the encoder.

- `0` - clockwise direction.
- `1` - counter-clockwise direction.

The Encoder block is developed based on GPT12 (general purpose timer) module available
in the AURIX TC4x devices, where timer T3 & T5(slow speed calculation) is
used.
