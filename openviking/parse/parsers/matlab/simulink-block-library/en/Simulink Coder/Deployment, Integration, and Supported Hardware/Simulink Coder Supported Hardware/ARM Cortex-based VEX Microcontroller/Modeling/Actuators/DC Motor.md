---
type: simulink-block
title: 'DC Motor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Actuators'
documentation_page: 'dcmotor'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/dcmotor.html'
language: en
---

# DC Motor

## Ports

### Input

### **Port\_1** — Input analog signal that sets motor speed integer in [ –128 127]

The block input value can range from –128 to 127. The sign determines the
direction of rotation of the motor, and the amplitude determines the speed. A block
input value of `0` stops the motor.

The input analog signal for the DC Motor block can be derived from
the output of other blocks in the model (for example, from a Gamepad Joystick block).

During simulations without the hardware, the DC Motor block emits
zeros if there is no block connected to the input port (see Block Produces Zeros or Does Nothing in Simulation). If the input value to
DC Motor is beyond the range of –128 to 127, you receive an error message during
simulation.

**Data Types:** `double`
### Output

### **Port\_1** — Motor speed during simulation scalar

The output is the speed of the motor, calculated by multiplying the value from the
input port by the value of the **Gearing Ratio** parameter and
rounding the product to the nearest integer. Connect a Sink block, such as a Display
block or Scope block, to the output port to view the simulation output. The Sink
blocks are available in the Utilities library in Simulink® Support Package for ARM
Cortex-based VEX Microcontroller.

#### Dependencies

This port appears only when you select the **Add output port to measure
speed during simulation** parameter.

**Data Types:** `double`

## Parameters

### **Motor Channel** — Motor channel for DC motor `1` (default) | 1 to 10

Select the motor channel or pin on the ARM
Cortex-based VEX Microcontroller that is connected to the DC motor.

Do not assign the same channel number to more than one DC Motor block
within the same model.

### **Gearing Ratio** — Gear ratio of motor during simulation `1/13.5` (default) | (`driving gear`) / (`driven gear`)

This parameter is applicable for simulation behavior only. The gear ratio value is a
scaling factor that scales the input value of the block (–128 to 127) to an approximate
motor RPM. Adjust it accordingly to match the simulated motor speed with the motor speed
in the actual installation.

### **Add output port to measure speed during simulation** — Add output port for simulation `off` (default) | `on`

Select this check box to add the output port to emit the speed of the DC motor
during simulation.

## Libraries

Simulink Coder Support Package for ARM Cortex-based Microcontroller / Actuators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

During code generation, simulation block that is connected to the output port of a
DC Motor block is ignored and has no effect on the generated code.

## Version History

**Introduced in R2016a**

## Description

Represent connected DC motor and set motor speed

The DC Motor block represents a DC motor connected to a specified motor
channel on an ARM®
Cortex®-based VEX® Microcontroller. The input signal sets the speed of the motor. There are 10
motor channels, or pins, on the VEX microcontroller that you can connect to DC motors. For information on the pin
layout of the microcontroller, see the VEX Cortex
Pin-Out diagram for VEX Robotics.
