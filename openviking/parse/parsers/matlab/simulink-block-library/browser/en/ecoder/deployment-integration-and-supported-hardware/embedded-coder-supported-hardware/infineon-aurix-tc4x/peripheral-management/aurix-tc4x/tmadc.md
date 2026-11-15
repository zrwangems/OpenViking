---
type: simulink-block
title: 'TMADC'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC4x / Peripheral Management / AURIX TC4x'
documentation_page: 'tmadc'
documentation_source_path: 'infineonaurix/ref/tmadc.html'
language: en
---

# TMADC

## Ports

### Input

### **trigger** — Port to trigger the conversion `scalar`

Triggers the TMADC input pin for conversion via software
trigger.

From trigger port when mode is set trigger only enables you to provide
the sample time.

- `1—` TMADC start of conversion is
  triggered
- `0—`TMADC start of conversion is not
  triggered

#### Dependencies

To view this port, set the **Mode** parameter to
`Trigger only`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **msg** — SoC Blockset simulation message `scalar`

This port receives SoC Blockset™ message from the interface blocks and the TMADC block
converts this message and outputs it at the **result**
port during simulation.

#### Dependencies

To view this input port, set the **Mode** to
`Trigger and read` or `Read
results only` and select the **Enable
simulation port** parameter and set the port type as
**SoC Data (Message based)**.

### **sig** — Simulink based simulation signal `scalar` | `vector`

The simulation-only Simulink® signal input port acts as a pass-through for the output of
the TMADC block during simulation.

#### Dependencies

To view this port, set **Mode** to
`Trigger and read` or `Read
results only` and select the **Enable
simulation port** parameter and set the port type to
**Signal**.
### Output

### **result** — Voltage as 12-bit value `scalar` | `vector`

The block outputs the voltage as a 12-bit value and the output port is
an array `N x 1` where **N** is
defined based on the number of channels selected.

#### Dependencies

To enable this port, set the **Mode** parameter
to `Trigger and read` or `Read
results only`.

**Data Types:** `uint16`

### **status** — Status of read operation `scalar`

The block outputs the status of read operation at this port as one of
these values:

- `0—`No error in reading the result after
  successful trigger for the corresponding channel
- `1—`Error in reading the result after
  successful trigger for the corresponding channel

#### Dependencies

To enable this port, set the **Mode** to
`Read results only` and select the
**Enable status port** parameter.

**Data Types:** `double`

### **timestamp** — Status of 16-bit counter value `scalar` | `vector`

The port outputs the status of the 16-bit counter value of timestamp
counter.

#### Dependencies

To enable this port, select the **Enable
timestamp** parameter.

**Data Types:** `Boolean`

### **event** — Event message to start conversion `scalar`

This port outputs an event message at each trigger to start the
conversion during simulation.

#### Dependencies

To view this port, set the **Mode** to
`Trigger only` and select the
**Enable simulation port** parameter, and set
the port type to **SoC Data (Message
based)**.

### **triggersig** — Simulink based trigger signal for simulation `scalar` | `vector`

This port outputs the data received at **trigger**
input port as a signal during simulation.

#### Dependencies

To view this port, set the **Mode** to
`Trigger only` and select the
**Enable simulation port** parameter, and set
the port type to **Signal**.

## Parameters

### **Mode** — Operation mode of the block `Trigger and read` (default) | `Trigger only` | `Read results only`

Select one of these operation modes:

- `Trigger and read—` Select this option to
  trigger conversion at every sample time. The block waits until the
  conversion is complete and outputs the results. This option enables
  the output port **result**.
- `Trigger only—` Select this option to
  trigger the selected channel via a software trigger. This option
  enables the input port **trigger**. As the block
  does not show the conversion results in this mode, you have to use
  another TMADC block with the **Mode** parameter set
  to `Read results only` to display the
  conversion results.
- `Read results only—` Select this option
  for the block to read the result at the selected channel. The block
  outputs `0` at the **status** port
  if it is able to read the result and `1` otherwise.
  This option enables the output port
  **result**.

### **Number of channels** — Select required channels `1` (default) | `2` | `3` | `...`

If you set the **Mode** to `Trigger and
read`, then select the required number of channels ranging
between `1` through `16`. The number of
channels are limited to 1 if you set the **Mode** to
`Trigger only` or `Read results
only`.

### **Enable timestamp** — Enable timestamp `off` (default) | `on`

Select to enable the timestamp.

When you select the `Enable timestamp` parameter, the
block configures an additional output port, timestamp similar to result port
to read the timestamp.

**Note**

- TMADC module has 16-bit timestamp counter which resets
  after every counter overflow.
- Enable timestamp parameter is not available when mode is
  set to `Trigger only`.

### **Enable status port** — Configure status port `off` (default) | `on`

When you select this parameter, the block configures the
**status** output port. The **status**
port outputs the status of the conversion result.

#### Dependencies

To enable this port, set the **Mode** parameter to
`Read results only`.

### **Sample time** — Frequency at which block reads input analog pin(s) `-1` (default) | `scalar` | `vector`

Specify in seconds how often the block should read the analog
pin(s).

When you specify this parameter as `-1`, Simulink determines the best sample time for the block based on the
block context within the model.

#### Dependencies

To enable the **Sample time** parameter, set the
**Mode** parameter to either `Trigger
and read` or `Read results
only`.

### **Enable simulation port** — Enable peripheral simulation ports in the block `off` (default) | `on`

Select this parameter to enable peripheral simulation capability.

### **Port Type** — Specify the type of peripheral simulation port `SoC Data (Message based)` (default) | `Signal`

Select this parameter to configure either the compatible or the
Simulink signal based simulation ports to enable peripheral simulation
capability.

#### Dependencies

To view this parameter, select the **Enable simulation
port** parameter.

## Libraries

Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / AURIX TC4x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022b**

## Description

Measure voltage of an analog input pin

Measure the voltage of an analog input pin.

The Time Multiplexed Analog to Digital Converter (TMADC) block outputs the voltage as
a 12-bit value and the output port is an array `N x 1` where
**N** is defined based on the number of channels selected.
