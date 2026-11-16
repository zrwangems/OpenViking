---
type: simulink-block
title: 'HDL Counter'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'hdlcounter'
documentation_source_path: 'ref/hdlcounter.html'
language: en
---

# HDL Counter

## Ports

### Input

### **rst** — Local reset port scalar

Local reset port for the counter that when high resets the count
value.

#### Dependencies

To enable this port, set **Local reset
port**.

**Data Types:** `Boolean`

### **load** — Load port scalar

Load port that when high sets the counter to the load value,
`load_val`.

#### Dependencies

To enable this port, set **Load ports**.

**Data Types:** `Boolean`

### **load\_val** — Load port value scalar

Data value to load for setting the count value when high input is
given to the load port.

#### Dependencies

To enable this port, set **Load ports**.

**Data Types:** `Boolean`

### **enb** — Count enable port scalar

Enable signal that specifies whether the counter should count from the
previous value. When this signal is high, the counter counts continues
up or down depending on the direction. When this signal is low, the
counter holds the previous value.

#### Dependencies

To enable this port, set **Count enable
port**.

**Data Types:** `Boolean`

### **dir** — Count direction port scalar

Count direction that specifies whether to count up or count down. This
port interacts with **Step value** to determine count direction.

- `1`: This value is the default that
  results in an up counter. The **Step
  value** is added to the current counter value
  to compute the next value.
- `0`: This value results in a down
  counter. The **Step value** is subtracted
  from the current counter value to compute the next
  value.

#### Dependencies

To enable this port, set **Count direction
port**.

**Data Types:** `Boolean`
### Output

### **count** — Counter value scalar

This is the counter value. By default, if you do not enable the input
ports, the counter counts up to a value that is determined based on the
**Counter type**, the **Count to
value**, and the **Word length**.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **count\_hit** — Counter limit indicator scalar

Counter limit indicator, returned as a Boolean scalar.

- `1`: indicates that the counter reached its
  limit.
- `0`: indicates that the counter did not reach
  its limit.

#### Dependencies

To enable this port, select the **Count hit output
port** parameter.

**Data Types:** `Boolean`

## Parameters

### **Counter type** — Counter behavior `Free running` (default) | `Count limited` | `Modulo`

Counter behavior that determines whether to model a free running,
count-limited, or module hardware counter.

- `Free running` (default): The counter
  continues to increment or decrement by the **Step
  value** until reset.
- `Count limited`: The counter
  increments or decrements by the **Step value**
  until it is exactly equal to the **Count to
  value**. If the **Step value**
  value is such that the count value does not exactly equal the
  **Count to value**, then it can continue
  counting to a threshold value that is determined by the word
  length.
- `Modulo`: The counter increments or
  decrements by the **Step value** until it
  reaches the **Count to value**. If the
  **Step value** value is such that the count
  value does not exactly equal the **Count to
  value**, then the counter wraps to a value that is
  determined by the wrapping step value.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CountType` |
| **Type:** character vector |
| **Value:** `'Free running'` | `'Count limited'` | `'Modulo'` |
| **Default:** `'Free running'` |

### **Initial value** — Counter value after reset `0` (default)

The value to which the counter resets. The default value is
`0`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CountInit` |
| **Type:** character vector |
| **Value:** An integer greater than or equal to zero |
| **Default:** `'0'` |

### **Step value** — Step value for count `1` (default)

Value added to counter at each sample time. The default value is
`1`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CountStep` |
| **Type:** character vector |
| **Value:** An integer greater than or equal to zero |
| **Default:** `'1'` |

### **Count to value** — Threshold count value `25` (default)

When you use a `Count limited` counter, if the
count is exactly equal to **Count to value**, the count
restarts at the **Initial value**. If the count value
exceeds the **Count to value**, the counter continues
counting to a threshold value that depends on the **Word
length**. The default is `25`.

When you use a `Modulo` counter, if the count reaches the
**Count to value**, the count restarts at a value that
is determined by the wrapping step value.

#### Dependencies

To enable this parameter, set **Counter type** to
`Count limited` or
`Modulo`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CountMax` |
| **Type:** character vector |
| **Value:** An integer greater than or equal to zero |
| **Default:** `'25'` |

### **Count from** — Criteria for count from value `Initial value` (default) | `Specify`

Specifies the parameter that sets the start value after rollover when you
use a `Count limited` or `Free
running` counter. When you use a
`Modulo` counter, the counter can rollover to a
wrapping step value that is different from the value to count from. When set
to `Specify`, the **Count from
value** parameter is the start value after rollover. The
default is `Initial value`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CountFromType` |
| **Type:** character vector |
| **Value:** `'Initial value'` | `'Specify'` |
| **Default:** `'Initial value'` |

### **Count from value** — Initial value to count from `0` (default)

Counter value after rollover when **Count from** is set
to `Specify`. The default is 0.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CountFrom` |
| **Type:** character vector |
| **Value:** `'Initial value'` | `'Specify'` |
| **Default:** `'Initial value'` |

### **Local reset port** — Local port to reset counter `off` (default) | `on`

When selected, creates a local reset port, `rst`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CountResetPort` |
| **Type:** character vector |
| **Value:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Load ports** — Port for load value `off` (default) | `on`

When selected, creates a load data port, `load_val`, and
load trigger port, `load`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CountLoadPort` |
| **Type:** character vector |
| **Value:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Count enable port** — Port to enable counting `off` (default) | `on`

When selected, creates a count enable port, `enb`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CountEnbPort` |
| **Type:** character vector |
| **Value:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Count direction port** — Port for count direction `off` (default) | `on`

When selected, creates a count direction port, `dir`.

Enabling this parameter disables the **Count hit output port**
parameter.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CountDirPort` |
| **Type:** character vector |
| **Value:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Count hit output port** — Port for count limit `off` (default) | `on`

Select this parameter to enable the **count\_hit** output port.

Enabling this parameter clears the **Count direction port**
parameter.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CountHitOutputPort` |
| **Type:** character vector |
| **Value:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Counter output data is** — Output data type signedness `Unsigned` (default) | `Signed`

Output data type signedness. The default is `Unsigned`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CountDataType` |
| **Type:** character vector |
| **Value:** `'Unsigned'` | `'Signed'` |
| **Default:** `'off'` |

### **Word length** — Counter word length `8` (default)

Bit width, including sign bit, for an integer counter; word length for a
fixed-point data type counter. The minimum value if **Output data
type** is `Unsigned` is
`1`, `2` if
`Signed`. The maximum value is
`125`. The default is `8`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CountWordLen` |
| **Type:** character vector |
| **Value:** An integer greater than or equal to one |
| **Default:** `'8'` |

### **Fraction length** — Counter fraction length `0` (default)

Fixed-point data type fraction length. The default is
`0`.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CountFracLen` |
| **Type:** character vector |
| **Value:** An integer greater than or equal to zero |
| **Default:** `'0'` |

### **Sample time** — Counter sample time `1` (default)

Sample time. The default is `1`. This parameter is not
available, and the block inherits its sample time from the input ports when
any of these parameters is selected:

- **Local reset port**
- **Load ports**
- **Count enable port**
- **Count direction port**

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `CountSampTime` |
| **Type:** character vector |
| **Value:** An integer greater than or equal to one |
| **Default:** `'1'` |

## Libraries

HDL Coder / Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that
affect HDL implementation and synthesized
logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline. |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline. |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline. |

**Restrictions**

- If the bitwidth of the input signal to a HDL Counter
  exceeds the data type limit, the generated HDL code can produce
  incorrect simulation results. To accommodate the larger bit width, use a
  larger data type.
- The block does not support vectors.
  Only scalar types are supported for block
  inputs and outputs.
- Load value used in `Modulo` counter mode must
  be within the range of the **Count from** and
  **Count to value** to avoid simulation
  mismatches.

## Version History

**Introduced in R2014a**

## Description

Free-running or count-limited hardware counter

The HDL Counter block models a free-running, count-limited, or modulo
hardware counter that supports signed and unsigned integer and fixed-point data types.
The counter emits its value for the current sample time. During simulation, this block
does not report warnings or errors due to wrap on overflow. To report these warnings,
see `Simulink.restoreDiagnostic`.

By default, the counter does not have input ports. The counter counts up from an
initial value to a threshold value based on the **Counter type**, the
**Count to value**, and the **Word length**. The
output data type of the counter depends on the **Counter output data**,
**Word length**, and **Fraction length**.
