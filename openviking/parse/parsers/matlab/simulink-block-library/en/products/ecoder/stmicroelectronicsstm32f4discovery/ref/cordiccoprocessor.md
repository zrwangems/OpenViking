---
type: simulink-block
title: 'CORDIC co-processor'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Computing Peripherals'
documentation_page: 'cordiccoprocessor'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/cordiccoprocessor.html'
language: en
---

# CORDIC co-processor

## Ports

### Input

### **theta** — sin/cos/sinh/cosh scalar

Theta is an angle in radians divided by ᴨ (pi), [-1,1]
for sin or cos function.

Theta is hyperbolic angle for hyperbolic functions [-0.559, 0.559]. For
hyperbolic function the input values exceeding the range are saturated.

#### Dependencies

To enable this port, set **Function** to either
`sin`, `cos`, `sin and
cos` or `sinh and cosh`.

**Data Types:** `fixdt(1,32,31)` | `int32`

### **x and y** — atan2/mod scalar

- `x` - x coordinate
- `y` - y coordinate

The range is [-1, 1].

#### Dependencies

To enable this port, set **Function** to either
`atan2`, `mod`, `atan2 and
mod`.

**Data Types:** `fixdt(1,32,31)` | `int32`
### Output

### **function** — Result of CORDIC function boolean

The block outputs the result of the selected function. Example, if you
select function as `sin and cos`, the block outputs the result
of sin and cos function.

**Note**

For hyperbolic function `sinh` or
`cosh`, a gain of 2 must be added to the
output.

**Data Types:** `fixdt(1,32,31)`

### **Status** — Execution status scalar

The block outputs CORDIC execution status.

- `0` - Successful
- `1` - Unsuccessful

#### Dependencies

To enable this port, select the **Output status**
parameter.

**Data Types:** `Boolean`

### **Executed func** — Execution function status scalar

The block outputs CORDIC execution function status.

The executed CORDIC function provides the following status:

- `0` - cos
- `1` - sin or sin and cos
- `2` - atan2 or atan2 and mod
- `3` - mod
- `5` - cosh
- `6` - sinh or sinh and cosh

#### Dependencies

To enable this port, set DMA mode to Read only and select the
**Execution function** parameter.

**Data Types:** `int32`

### **Executed iters** — Execution iteration status scalar

The block outputs the executed iterations in the previous
calculation.

The executed CORDIC iteration provides the following status:

- `0` - cos
- `1` - sin or sin and cos
- `2` - atan2 or atan2 and mod
- `3` - mod
- `5` - cosh
- `6` - sinh or sinh and cosh

#### Dependencies

To enable this port, set DMA mode to Read only and select the
**Execution iteration** parameter.

**Data Types:** `int32`

### **Executed array size** — Execution array size status scalar

The block outputs the executed array size in the previous
calculation.

The executed CORDIC array size provides the following status:

- `0` - cos
- `1` - sin or sin and cos
- `2` - atan2 or atan2 and mod
- `3` - mod
- `5` - cosh
- `6` - sinh or sinh and cosh

#### Dependencies

To enable this port, set DMA mode to Read only and select the
**Execution array size** parameter.

**Data Types:** `int32`

## Parameters

### **Function** — Select math function `sin and cos` (default) | `sinh and cosh` | `atan2 and mod` | `sin` | `cos` | `sinh` | `cosh` | `atan2` | `mod`

Select the trigonometric or hyperbolic function.

### **Number of iterations** — Select iterations `24` (default) | `4` | `8` | `12` | `16` | `…`

Select the iterations to improve the precision of the result.

### **CORDIC mode** — Select CORDIC mode `DMA` (default) | `Zero overhead`

Select **DMA** or **Zero overhead** as CORDIC mode.

- `Zero overhead` - The data is written and read from
  the CORDIC co-processor individually.
- `DMA` - The process of looping through the array of
  element is accomplished by DMA.

### **DMA mode** — Select DMA mode `Write and Read` (default) | `Write only` | `Read only`

Enables user to perform write and read operations of DMA from a single
block.

- `Write only` - perform write operation of DMA
- `Read` - perform read operation of DMA

#### Dependencies

To enable this parameter, set the **CORDIC
mode** to DMA.

### **Output data type** — Select DMA output data type `fixdt(1,32,31)` (default) | `int32` | `Read only`

Specify the output data type for CORDIC co-processor.

#### Dependencies

To enable this parameter, set the **DMA mode**
to **Read only**.

### **Input size** — Specify DMA input size `1` (default)

Specify the input size for the CORDIC co-processor.

The user obtains a valid output when this parameter aligns with the input size
of the write block.

#### Dependencies

To enable this parameter, set the **DMA mode**
to **Read only**.

### **Executed function** — Enable executed function `off` (default) | `on`

When you select this parameter, the block configures **Executed func** output port. The port outputs the executed function
in a previous step.

#### Dependencies

To enable this parameter, set the **DMA mode**
to **Read only**.

### **Executed iterations** — Enable executed iterations `off` (default) | `on`

When you select this parameter, the block configures **Executed iters** output port. The port outputs the executed
iterations in a previous step.

#### Dependencies

To enable this parameter, set the **DMA mode**
to **Read only**.

### **Executed array size** — Enable executed array size `off` (default) | `on`

When you select this parameter, the block configures **Executed array size** output port. The port outputs the executed
array size in a previous step.

#### Dependencies

To enable this parameter, set the **DMA mode**
to **Read only**.

### **Sample time** — Frequency at which block reads pin value `-1` (default) | `non-negative real value`

Specify how often (in seconds) the block reads the pin value. Enter a value
greater than zero. When you specify this parameter as -1, Simulink determines the
best sample time for the block based on the block context within the model.

#### Dependencies

To enable this parameter, set the **DMA mode**
to **Read only**.

### **Timeout (in ms)** — DMA timeout `10` (default)

Specify the DMA timeout in microseconds.

### **Enable preemption** — Select enable preemption `off` (default) | `on`

Select to enable the preemption.

### **Output status** — Enable output status `off` (default) | `on`

When you select this parameter, the block configures **Status** output port. The Status port outputs the status of
execution.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023b**

## Description

Enable hardware acceleration of trigonometric and hyperbolic mathematical functions

The CORDIC co-processor block provides hardware acceleration of trigonometric and
hyperbolic mathematical functions used in computationally intensive application to perform
other tasks. The CORDIC co-processor block supports zero overhead mode.
