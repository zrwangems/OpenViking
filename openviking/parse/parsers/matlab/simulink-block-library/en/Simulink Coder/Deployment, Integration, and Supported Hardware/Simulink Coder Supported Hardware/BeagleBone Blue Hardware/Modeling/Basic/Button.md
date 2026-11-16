---
type: simulink-block
title: 'Button'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Basic'
documentation_page: 'button'
documentation_source_path: 'beagleboneblue/ref/button.html'
language: en
---

# Button

## Ports

### Output

### **Port\_1** — Logical state of button scalar

When the button specified in the **Button** parameter
is pressed on the hardware, the block outputs `1`. When
the button specified in the **Button** parameter is
released on the hardware, the block outputs `0`. For
example, if the **Button** parameter on the Block
Parameters dialog box is set to `Mode`, and the
Mode button on the hardware is pressed, the block outputs
`1`. When the Mode button is released, the block
outputs `0`.

**Data Types:** `uint8`

## Parameters

### **Button** — Hardware button `Mode` (default) | `Pause`

Select the button of which the logical state (pressed or released) is to
be read.

### **Sample time** — Interval at which block reads button state `0.1` (default)

Specify how often the block reads the state of the button specified in the
**Button** parameter.

## Libraries

Simulink Coder Support Package for BeagleBone Blue Hardware / Basic

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017b**

## Description

Read logical state of button

The Button block reads the logical state of a user-configurable button
on the hardware. The hardware has two user-configurable buttons, Mode and Pause, with
two logical states, pressed and released.

During simulations without hardware, this block outputs zeros. See Block Produces Zeros or Does Nothing in Simulation.
