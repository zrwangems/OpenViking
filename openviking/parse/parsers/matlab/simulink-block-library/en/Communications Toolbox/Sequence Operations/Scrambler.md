---
type: simulink-block
title: 'Scrambler'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Sequence Operations'
documentation_page: 'scrambler'
documentation_source_path: 'ref/scrambler.html'
language: en
---

# Scrambler

## Ports

### Input

### **In** — Input data signal vector

Input data signal, specified as an
*N*S-by-1 vector.
*N*S represents the number
of samples in the input signal. The input values must be integers from
`0` to `Calculation
base` – `1`.

**Data Types:** `double` | `Boolean` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Rst** — Reset scrambler scalar

Reset scrambler, specified as a scalar. The scrambler is reset if a
nonzero input is applied to the port.

#### Dependencies

To enable this port, set `Initial
states source` to `Dialog
Parameter` and select `Reset on nonzero input via port`.

### **ISt** — Initial states vector

Initial states of the scrambler registers when the simulation starts,
specified as a nonnegative integer vector. The length of
**ISt** must equal the order of the `Scramble
polynomial` parameter. The vector element values must be
integers from `0` to `Calculation
base` – `1`.

#### Dependencies

To enable this port, set `Initial
states source` to `Input
port`.
### Output

### **Out** — Output scrambled data vector

Output scrambled data, returned as an
*N*S-by-1 vector.
*N*S equals the number of
samples in the input signal.

**Data Types:** `double`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Calculation base** — Calculation base `4` (default) | nonnegative integer

Calculation base used in the scrambler for modulo operations, specified as
a nonnegative integer. The input and output of this block are integers from
`0` to **Calculation base** –
`1`.

### **Scramble polynomial** — Polynomial that defines connections in scrambler `'1 + x^-1 + x^-2 + x^-4'` (default) | character vector | integer vector | binary vector

Polynomial that defines the connections in the scrambler, specified as a
character vector, integer vector, or binary vector. The **Scramble
polynomial** parameter defines if each switch in the scrambler
is on or off. Specify the polynomial as:

- A character vector, such as `'1 + x^-6 +
  x^-8'`. For more details on specifying polynomials
  in this way, see Representation of Polynomials in Communications Toolbox.
- An integer vector, such as `[0 -6 -8]`,
  listing the descrambler coefficients in order of descending
  powers of *x*-1,
  where
  *p*(*x*-1)
  = 1 +
  *p1x*-1
  +
  *p2x*-2
  + ...
- A binary vector, such as `[1 0 0 0 0 0 1 0
  1]`, listing the powers of *x*
  that appear in the polynomial that has a coefficient of 1. In
  this case, the order of the scramble polynomial is one less than
  the binary vector length.

**Example:** `'1 + x^-6 + x^-8'`, `[0 -6
-8]`, and `[1 0 0 0 0 0 1 0 1]` all represent this
polynomial:

*p*(*x*-1)
= 1 + *x*-6 +
*x*-8

### **Initial states source** — Set the source for scrambler initial states `Dialog Parameter` (default) | `Input port`

- `Dialog Parameter` – Specify
  scrambler initial states by using the `Initial
  states` parameter.
- `Input port` – Specify scrambler
  initial states by using the `ISt`
  port.

### **Initial states** — Initial states of scrambler registers `[0 1 2 3]` (default) | nonnegative integer vector

Initial states of scrambler registers when the simulation starts,
specified as a nonnegative integer vector. The length of **Initial
states** must equal the order of the `Scramble
polynomial` parameter. The vector element values must be
integers from `0` to `Calculation
base` – `1`.

#### Dependencies

This parameter is available when `Initial states
source` is set to `Dialog
Parameter`.

### **Reset on nonzero input via port** — Reset scrambler via input port off (default) | on

Select this parameter to reset the Scrambler block via
input port `Rst`.

#### Dependencies

This parameter is available when `Initial states
source` is set to `Dialog
Parameter`.

## Libraries

Communications Toolbox / Sequence Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `integer` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Scramble input signal

The Scrambler block applies multiplicative scrambling to input data.

One purpose of scrambling is to reduce the length of consecutive 0s or 1s in a
transmitted signal. Long sequences of 0s or 1s can cause transmission synchronization
problems. This schematic shows the scrambler operation. All adders perform addition
modulo *N*, where *N* is the value specified by the
`Calculation base`
parameter.

At each time step, the input causes the contents of the registers to shift
sequentially. Using the `Scramble polynomial`
parameter, you specify the on or off state for each switch in the scrambler.

To achieve repeatable initial scrambler conditions, you can use one of these optional
input ports:

- Select the `Reset on
  nonzero input via port` parameter and reset the scrambler with
  `Rst`.
- Set the `Initial states
  source` parameter to `Input port` and
  provide the initial states with `ISt`.

This block can accept input sequences that vary in length during simulation. For more
information about sequences that vary in length, see Variable-Size Signal Basics (Simulink).

**Note**

To apply additive scrambling to input data, you can use the PN Sequence Generator block and the Logical Operator (Simulink) block configured
as an XOR logical operator. For an example, see Additive Scrambling of Input Data in Simulink.
