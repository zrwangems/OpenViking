---
type: simulink-block
title: 'FCC'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC4x / Peripheral Management / AURIX TC4x'
documentation_page: 'fcc'
documentation_source_path: 'infineonaurix/ref/fcc.html'
language: en
---

# FCC

## Ports

### Input

### **threshold** — Threshold value for comparison scalar

Specify the reference threshold value for comparison at this port.

#### Dependencies

To enable this port, set the **Mode** parameter to
`Normal` or
`Hysteresis` and select the **Enable
threshold input** parameter.

**Data Types:** `single`

### **stepWidth** — Step width of ramp scalar

Specify the step width of the ramp at this port.

#### Dependencies

To enable this parameter, set the **Mode** parameter to
`Ramp` and select the **Enable ramp
configuration inputs** parameter.

**Data Types:** `single`

### **stepSize** — Step size of ramp scalar

Specify the step size of the ramp at this port.

#### Dependencies

To enable this parameter, set the **Mode** parameter to
`Ramp` and select the **Enable ramp
configuration inputs** parameter.

**Data Types:** `single`

### **rampStart** — Start value of ramp scalar

Specify the start value of the ramp at this port.

#### Dependencies

To enable this parameter, set the **Mode** parameter to
`Ramp` and select the **Enable ramp
configuration inputs** parameter.

**Data Types:** `single`

### **rampEnd** — End value of ramp scalar

Specify the end value of the ramp at this port.

#### Dependencies

To view this parameter, select the **Mode** parameter as
`Ramp` and ensure the **Enable ramp
configuration inputs** parameter is enabled.

**Data Types:** `single`
### Output

### **status** — Status of boundary flag `0` | `1`

The block outputs the status of the boundary flag during a threshold update
as one of these values:

- `0 —` Boundary flag is inactive
- `1 —` Boundary flag is active

**Data Types:** `Boolean`

### **threshold** — Final threshold value in ramp mode scalar

This port returns the threshold value that the FCC reaches at the end of the
ramp mode.

#### Dependencies

To enable this port, set the **Mode** parameter to
`Ramp` and select the **Enable threshold
output** parameter.

**Data Types:** `single`

## Parameters

### **Mode** — Operation mode for threshold update `Normal` (default) | `Hysteresis` | `Ramp`

Select one of these operation modes:

- `Normal—` Compare the threshold reference value
  against the analogue input signal. If you enable the **Enable
  threshold input** parameter, the comparator uses a threshold
  value until a hardware or software trigger occurs. If not enabled, the
  block sets the initial threshold value to 5V.
- `Hysteresis—` Compare the upper and lower limit
  threshold values against the analogue input signal. In this mode, you can
  update the new threshold limit values using threshold trigger or software
  trigger events.
- `Ramp—` Compare the ramp threshold signal against the
  analogue input signal. You can configure the start value, end value, step
  size (indicating the increment in voltage for every step) and step width
  (indicating the increment in time for every step) of the ramp signal.
  Control the start and end of ramp mode using below cases:

  - Start ramp on software trigger and end on reaching the End of
    Threshold Value (ETV)
  - Start ramp on software trigger and end on receiving a
    hardware trigger or reaching the ETV value
  - Start ramp on software trigger and end on Boundary flag
    transition or reaching the ETV value
  - Start ramp on hardware trigger and end on reaching the ETV
    value
  - Start ramp on hardware trigger and end on receiving another
    hardware trigger or reaching the ETV value

  You can use this mode of operation to control input signal behavior
  during system soft start or power-down operation without software
  intervention.

`Normal`, `Hysteresis` or
`Ramp`.

Selecting an operation mode enables options in the
**Threshold** tab of the FCC
Peripheral Configuration.

### **Enable threshold input** — Option to enable threshold input `on` (default) | `off`

Select this parameter to configure the **threshold** input
port.

#### Dependencies

To enable this parameter, set the **Mode** parameter to
`Normal` or
`Hysteresis`.

### **Enable ramp configuration inputs** — Option to enable ramp configuration input ports `on` (default) | `off`

Select this parameter to enable the input ports for configuring the ramp mode.

When you select this parameter, the block configures the
**stepWidth**, **stepSize**,
**rampStart**, and **rampEnd** input
ports.

#### Dependencies

To enable this parameter, set the **Mode** parameter to
`Ramp`.

### **Enable threshold output** — Option to enable threshold output `on` (default) | `off`

Select this parameter to configure the **threshold** output
port.

#### Dependencies

To enable this parameter, set the **Mode** parameter to
`Ramp`.

## Libraries

Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / AURIX TC4x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

## Description

Detect when analog input signal crosses 10-bit threshold value

The FCC block models a fast compare comparator (FCC) that detects when the value
crossings of an analog input signal crosses a programmable 10-bit threshold value. The
block outputs the status of the boundary flag as a Boolean value.
