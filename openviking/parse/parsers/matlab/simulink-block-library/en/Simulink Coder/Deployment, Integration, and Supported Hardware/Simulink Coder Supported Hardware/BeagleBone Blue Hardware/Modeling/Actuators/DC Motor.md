---
type: simulink-block
title: 'DC Motor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Actuators'
documentation_page: 'dcmotor'
documentation_source_path: 'beagleboneblue/ref/dcmotor.html'
language: en
---

# DC Motor

## Ports

### Input

### **Port\_1** — Input signal scalar

The block accepts normalized values ranging from –100 to 100.

The sign determines the direction of rotation, and the amplitude
determines the power supplied to the motor.

- `1` to `100`: Forward
  rotation, minimum to maximum power.
- `–1` to `–100`: Reverse
  rotation, minimum to maximum power.
- `0`: No power is supplied

For input value beyond the range of –100 to 100, the block has the
same effect as sending the maximum or minimum input values.

**Data Types:** `uint8` | `int8`

## Parameters

### **Motor Index** — Port index on the hardware `1` (default) | `2` | `3` | `4`

Select the DC motor port index on the hardware to which the DC motor is
connected.

### **Stop Action** — Stopping behavior of the motor `Brake` (default) | `Free Spin`

Using this parameter, configure the motor to brake or spin freely when
the block receives an input of `0` (stop).

- `Brake`: When you select this option,
  a back electromotive force is applied on the motor causing the
  motor to stop immediately.
- `Free Spin`: When you select this
  option, the motor spins freely as if it is disconnected from the
  wheel(s).

## Libraries

Simulink Coder Support Package for BeagleBone Blue Hardware / Actuators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017b**

## Description

Set power, direction, and stopping action of a DC motor

The DC Motor block controls the power, direction, and stopping action
of rotation of a DC motor connected to BeagleBone® Blue. Use this block with the Encoder block to measure the incremental position of the motor.

The input signal determines the power supplied to the motor and the direction of
rotation of the motor. The stopping action specified in the **Stop
action** parameter of the Block Parameters dialog box determines the
stopping behavior of the motor.

During simulations without hardware, this block does nothing. See Block Produces Zeros or Does Nothing in Simulation.
