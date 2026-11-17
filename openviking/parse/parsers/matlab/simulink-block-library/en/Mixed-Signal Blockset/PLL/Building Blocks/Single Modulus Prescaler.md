---
type: simulink-block
title: 'Single Modulus Prescaler'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'PLL / Building Blocks'
documentation_page: 'singlemodulusprescaler'
documentation_source_path: 'ref/singlemodulusprescaler.html'
language: en
---

# Single Modulus Prescaler

## Ports
```yaml
ports:
- name: clk in
  summary: Input clock frequency scalar
  direction: input
  data_types: double
- name: div-by
  summary: Ratio of output to input clock frequency scalar integer
  direction: input
  data_types: double
- name: clk out
  summary: Output clock frequency scalar
  direction: output
  data_types: double
```

### Input

### **clk in** — Input clock frequency scalar

Input clock frequency, specified as a scalar. In a PLL system, the
**clk in** port is connected to the output port of
a VCO block.

**Data Types:** `double`

### **div-by** — Ratio of output to input clock frequency scalar integer

Ratio of output to input clock frequency, expressed as a scalar
integer.

**Data Types:** `double`
### Output

### **clk out** — Output clock frequency scalar

Output clock frequency, expressed as a scalar. In a PLL system, the
**clk out** port is connected to the feedback input
port of a PFD block. The output at the **clk out**
port is a square pulse train of 1 V amplitude.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Enable increased buffer size
  summary: Enable increased buffer size off (default) | on
  group: ''
- name: Buffer size
  summary: Number of samples of the input buffering available during simulation 1 (default) | positive integer scalar
  group: ''
```

### **Enable increased buffer size** — Enable increased buffer size off (default) | on

Select to enable increased buffer size during simulation. This increases
the buffer size of the Logic
Decision inside the Single Modulus Prescaler
block. By default, this option is deselected.

### **Buffer size** — Number of samples of the input buffering available during simulation `1` (default) | positive integer scalar

Number of samples of the input buffering available during simulation,
specified as a positive integer scalar. This sets the buffer size of the
Logic
Decision inside the Single Modulus Prescaler
block.

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

Integer clock divider that divides frequency of input signal

The Single Modulus Prescaler subsystem block divides the frequency of
the input signal by a tunable integer value, *N*, passed to the
**div-by** port. In frequency synthesizer circuits, such as a
phase-locked loop (PLL) system, these prescalers divide the VCO output
frequency by an integer value. The resulting lower frequency at the prescaler output
port is comparable to the reference input at the PFD block. The Single Modulus Prescaler
is also termed as integer clock divider.
