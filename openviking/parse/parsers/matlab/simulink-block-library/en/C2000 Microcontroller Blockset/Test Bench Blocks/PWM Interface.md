---
type: simulink-block
title: 'PWM Interface'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Test Bench Blocks'
documentation_page: 'pwminterface'
documentation_source_path: 'ref/pwminterface.html'
language: en
---

# PWM Interface

## Ports
```yaml
ports:
- name: msg
  summary: SoC message data numeric vector
  direction: input
  data_types: SoCData
- name: PWM
  summary: Pulse-width-modulated signal scalar
  direction: output
  data_types: double
- name: ~PWM
  summary: Complimentary pulse-width-modulated signal scalar
  direction: output
  data_types: double
- name: dCycle
  summary: Analog approximation of pulse-width-modulated signal scalar
  direction: output
  data_types: double
- name: event
  summary: Event emitted on each PWM cycle scalar
  direction: output
  data_types: rteEvent
- name: event*n*
  summary: Replicate event emitted on each PWM cycle scalar
  direction: output
  data_types: rteEvent
- name: interrupt
  summary: Interrupt event emitted on each PWM cycle scalar
  direction: output
  data_types: rteEvent
```

### Input

### **msg** — SoC message data numeric vector

This port receives the duty cycle data from the **msg** port of a connected PWM Write block.

**Data Types:** `SoCData`
### Output

### **PWM** — Pulse-width-modulated signal scalar

This port outputs the pulse-width-modulated rectangular wave defined by the
**dCycle** input port.

#### Dependencies

To enable this port, set the **Output mode** parameter to
`Switching`.

**Data Types:** `double`

### **~PWM** — Complimentary pulse-width-modulated signal scalar

This port outputs the complimentary **PWM** signal.

#### Dependencies

To enable this port, set the **Output mode** parameter to
`Switching`.

**Data Types:** `double`

### **dCycle** — Analog approximation of pulse-width-modulated signal scalar

This port emits the averaged value of the PWM waveform, which is a pass-through of
the duty cycle input value. This image shows the average output signal equivalent to
the PWM output.

Approximate waveform of PWM signal.

#### Dependencies

To enable this port, set the **Output mode** parameter to
`Average`.

**Data Types:** `double`

### **event** — Event emitted on each PWM cycle scalar

This port sends a message during each PWM output event that can connect to the
**start** port of the ADC Interface block to synchronize ADC and
PWM events in closed-loop systems.

#### Dependencies

To enable this port, the **Type** parameter must be set to
`ADC start` or `ADC start and PWM
interrupt`.

**Data Types:** `rteEvent`

### **event*`n`*** — Replicate event emitted on each PWM cycle scalar

This port creates a replica port of the **event** output port to
coordinate multiple ADC modules with the PWM module.

#### Dependencies

To enable this port, set the **Type** parameter to
`ADC start` or `ADC start and PWM
interrupt` and the **Number of replicas** parameter
to a value greater than or equal to 2.

**Data Types:** `rteEvent`

### **interrupt** — Interrupt event emitted on each PWM cycle scalar

This port sends a message during each PWM output event that can connect to the
Task Manager block to trigger other tasks in response to the PWM output update.

#### Dependencies

To enable this parameter, set the **Type** parameter to
`PWM interrupt` or `ADC start and PWM
interrupt`.

**Data Types:** `rteEvent`
## Parameters
```yaml
parameters:
- name: PWM waveform period (s)
  summary: Period of PWM waveform 50e-6 (default) | positive scalar
  group: Main
- name: Output mode
  summary: Output mode Switching (default) | Average
  group: Main
- name: Counter mode
  summary: Counter waveform Up-Down (default) | Up | Down
  group: Main
- name: Sampling mode
  summary: Sampling mode End of PWM period (default) | Mid or End of PWM period | Immediate (at compare matches)
  group: Main
- name: Dead time (s)
  summary: Dead band switching delay 1e-6 (default) | positive scalar
  group: Main
- name: At *position* of period
  summary: Signal change at position in period High | Low | Change | NoChange
  group: PWM Output
- name: At compare *n*
  summary: Signal change at comparator n trigger High | Low | Change | NoChange
  group: PWM Output
- name: At compare *n* *direction* count
  summary: Signal change at comparator n trigger High | Low | Change | NoChange
  group: PWM Output
- name: Phase offset in degree (0-360)
  summary: PWM waveform offset scalar from 0 to 360
  group: Phase
- name: Type
  summary: Type of events to generate ADC start (default) | PWM interrupt | ADC start and PWM interrupt
  group: Event
  type: 'value is set to:'
- name: ADC start condition
  summary: Trigger mode relative to PWM waveform End of PWM period (default) | Mid of PWM period | Mid or End of PWM period
    | Compare 1 up count | Compare 1 down count | Compare 2 up count | Compare 2 down count
  group: Event
- name: Generate on
  summary: Generate event on multiple of PWM update 1st event (default) | nth event | 16th event
  group: Event
- name: Number of replicas
  summary: Generate replica event ports 1 (default) | integer from 1 to 16
  group: Event
- name: PWM interrupt condition
  summary: Trigger mode relative to PWM waveform End of PWM period (default) | Mid of PWM period | Mid or End of PWM period
    | Compare 1 up count | Compare 1 down count | Compare 2 up count | Compare 2 down count
  group: Event
- name: Interrupt latency (s)
  summary: Interrupt generation latency 0 (default) | positive number
  group: Event
- name: Generate on
  summary: Generate event on multiple of PWM update 1st event (default) | nth event | 16th event
  group: Event
```

### Main

### **PWM waveform period (s)** — Period of PWM waveform `50e-6` (default) | positive scalar

Specify the period of the PWM waveform in seconds.

**Note**

For `PWM waveform period (s)` of 10ns, the duty cycle must be
greater than 1%.

### **Output mode** — Output mode `Switching` (default) | `Average`

Simulate the output signal as either a true PWM waveform by specifying
`Switching` or as the average of the duty cycle by specifying
`Average`.

**Example:** `Switching`

### **Counter mode** — Counter waveform `Up-Down` (default) | `Up` | `Down`

The counter mode specifies the shape of the underlying sawtooth waveform that
drives the PWM output signal inside the PWM module. In `Up` mode, the
sawtooth counter increments to the maximum and then resets to zero on each period. In
`Down` mode, the sawtooth counter decrements to zero then resets to
the maximum. In `Up-Down` mode, the sawtooth counter oscillates from
zero to the maximum value.

**Example:** `Up`

### **Sampling mode** — Sampling mode `End of PWM period` (default) | `Mid or End of PWM period` | `Immediate (at compare matches)`

Specify the time at which the input duty cycle is sampled.

**Example:** `Mid or End of PWM period`

### **Dead time (s)** — Dead band switching delay `1e-6` (default) | positive scalar

A time delay is introduced between turning off one of the transistors of a leg of
an inverter and turning on the other transistor to ensure that a dead short circuit
does not occur. This diagram shows the expected duty cycle and the delay introduced by
the transistor switching the dead band.

**Example:** `450e-9`

### PWM Output

### **At *`position`* of period** — Signal change at position in period `High` | `Low` | `Change` | `NoChange`

Specify the state of the PWM waveform signal at the
*`position`* in the waveform relative to the total period.
When set to `High` or `Low`, the
waveform output changes to `1` or `0`, respectively.
When set to `Change`, the waveform inverts the current value.
When set to `NoChange`, the waveform does not change. The
*`position`* can either be the `start` or
`mid` point of the PWM waveform. This table gives the default
settings for these parameters.

| Parameter | Default |
| --- | --- |
| **At start of period** | `High` |
| **At mid of period** | `NoChange` |

#### Dependencies

`At mid of period` is only available when the **Counter
mode** parameter is set to Up-Down.

### **At compare *`n`*** — Signal change at comparator n trigger `High` | `Low` | `Change` | `NoChange`

Specify the state of the PWM waveform signal when the internal PWM counter
triggers comparator *`n`*. When set to
`High` or `Low`, the waveform
output changes to `1` or `0`, respectively. When set
to `Change`, the waveform inverts the current value. When set
to `NoChange`, the waveform does not change. Two comparators,
`1` and `2`, are available to modify the PWM
signal. This table gives the default settings for these parameters.

| Parameter | Default |
| --- | --- |
| **At compare 1** | `Low` |
| **At compare 2** | `NoChange` |

#### Dependencies

**At compare 1** and **At compare 2**
parameters are only available when the **Counter mode** parameter
is set to `Up` or `Down`.

### **At compare *`n`* *`direction`* count** — Signal change at comparator n trigger `High` | `Low` | `Change` | `NoChange`

Specify the state of the PWM waveform signal when the internal PWM counter crosses
the comparator *`n`* value in the specified
*`direction`*. When set to `High` or
`Low`, the waveform output changes to `1`
or `0`, respectively. When set to `Change`,
the waveform inverts the current value. When set to
`NoChange`, the waveform does not change. Two comparators,
`1` and `2`, are available to modify the PWM
signal. This table gives the default settings for these parameters.

| Parameter | Default |
| --- | --- |
| **At compare 1 up count** | `Low` |
| **At compare 1 down count** | `High` |
| **At compare 2 up count** | `NoChange` |
| **At compare 2 down count** | `NoChange` |

#### Dependencies

These arguments are only available when the **Counter mode**
parameter is set to `Up-Down`.

### Phase

### **Phase offset in degree (0-360)** — PWM waveform offset scalar from `0` to `360`

Specify the phase of the PWM waveform relative period of waveform. The phase is
represented as a scalar between `0` to `360`
degrees.

### Event

### **Type** — Type of events to generate `ADC start` (default) | `PWM interrupt` | `ADC start and PWM interrupt`

Specify the types of events on which to generate events. When the
**Type**value is set to:

- `ADC start` — Generate an event to trigger the start
  ADC conversion.
- `PWM interrupt` — Generate an interrupt event to
  trigger the start of a task.
- `ADC start and PWM interrupt` — Generate events for
  both ADCs and tasks.

**Example:** `ADC start and PWM interrupt`

### **ADC start condition** — Trigger mode relative to PWM waveform `End of PWM period` (default) | `Mid of PWM period` | `Mid or End of PWM period` | `Compare 1 up count` | `Compare 1 down count` | `Compare 2 up count` | `Compare 2 down count`

Specify when this block triggers an event relative to the PWM waveform.

**Example:** `Mid or End of PWM period`

#### Dependencies

To enable this parameter, the **Type** parameter must be set to
`ADC start` or `ADC start and PWM
interrupt`.

### **Generate on** — Generate event on multiple of PWM update `1st event` (default) | `nth event` | `16th event`

Specify to generate and output an ADC trigger event on the specified multiple of
the PWM vent. For example, if **Generate on** is set to the
`6th event`, the PWM Interface block
receives 6 messages updates the output 6 times before generating an ADC event
message.

**Example:** `4th event`

#### Dependencies

To enable this parameter, the **Type** parameter must be set to
`ADC start` or `ADC start and PWM
interrupt`.

### **Number of replicas** — Generate replica event ports `1` (default) | integer from `1` to `16`

Generate replica ADC event ports and events on the block. Use this coordinate the
triggering of multiple ADCs modules from a single PWM Interface
block.

**Example:** `4`

#### Dependencies

To enable this parameter, the **Type** parameter must be set to
`ADC start` or `ADC start and PWM
interrupt`.

### **PWM interrupt condition** — Trigger mode relative to PWM waveform `End of PWM period` (default) | `Mid of PWM period` | `Mid or End of PWM period` | `Compare 1 up count` | `Compare 1 down count` | `Compare 2 up count` | `Compare 2 down count`

Specify when this block triggers an interrupt event relative to the PWM
waveform.

**Example:** `Mid or End of PWM period`

#### Dependencies

To enable this parameter, the **Type** parameter must be set to
`PWM interrupt` or `ADC start and PWM
interrupt`.

### **Interrupt latency (s)** — Interrupt generation latency `0` (default) | positive number

Specify the time required by the PWM hardware module from the completion of the
output update to the generation of the interrupt in software.

**Example:** `0.00001`

#### Dependencies

To enable this parameter, the **Type** parameter must be set to
`PWM interrupt` or `ADC start and PWM
interrupt`.

### **Generate on** — Generate event on multiple of PWM update `1st event` (default) | `nth event` | `16th event`

Specify to generate and output a PWM interrupt trigger event on the specified
multiple of the PWM vent. For example, if **Generate on** is set to
the `6th event`, the PWM Interface block
receives 6 messages updates the output 6 times before generating an PWM interrupt
event message.

**Example:** `4th event`

#### Dependencies

To enable this parameter, the **Type** parameter must be set to
`PWM interrupt` or `ADC start and PWM
interrupt`.
## Libraries

SoC Blockset / Peripherals C2000 Microcontroller Blockset / Test Bench Blocks Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / Test Bench Blocks Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / Test Bench Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

To automatically generate C code for your design, and execute
on an SoC device, use the SoC Builder (SoC Blockset) tool. To
generate and execute C code for your SoC models, Embedded Coder® features are required. For more information on generating code for SoC designs,
see Use SoC Builder to Generate SoC Design (SoC Blockset).

## Version History

**Introduced in R2020b**

## Description

Simulate pulse width modulation (PWM) output from hardware

The PWM Interface block simulates the PWM output of a hardware board. This blocks gets
duty cycle data messages from a connected PWM Write block that can either generate a switching
pulse-width-modulated waveform or pass the duty cycle value to the output.
