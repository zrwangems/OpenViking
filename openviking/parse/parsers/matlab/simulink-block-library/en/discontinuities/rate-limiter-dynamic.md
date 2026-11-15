---
type: simulink-block
title: 'Rate Limiter Dynamic'
family: discontinuities
documentation_release: R2025b
official_category: 'Discontinuities'
documentation_page: 'ratelimiterdynamic'
language: en
---

# Rate Limiter Dynamic

Limit rate of change of signal

## Libraries

Simulink / Discontinuities

## Description

The Rate Limiter Dynamic block limits the rising and falling rates of
the signal.

- The external signal `up` sets the upper limit on the rising
  rate of the signal.
- The external signal `lo` sets the lower limit on the falling
  rate of the signal.

Follow these guidelines when using the Rate Limiter Dynamic
block:

- Ensure that the data types of `up` and `lo`
  are the same as the data type of the input signal `u`.

  When the lower limit uses a signed type and the input signal uses an unsigned
  type, the output signal keeps increasing regardless of the input and the
  limits.
- Use a fixed-step solver to simulate models that contain this block.

  Because the Rate Limiter Dynamic block supports only discrete
  sample time.

## Ports

### Input

### **u** — Input signal scalar

Input signal to the rate limiter algorithm.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **lo** — Limit of derivative for decreasing input scalar

Dynamic value providing the limit of the falling rate of the input
signal. Make the signal data type of `lo`the same data
type of the input signal `u`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **up** — Limit of derivative for increasing input scalar

Dynamic value providing the limit of the rising rate of the input
signal. Make the signal data type of `up`the same data
type of the input signal `u`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Y** — Output signal scalar

Output signal from the rate limiter algorithm.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `enumerated` | `bus`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

The code generator does not explicitly group primitive blocks that constitute a
nonatomic masked subsystem block in the generated code. This flexibility allows for
more efficient code generation. In certain cases, you can achieve grouping by
configuring the masked subsystem block to execute as an atomic unit by selecting the
**Treat as atomic unit** option.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
