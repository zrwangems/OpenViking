---
type: simulink-block
title: 'Smart Motor Read'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Sensors'
documentation_page: 'smartmotorread'
documentation_source_path: 'vexv5/ref/smartmotorread.html'
language: en
---

# Smart Motor Read

## Ports

### Input

### **Reset** — Signal that resets the encoder reading integer (0 = no reset; integer ≥ 1 = reset)

Connect to a signal that resets the in-built encoder of V5 Smart Motor.

#### Dependencies

This input appears only when you set the **Reset mode**
parameter to `Reset by external signal`.

**Data Types:** `double`
### Output

### **Position** — Encoder value from V5 Smart Motor tick count | rotations | degrees

The value that is read from the in-built encoder of V5 Smart Motor, based on the
selected `Encoder unit`.

For example, if the motor has completed two rotations (assuming that the gear
ratio is 36:1):

- tick count = `3600`
- degrees = `720`
- rotations = `2`

#### Dependencies

This output depends on the value selected for the **Encoder
unit** parameter.

**Data Types:** `double`

### **Velocity** — Velocity of V5 Smart Motor RPM

The velocity of V5 Smart Motor as read from the in-built encoder. The sign
determines the direction of rotation of the motor, and the amplitude determines the
velocity in RPM. Positive value indicates that the motor is rotating in clockwise
direction and negative value indicates anticlockwise direction. An output value of
`0` indicates that the motor is stationary.

#### Dependencies

This output appears only when you select the **Output velocity and
fault** check box.

**Data Types:** `double`

### **Fault** — Fault indication from V5 Smart Motor `1` | l`2` | `3`

The fault indication that is decoded from the V5 Smart Motor. The output value
represents these type of faults:

- `1`: Over-current fault
- `2`: Over-temperature fault
- `3`: Both over-current and over-temperature faults

#### Dependencies

This output appears only when you select the **Output velocity and
fault** check box.

**Data Types:** `double`

## Parameters

### **Smart Port** — Select the Smart Port to which V5 Smart Motor is connected 1 (default) | `1` to `21`

Select the Smart Port on the VEX EDR V5 Robot Brain to which the V5 Smart Motor is connected. There are 21
Smart Ports on the VEX EDR V5 Robot Brain that you can connect to V5 Smart Motor.

Smart Port must be unique for each block in the model. If multiple Smart Motor Read
blocks with the same port are used, the last executed Smart Motor Read block may only be
active. For the Vex Robotics Competition, you can use the same Smart Motor Read block
with the same Smart Port in the driver mode or the autonomous mode.

### **Encoder unit** — Select the unit for reading the motor position from the encoder `Counts` (default) | `Rotations` | `Degrees`

Select the unit for reading the V5 Smart Motor's position from the in-built encoder.
The position can be read in terms of tick counts, number of rotations, or
degrees.

### **Reset mode** — Select the reset mode for reading values `Reset at each sample time` (default) | `No reset` | `Reset by external signal`

Select the reset mode for reading values from the in-built encoder of the V5 Smart
Motor.

When you select `Reset by external signal`, an additional
input – `Reset` – is added to the block, which can be connected to a
reset signal.

### **Sample time** — Interval at which the block reads values `0.2` (default) | positive scalar | -1

Enter the time interval at which the block reads values from the in-built encoder of
the V5 Smart Motor.

When you set this parameter to `-1`, Simulink® determines the best sample time for the block based on the block context
within the model.

## Libraries

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Represent connected V5 Smart Motor and read encoder values

The Smart Motor Read block represents a V5 Smart Motor connected to a
specified port on a VEX® EDR V5 Robot Brain, and read the values from the in-built encoder of the V5
Smart Motor.
