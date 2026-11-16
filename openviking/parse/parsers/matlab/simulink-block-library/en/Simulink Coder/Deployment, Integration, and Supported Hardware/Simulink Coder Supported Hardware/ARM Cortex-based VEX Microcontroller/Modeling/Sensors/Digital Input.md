---
type: simulink-block
title: 'Digital Input'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Sensors'
documentation_page: 'digitalinput'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/digitalinput.html'
language: en
---

# Digital Input

## Ports

Not documented in R2025b.

## Parameters

**Digital Port**
:   Select a digital pin (or port), a value between 1 and 12.

    Do not assign the same pin number to multiple blocks within your model.

**Add input port for simulation**
:   Select this check box to simulate the digital input block.

**Sample time**
:   Specify how often this block should read the digital pin value, in seconds. This
    parameter value defaults to 1/5 second. If you select **Add input port for
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

Read the digital value of an input pin

Read the digital or logical value (1 or 0) of the selected digital port (pin). You can
use up to 12 digital IO pins on the VEX® microcontroller. For information on the digital pin layout of the
microcontroller, see `VEX
Cortex Pin-out`.

During simulations, without the hardware, this block emits zeros if no Source block is
connected to the simulation input port. See Block Produces Zeros or Does Nothing in Simulation. To achieve simulation
behavior, connect a Source block from the Utilities library in VEX Microcontroller
library.

During code generation, any simulation block that is connected to the input port of the
Digital Input block is ignored and has no effect on the generated code.

It is possible that the code generated from this block does not work properly. If the
VEX microcontroller is connected to a PC using the orange USB A to A cable and has
no active VEX 7.2V battery connected, the VEX battery provides power to sensors.
