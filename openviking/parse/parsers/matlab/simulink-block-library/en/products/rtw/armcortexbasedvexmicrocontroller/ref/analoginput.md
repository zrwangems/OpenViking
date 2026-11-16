---
type: simulink-block
title: 'Analog Input'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Sensors'
documentation_page: 'analoginput'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/analoginput.html'
language: en
---

# Analog Input

## Ports

Not documented in R2025b.

## Parameters

**Analog Port**
:   Select an analog channel (or port), a value between 1 and 8.

    Do not assign the same channel number to multiple blocks within your model.

**Add input port for simulation**
:   Select this check box to simulate the analog input block.

**Sample time**
:   Specify how often this block should read the pin value, in seconds. This parameter
    value defaults to 1/5 second. If you select **Add input port for
    simulation** check box, the **Sample time** parameter is
    hidden and the value is inherited (Sample time = -1).

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017a**

## Description

Read the value of a sensor attached to an analog input pin

Read the voltage of the selected analog port (pin). Use the analog input pin to measure
the output of sensors (voltage), such as potentiometer. The 12-bit sensor value has a range
of 0 to 4095 reflecting an input voltage of 0V to 5V. You can use up to 8 analog IO pins on
the VEX® microcontroller. For information on the digital pin layout of the
microcontroller, see `VEX
Cortex Pin-out`.

During code generation, any simulation block that is connected to the input port of the
Analog Input block is ignored and has no effect on the generated code.

During simulations, without the hardware, this block emits zeros if there is no Source
block connected the simulation input port. See Block Produces Zeros or Does Nothing in Simulation. Connect a Source block from
the Utilities library in VEX Microcontroller library for achieving simulation
behavior.

For the code generated from this block to work properly on a VEX microcontroller that is tethered to the PC, make sure that you connect a VEX
7.2V Battery to the microcontroller and turn on the battery.
