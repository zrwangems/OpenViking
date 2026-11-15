---
type: simulink-block
title: 'Button'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Sensor Blocks'
documentation_page: 'button'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/button.html'
language: en
---

# Button

## Ports

### Output

### **Status** — Status of EV3 brick button `0` | `1`

The block outputs the status of the LEGO
MINDSTORMS EV3 brick button.

- `0` — Indicates that the EV3 brick button is not
  pressed.
- `1` — Indicates that the EV3 brick button is
  pressed.

**Data Types:** `uint8`

## Parameters

### **Button** — EV3 brick button `Up` (default) | `Center` | `Down` | `Right` | `Left`

Select the LEGO
MINDSTORMS EV3 brick button of whose status is to be determined.

### **Sample time** — Time interval at which block reads EV3 brick button status `0.1` (default) | positive integer

Specify the frequency of how often the block reads the EV3 brick button status.
Shorter sample times, such as `0.01`, may produce unreliable
measurements.

Smaller sample times require the processor to complete the same number of
instructions in less time, which can cause task overruns.

## Libraries

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2012a**

## Description

Detect status of EV3 brick button

Use the Button block to detect whether the LEGO®
MINDSTORMS® EV3 brick button is pressed or not. You can configure the block to detect the
status of center, left, right, up, and down buttons. However, you cannot configure the block
to detect the status of the back button as the EV3 brick reserves it to stop and shut down
programs.

During simulations without hardware, this block emits zeros. See Block Produces Zeros or Does Nothing in Simulation.
