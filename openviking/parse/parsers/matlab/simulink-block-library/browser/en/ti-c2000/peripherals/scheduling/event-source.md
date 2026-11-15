---
type: simulink-block
title: 'Event Source'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Scheduling'
documentation_page: 'eventsource'
documentation_source_path: 'ref/eventsource.html'
language: en
---

# Event Source

## Ports

### Input

### **data** — Input data numeric vector

Input data, specified as a numeric vector. The block converts this data into an
event that corresponds to the rate of the input data. You can use this event to drive
an event-driven task in the Task Manager block.

#### Dependencies

To enable this port, set the **Input** parameter to
`From input port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **event** — Task event signal scalar

This port sends a task event signal that triggers the Task Manager (SoC Blockset)
block to execute the associated event-driven task.

**Data Types:** `rteEvent`

## Parameters

### **Input** — Source of input data `From dialog` (default) | `From input port` | `From timeseries object`

Set the input data source for the block by selecting one of these values.

- `From dialog` — Input a one-dimensional array of data
  by using a function. Specify this function for the **Value**
  parameter.
- `From input port` — Input data and signals using input
  ports on the block.
- `From timeseries object` — Input data and time values
  using a timeseries object that you created in MATLAB®. For more information see Time Series Objects and Collections.

### **Sample time** — Time interval of sampling `-1` (default) | nonnegative scalar

Specify a discrete time interval, in seconds, at which the block outputs
data.

#### Dependencies

To enable this parameter, set the **Input** parameter to
`From dialog`.

### **Object name** — Name of timeseries object `[]` (default) | timeseries object

Specify a `timeseries` object. This `timeseries`
object provides the input data for the block. For more information about time series
objects, see Time Series Objects and Collections.

#### Dependencies

To enable this parameter, set the **Input** parameter to
`From timeseries object`.

## Libraries

SoC Blockset / Processor Testbench C2000 Microcontroller Blockset / Scheduling Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / Test Bench Blocks Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / Test Bench Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

## Description

Simulate and playback recorded task events

The Event Source block, connected to the Task Manager (SoC Blockset) block,
enables you to simulate tasks events in your Simulink® model. Task timing data can be provided from the block mask, an external
file, or from an input port driven by other model signals.
