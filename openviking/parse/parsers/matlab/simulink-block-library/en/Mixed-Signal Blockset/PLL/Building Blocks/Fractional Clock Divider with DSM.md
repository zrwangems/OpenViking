---
type: simulink-block
title: 'Fractional Clock Divider with DSM'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'PLL / Building Blocks'
documentation_page: 'fractionalclockdividerwithdsm'
documentation_source_path: 'ref/fractionalclockdividerwithdsm.html'
language: en
---

# Fractional Clock Divider with DSM

## Ports
```yaml
ports:
- name: clk in
  summary: Input clock frequency scalar
  direction: input
  data_types: double
- name: div-by
  summary: Ratio of output to input clock frequency fractional scalar
  direction: input
  data_types: double
- name: clk out
  summary: Output clock frequency scalar
  direction: output
  data_types: double
```

### Input

### **clk in** — Input clock frequency scalar

Input clock frequency that needs to be divided, specified as a
scalar. In a phase-locked loop (PLL) system, the **clk
in** port is connected to the output of a VCO block.

**Data Types:** `double`

### **div-by** — Ratio of output to input clock frequency fractional scalar

Ratio of output to input clock frequency, specified as a fractional
scalar. The value at the **div-by** port,
*N.FF*, is split into two parts: the integer part
(*N*) and the fractional part
(*.FF*).

For an *n*th-order delta sigma modulator, the value
at the **div-by** port is achieved by varying
*N* between 2n different
integer values.

**Note**

For an *n*th order delta sigma modulator, use a
value ≥ 2n at the **div-by** port.

**Data Types:** `double`
### Output

### **clk out** — Output clock frequency scalar

Output clock frequency, specified as a scalar. In a PLL system, the
**clk out** port is connected to the feedback input
port of a PFD block. The output at the **clk out**
port is a square pulse train of 1 V amplitude.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Delta Sigma Modulator order
  summary: Order of the Delta Sigma Modulator 3rd order (default) | 1st order | 2nd order | 4th order
  group: ''
- name: Enable increased buffer size
  summary: Enable increased buffer size off (default) | on
  group: ''
- name: Buffer size
  summary: Number of samples of the input buffering available during simulation 1 (default) | positive integer scalar
  group: ''
```

### **Delta Sigma Modulator order** — Order of the Delta Sigma Modulator `3rd order` (default) | `1st order` | `2nd order` | `4th order`

The order of the delta sigma modulator.

For an *n*th-order of the delta sigma modulator, the
value at the **div-by** port is achieved by varying the
*N* counter value between 2n
different values. Modulator order defines the range of values by which the
signal at the **clk in** port will be divided, providing a
division effect similar to *N.FF* value at the
**div-by** port.

#### Programmatic Use

- Use `get_param(gcb,'dsm')` to view the
  current **Delta Sigma Modulator order**.
- Use `set_param(gcb,'dsm',value)` to set
  **Delta Sigma Modulator order** to a
  specific value.

### **Enable increased buffer size** — Enable increased buffer size off (default) | on

Select to enable increased buffer size during simulation. This increases
the buffer size of the Logic
Decision inside the Fractional Clock Divider with
DSM block. By default, this option is deselected.

### **Buffer size** — Number of samples of the input buffering available during simulation `1` (default) | positive integer scalar

Number of samples of the input buffering available during simulation,
specified as a positive integer scalar. This sets the buffer size of the
Logic
Decision inside the Fractional Clock Divider with
DSM block.

Selecting different simulation solver or sampling strategies can change
the number of input samples needed to produce an accurate output sample. Set
the **Buffer size** to a large enough value so that the
input buffer contains all the input samples required.

#### Dependencies

This parameter is only available when **Enable increased
buffer size** option is selected in the Block Parameters
dialog box.

#### Programmatic Use

- Use `get_param(gcb,'NBuffer')` to view the
  current value of **Buffer size**.
- Use `set_param(gcb,'NBuffer',value)` to set
  **Buffer size** to a specific value.
## Libraries

Mixed-Signal Blockset / PLL / Building Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Delta Sigma Modulator based fractional clock divider

Using delta sigma (Δ-Σ) modulation technique, a Fractional Clock Divider with
DSM reduces the primary fractional spurs by spreading out the range over
which the **div-by** value is varied. This block allows delta sigma
modulation of up to 4th order.
