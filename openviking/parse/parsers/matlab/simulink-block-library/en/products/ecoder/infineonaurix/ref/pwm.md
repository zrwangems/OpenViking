---
type: simulink-block
title: 'PWM'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC4x / Peripheral Management / AURIX TC4x'
documentation_page: 'pwm'
documentation_source_path: 'infineonaurix/ref/pwm.html'
language: en
---

# PWM

## Ports

### Input

### **duty** — Input value which determines duty cycle `Float range between [0-100]`

The value sent to the block input determines the duty cycle of the
square wave that the board outputs on the specified PWM pin specified in
PWM Peripheral Configuration.

**Data Types:** `Float`

### **freq** — Input port determines frequency of PWM signal `scalar`

The freq port determines the frequency of PWM signal for the selected
channels. When you enable the frequency port, the port accepts a scalar
input value and sets it as the frequency of the timer unit.

#### Dependencies

To enable this port, select the **Enable frequency
input** parameter.

### **phase** — Phase of selected channel `scalar` | `vector`

The phase port accepts an input value in the range of `0 to
2`pi and sets the phase for the corresponding channel. It
accepts `N x 1` values corresponding to the
**N** channels selected.

#### Dependencies

To enable this port, select the **Enable phase
input** parameter.

**Data Types:** `single` | `double`

### **dtm\_rise** — Rising dead time module `scalar` | `vector`

The dtm\_rise port accepts the rising dead time values in seconds. The
timer unit selected in the PWM peripheral app should have DTM sub module
for this feature. It accepts `N x 1` values
corresponding to the **N** channels selected.

#### Dependencies

To enable this port, select the **Enable dead time
properties input** parameter.

**Data Types:** `Float` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

### **dtm\_fall** — Falling dead time module `scalar` | `vector`

The dtm\_fall port accepts the falling dead time values in seconds. The
timer unit selected in the PWM peripheral app should have DTM sub module
for this feature. It accepts `N x 1` values
corresponding to the **N** channels selected.

#### Dependencies

To enable this port, select the **Enable dead time
properties input** parameter.

**Data Types:** `Float` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`
### Output

### **Status** — Status of the PWM module `scalar`

The block outputs the status of the PWM module as one of these
values:

- `255—`Unknown state
- `0—` Initialized
- `1—` Running
- `2—` Stopped
- `3—` Error

#### Dependencies

To view this port, select the **Enable status
output** parameter.

**Data Types:** `uint8`

### **msg** — SoC Blockset simulation message `bus`

The port outputs the PWM bus object in the SoC Blockset™ simulation message format during simulation. The PWM bus
object contains the information received by the block at the input
ports.

#### Dependencies

To view this port, select the **Enable simulation
port** parameter and set the port type to **SoC
Data (Message based)**.

### **sig** — Simulink based simulation signal `scalar` | `vector`

The port outputs the PWM bus object during simulation. The PWM bus
object contains the information received by the block at the input
ports.

#### Dependencies

To view this port, select the **Enable simulation
port** parameter and set the port type to
**Signal**.

## Parameters

### Basic

### **Enable frequency input** — Select to enable input frequency port `off` (default) | `on`

Select this parameter to set the PWM frequency.

When you select the **Enable frequency input**
parameter, the block configures an input port,
`freq`.

### **Enable phase input** — Select to enable input phase port `off` (default) | `on`

Select this parameter to set the phase of selected channel.

When you select the **Enable phase input** parameter,
the block configures an input port, `phase`.

### **Enable status output** — Select to configure the status port `off` (default) | `on`

When you select the **Enable status output**
parameter, the block configures `Status` output
port.

### **Enable simulation port** — Enable peripheral simulation ports in the block `off` (default) | `on`

Select this parameter to enable peripheral simulation
capability.

### **Port Type** — Specify the type of peripheral simulation port `SoC Data (Message based)` (default) | `Signal`

Select this parameter to configure either the SoC compatible or the
Simulink® signal based simulation ports to enable peripheral
simulation capability.

#### Dependencies

To view this parameter, select the **Enable simulation
port** parameter.

### Advanced

### **Number of channels** — Select required channels `1` (default) | `2` | `3` | `...`

Select the required number of PWM channels to send the duty cycles.
The number of channels determines the size of the input ports
`phase`, `dtm_rise`, and
`dtm_fall`.

The number of channels selected depends on the timer module selection
in PWM peripheral configuration app.

- `TOM—`16 channels are available
- `ATOM—`8 channels are available

### **Enable dead time properties input** — Select to enable rising and falling input ports `off` (default) | `on`

Select this parameter to determine the PWM dead time value in
seconds.

For more information on standard dead time generation, see Dead-Time Module Properties.

**Note**

Enabling the dead time properties parameter in the block
configures the `dtm_rise` and
`dtm_fall` input ports. To use the dead
time functionality, go to PWM Peripheral Configuration in the Hardware Mapping
window and configure the corresponding dead time parameters in
**Module** and **Channel**
tabs.

## Libraries

Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / AURIX TC4x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022b**

## Description

Generate pulse width modulated waveforms

The block input controls the duty cycle of the square waveform for the corresponding
channel. An input value of `0` produces a `0` percent
duty cycle and an input value of `100` produces a
`100` percent duty cycle. It accepts `N x 1`
values of duty cycles corresponding to the **N** channels
selected.
