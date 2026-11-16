---
type: simulink-block
title: 'Digital IO Interface'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals'
documentation_page: 'digitaliointerface'
documentation_source_path: 'ref/digitaliointerface.html'
language: en
---

# Digital IO Interface

## Ports

### Input

### **msg** — SoC message data scalar

This port receives the logical signal from the **msg** port of a
connected IO Data Source block.

#### Dependencies

To enable this port, set the  **IO direction** parameter
to `Output`.

**Data Types:** `SoCData`

### **in** — Input digital signal scalar

This port specifies the input digital voltage signal to convert into a
digital logical measurement.

#### Dependencies

To enable this port, set the  **IO direction** parameter
to `Input`.

**Data Types:** `single` | `double`
### Output

### **out** — Output digital signal scalar

This port outputs the logical signal value provided from the
**msg** input port.

#### Dependencies

To enable this port, set the  **IO direction** parameter
to `Output`.

**Data Types:** `single` | `double`

### **event** — Task event signal scalar

This port sends a message at each digital IO threshold event. This output
connects to the input of the Task Manager block to execute the associated
event-driven task after executing the IO event.

#### Dependencies

To enable this port, set the  **IO direction** parameter
to `Input` and select the **Enable
event** parameter.

**Data Types:** `rteEvent`

### **message** — SoC message data scalar

This port sends the Digital IO Interface input signal data as
a message to the **msg** input port of the IO Data Sink block.

#### Dependencies

To enable this port, set the  **IO direction** parameter
to `Input`.

**Data Types:** `SoCData`

## Parameters

### **IO direction** — Configure block as digital input or output `Input` (default) | `Output`

Select a value for the Digital IO Interface block to act as a
digital input or a digital output.

### **Low input voltage** — Low input voltage threshold `0.2` (default) | nonnegative scalar

Specify the lower threshold voltage of the input signal. When the signal value
crosses below the threshold, the block registers this crossing as an input change,
generating an event and new message with a digital value of
`0`.

**Example:**
`0.3`

### **High input voltage** — High input voltage threshold `2.5` (default) | nonnegative scalar

Specify the upper threshold voltage of the input signal. When the signal value
crosses above the threshold, the block registers this crossing as an input change,
generating an event and new message with a digital value of
`1`.

**Example:**
`0.3`

### **Enable event** — Option to enable event generation `on` (default) | `off`

Select this parameter for the Digital IO Interface block to
generate an event following a digital transition event. Selecting this parameter
also enables the **event** output port, which you can connect to
a Task Manager to simulate asynchronous digital read operation.

### **Condition** — Condition on when to trigger event `Rising edge` (default) | `Falling edge` | `Both`

Select the condition for when to generate the digital input event.

- `Rising edge` — Generate an event when the input
  signal on the **in** input port is greater than the
  **High input voltage** parameter value.
- `Falling edge` — Generate an event when the input
  signal on the **in** input port is less than the
  **Low input voltage** parameter value.
- `Both` — Generate an event on both conditions of
  the `Rising edge` and `Falling
  edge` options.

### **Sample time** — Sample time `-1` (default) | positive scalar

Specify the sample time (in seconds) to define the rate at which to output the
message containing the digital input data.

## Libraries

SoC Blockset / Peripherals Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / Test Bench Blocks Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / Test Bench Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021b**

## Description

Simulate digital input and output pins on processor

The Digital IO Interface block simulates the behavior of a GPIO processor
pin on a hardware board. You can configure the block as either an input digital block or an
output digital block.

When you configure this block as an input, the block captures the crossing event of an
input signal on the pin. When the crossing event occurs, the block emits the logical state
of the pin as a signal and sends an event to a Task Manager block. A task can then read the
logical value using an IO Data Sink block.

When you configure this block as an output, the block emits the logical signal from a
connected IO Data Source block.
