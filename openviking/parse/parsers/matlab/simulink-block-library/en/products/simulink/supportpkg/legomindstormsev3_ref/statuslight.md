---
type: simulink-block
title: 'Status Light'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Control Blocks'
documentation_page: 'statuslight'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/statuslight.html'
language: en
---

# Status Light

## Ports

### Input

### **Status light** — Set status light of EV3 brick buttons integer

The block inputs these values to set the status light of the EV3 brick buttons.

- `0` — Off
- `1` — Set the status light color of the EV3 brick to solid
  green.
- `2` — Set the status light color of the EV3 brick to solid
  red.
- `3` — Set the status light color of the EV3 brick to solid
  orange.
- `4` — Set the status light color of the EV3 brick to
  pulsing green.
- `5` — Set the status light color of the EV3 brick to
  pulsing red.
- `6` — Set the status light color of the EV3 brick to
  pulsing orange.
- Other values — Off

This block converts the data type of the values it receives. You do not need to
convert the data type of the input signal.

**Data Types:** `int8`

## Parameters

Not documented in R2025b.

## Libraries

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Control status light on EV3 brick

Use the Status Light block to control the color and effect of the status
light behind the buttons on the EV3 brick.

During simulations without hardware, this block emits zeros. See Block Produces Zeros or Does Nothing in Simulation.
