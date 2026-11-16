---
type: simulink-block
title: 'EVADC'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC3x / Peripheral Management / AURIX TC3x'
documentation_page: 'evadc'
documentation_source_path: 'infineonaurixtc3x/ref/evadc.html'
language: en
---

# EVADC

## Ports

### Input

### **trigger** — Trigger the conversion scalar

Triggers the EVADC input pin for conversion via software trigger.

#### Dependencies

To enable this port, set the **Mode** parameter to
`ADC trigger`.

**Data Types:** `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **msg** — SoC simulation message `scalar`

This port receives message from the interface blocks and the EVADC block
converts this message and outputs it at the **result** port
during simulation.

#### Dependencies

To view this input port, set the **Mode** parameter to
`ADC read` and select the **Enable
simulation port** parameter and set the port type as
**SoC Data (Message based)**.

### **sig** — Simulink® based simulation signal `scalar` | `vector`

The simulation-only Simulink signal input port acts as a pass-through for the output of the
EVADC block during simulation.

#### Dependencies

To view this input port, set the **Mode** parameter to
`ADC read` and select the **Enable
simulation port** parameter and set the port type as
**Signal**.
### Output

### **result** — Voltage as 12-bit value scalar | vector

The block outputs the input voltage as a 12-bit value in an
`N-by-1` array, where N is defined based on the number of
channels specified in the **Number of channels**
parameter.

**Data Types:** `uint16`

### **status** — Status of read operation scalar

The block outputs the status of read operation in an
`1-by-N` array, where N represents the number of channels
specified in the **Number of channels** parameter. Each array
element represents status of read operation of individual channel as one of
these values:

- `0 —` Conversion result is available
- `1 —` Conversion result is not available

#### Dependencies

To enable this port, set the **Mode** parameter to
`ADC read` and enable the
**Status** parameter.

**Data Types:** `uint8`

### **event** — Event message to start conversion `scalar`

This port outputs an event message at each trigger to start the conversion
during simulation.

#### Dependencies

To view this port, set the **Mode** parameter to
`ADC trigger`, select the **Enable
simulation port** parameter, and set the port type to
**SoC Data (Message based)**.

### **triggersig** — Simulink based trigger signal for simulation `scalar` | `vector`

This port outputs the data received at **trigger** input
port as a signal during simulation.

#### Dependencies

To view this port, set the **Mode** parameter to
`ADC trigger` and select the **Enable
simulation port** parameter, and set the port type to
**Signal**.

## Parameters

### **Mode** — Operation mode of the EVADC block `ADC read` (default) | `ADC trigger`

Select one of these operation modes:

- `ADC read —` Select this option for the block to
  read the result at the selected channel. This option enables the output port
  **result**. Selection of this mode enables options in
  the **Input #** tab and **Group select**
  tab in the EVADC Peripheral Configuration.
- `ADC trigger —` Select this option to trigger the
  selected channel via a software trigger. This option enables the input port
  **trigger**. Selection of this mode enables options
  **Group select** tab in the EVADC Peripheral Configuration.

  **Note**

  As the block does not show the conversion results in this mode, you
  must use another EVADC block with the **Mode**
  parameter set to `ADC read` to display the
  conversion results.

### **Number of channels** — Select number of channels `1` (default) | `2` | `3` | `...`

Select the required number of channels ranging between `1`
through `16`.

### **Status** — Option to enable status port `off` (default) | `on`

When you select this parameter, the block configures the
**status** output port to output the status of the conversion
result.

#### Dependencies

To enable this port, set the **Mode** parameter to
`ADC read`.

### **Sample time** — Frequency at which block reads input analog pin(s) `-1` (default) | scalar | vector

Specify in seconds how often the block must read the analog pin(s).

When you set this parameter to `-1`, Simulink determines the best sample time for the block based on the block
context within the model.

#### Dependencies

To enable the **Sample time** parameter, set the
**Mode** parameter to `ADC
read`.

### **Enable simulation port** — Enable peripheral simulation ports in the block `off` (default) | `on`

Select this parameter to enable peripheral simulation capability.

### **Port Type** — Specify the type of peripheral simulation port `SoC Data (Message based)` (default) | `Signal`

Select this parameter to configure either the SoC message or the Simulink signal based simulation ports to enable peripheral simulation
capability.

#### Dependencies

To view this parameter, select the **Enable simulation
port** parameter.

## Libraries

Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / AURIX TC3x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

## Description

Measure voltage of an analog input pin

Measure the voltage of an analog input pin.

The Enhanced Versatile Analog to Digital Converter (EVADC) block outputs the voltage of
the input signal as a 12-bit value in an `N-by-1` array, where N is
defined based on the number of channels selected.

**Note**

If you add the same pin in multiple channels of single EVADC block, then some
channels fail to capture the converted result in external mode and Synopsys
Virtualizer Studio.
