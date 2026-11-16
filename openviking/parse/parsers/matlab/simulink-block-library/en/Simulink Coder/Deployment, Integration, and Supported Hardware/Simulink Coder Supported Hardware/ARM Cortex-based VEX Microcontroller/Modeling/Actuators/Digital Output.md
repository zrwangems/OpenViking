---
type: simulink-block
title: 'Digital Output'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Actuators'
documentation_page: 'digitaloutput'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/digitaloutput.html'
language: en
---

# Digital Output

## Ports

### Input

### **Port\_1** — Sets logical value (1 or 0) of pin `1` | `0`

Connect the input port to a block that generates a logical value
(`1` or `0`).

**Data Types:** `Boolean`
### Output

### **Port\_1** — Signal used during simulation `1` | `0`

Connect an appropriate sink block from the Utilities library in Simulink® Support Package for ARM
Cortex-based VEX Microcontroller to the output port to view the simulation output.

During simulations, this block emits zeros if no block is connected the input port
(see Block Produces Zeros or Does Nothing in Simulation).

#### Dependencies

This port appears only when you select the **Add output port for
simulation** parameter.

**Data Types:** `Boolean`

## Parameters

### **Digital Port (1 to 12)** — Select digital pin (or port) on VEX Microcontroller `1` (default) | integer in the range [1 12]

You can select one of the 12 digital IO pins on the VEX Microcontroller to act as digital output.

Do not assign the same pin number to multiple blocks in your model.

### **Add output port for simulation** — Add output port to simulate logical output `off` (default) | `on`

Select this check box to add an output port that simulates the logical output of the
block.

## Libraries

Simulink Coder Support Package for ARM Cortex-based VEX Microcontroller / Actuators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016a**

## Description

Represent one pin as digital output and set logical value

The Digital Output block is used to represent one of the 12 digital IO pins
on an ARM®
Cortex®-based VEX® Microcontroller as a digital output. The block sets the digital/logical value (1
or 0) of the pin. For information on the pin layout of the microcontroller, see the VEX Cortex
Pin-Out diagram from VEX Robotics.
