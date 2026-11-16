---
type: simulink-block
title: 'SinCos Embedded Optimized'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Math Transforms'
documentation_page: 'sincosembeddedoptimized'
documentation_source_path: 'ref/sincosembeddedoptimized.html'
language: en
---

# SinCos Embedded Optimized

## Ports

### Input

### **θe** — Reference voltage position scalar

Position or phase value of the reference voltage signal specified as scalar in
either per-unit, radians, or degrees.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **sin** — Sine voltage waveform scalar

Sine waveform output with a frequency that is identical to the position or phase
signal (`θe`) frequency.

**Data Types:** `single` | `double` | `fixed point`

### **cos** — Cosine voltage waveform scalar

Cosine waveform output with a frequency that is identical to the position or phase
signal (`θe`) frequency.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

### **Optimize for selected embedded target hardware** — Optimize block for selected hardware `off` (default) | on

Select this parameter to optimize the block automatically for the embedded target
hardware you are using. If you select this parameter, the block automatically selects an
approximation method (to compute the sine and cosine signals) that is optimized for your
hardware target.

For example, if you select any Texas Instruments hardware target in the **Hardware board** parameter
available in the **Hardware Implementation** tab of the Configuration
Parameters dialog box for the Simulink model containing this block, the block automatically sets the
**Approximation method** parameter to `TI
IQMATH`. For more information about the supported approximation methods,
see the Approximation method parameter.

### **Approximation method** — Approximation method for computing sine and cosine signals `Lookup` (default) | `None` | `CORDIC` | `TI IQMATH`

Specify the type of approximation for computing the sine and cosine output signals.
You can select one of these values.

- `None` — Select this value if you do not want to use
  any approximation.
- `CORDIC` — Select this value if you want to use the
  CORDIC approximation method.
- `Lookup` — Select this value if you want to use the
  lookup approximation method.
- `TI IQMATH` — Block selects this value if you are using
  a Texas Instruments hardware target.

#### Dependencies

You cannot manually select the value `TI IQMATH`. The
block automatically selects this value, when:

- You select any Texas Instruments hardware target in the **Hardware board** parameter
  available in the **Hardware Implementation** tab of the
  Configuration Parameters dialog box for the Simulink model containing this block.
- You select the **Optimize for selected embedded target
  hardware** parameter.

### **Theta units** — Unit of `θe` `Per-unit` (default) | `Radians` | `Degrees`

Unit of the input reference voltage position.

#### Dependencies

To enable this parameter, set the **Approximation method**
parameter to either `None` or
`Lookup`.

### **Number of data points for lookup table** — Size of lookup table array `1024` (default) | scalar

Size of the lookup table array. This parameter accepts a value between 125 and
4095.

**Note**

Based on the value you enter in this parameter, the block uses a value nearest to
`(125*n)+2`. The block performs this approximation to optimize the
computation in the hardware.

#### Dependencies

To enable this parameter, set the **Approximation method**
parameter to `Lookup`.

### **Table data type** — Data type of lookup table array `Inherit: Inherit via input` (default) | `double` | `single` | `fixdt(1,16,0)` | `<data type expression>`

Data type for the lookup table array, specified as:

- `Inherit: Inherit via input`
- `double`
- `single`
- `fixdt(1,16,0)`
- `<data type expression>`

For more information on setting data types, see Control Data Types of Signals.

#### Dependencies

To enable this parameter, set the **Approximation method**
parameter to `Lookup`.

### **Number of iterations** — Number of iterations for CORDIC algorithm `11` (default) | positive integer, less than or equal to word length of fixed-point input

Specify the number of iterations to perform the CORDIC algorithm. The default value
is 11.

- When the block input uses a floating-point data type, the number of iterations
  can be a positive integer.
- When the block input is a fixed-point data type, the number of iterations cannot
  exceed the word length.

  For example, if the block input is `fixdt(1,16,15)`, the word
  length is 16. In this case, the number of iterations cannot exceed 16.

#### Dependencies

To enable this parameter, set the **Approximation method**
parameter to `CORDIC`.

### **Theta data type** — Data type of lookup table array `fixdt([],16,0)` (default) | `double` | `single` | `<data type expression>`

Data type for the lookup table array, specified as:

- `double`
- `single`
- `fixdt([],16,0)`
- `<data type expression>`

For more information on setting data types, see Control Data Types of Signals.

#### Dependencies

To enable this parameter, configure the block to use the `TI
IQMATH` approximation method by:

- Selecting any Texas Instruments hardware target in the **Hardware board** parameter
  available in the **Hardware Implementation** tab of the
  Configuration Parameters dialog box for the Simulink model containing this block.
- Selecting the **Optimize for selected embedded target
  hardware** parameter.

## Libraries

Motor Control Blockset / Controls / Math Transforms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2024b**

## Description

Implement sine and cosine functions

The SinCos Embedded Optimized block implements sine and cosine functions
using the specified position or phase input signal.

The block supports CORDIC, TI IQMATH, and lookup-based approximation methods to compute
the sine and cosine signals. The following table lists the supported data types,
θe input units, as well as use cases for each approximation
method.

| Approximation Method | Data Types Supported | θe Input Units Supported | When to Use This Method |
| --- | --- | --- | --- |
| None | Floating point | - Per-unit (0 to 1) - Radians (0 to 2π) - Degrees (0 to 360) | You want to use the default Taylor series algorithm. |
| CORDIC | Floating point and fixed point | Radians (-π to π) | You want a fast, approximate iterative calculation. |
| Lookup | Floating point and fixed point | - Per-unit (0 to 1) - Radians (0 to 2π) - Degrees (0 to 360) | You want a fast, approximate lookup table implementation. |
| Texas Instruments® IQMATH | Fixed point  (`TI IQMATH` does not support 16-bit fixed point data type) | Per-unit (0 to 1) | You cannot manually select this value. The block automatically selects this value, when you optimize the block for a Texas Instruments hardware. |

The block enables you to automatically select an optimized approximation method for the
hardware board that you select in the **Hardware Implementation** tab of the
Configuration Parameters dialog box for the Simulink® model containing this block.

For example, the block automatically selects the Texas Instruments IQ math approximation method, if you select any Texas Instruments hardware target.

### CORDIC Approximation Method

CORDIC is an acronym for COordinate Rotation DIgital Computer. The Givens rotation-based
CORDIC algorithm is one of the most hardware-efficient algorithms available because it
requires only iterative shift-add operations. For more information, see CORDIC. The
block input has further requirements.

For more information about selecting the CORDIC approximation method, see Approximation method.

This table summarizes what happens for an invalid input.

| Block Usage | Effect of Invalid Input |
| --- | --- |
| Simulation modes | An error appears. |
| Generated code | Undefined behavior occurs. Avoid relying on undefined behavior for generated code. |

### Lookup Approximation Method

The block supports the lookup table approach. This approach results in optimized
code-execution when used with the model settings and configuration adopted by the examples
shipped in Motor Control Blockset™. You can specify the number of lookup table points in the **Number of
data points for lookup table** parameter.

This figure shows the input position along with the sine and cosine output signals that
the block generates using the lookup approximation method:

For more information about selecting the lookup approximation method, see Approximation method.
