---
type: simulink-block
title: 'Fractional Clock Divider with Accumulator'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Phase-Locked Loops / Building Blocks'
documentation_page: 'fractionalclockdividerwithaccumulator'
documentation_source_path: 'ref/fractionalclockdividerwithaccumulator.html'
language: en
---

# Fractional Clock Divider with Accumulator

## Ports

### Input

### **clk in** — Input clock frequency scalar

Input clock frequency, specified as a scalar. In a PLL system, the
**clk in** port is connected to the output port of
a VCO block.

**Data Types:** `double`

### **div-by** — Ratio of output to input clock frequency fractional scalar

Ratio of output to input clock frequency, specified as a fractional
scalar.

The value at the **div-by** port is split into two
parts: the integer part (*N*) and the fractional part
(*.FF*).

**Data Types:** `double`
### Output

### **clk out** — Output clock frequency scalar

Output clock frequency, specified as a scalar. In a PLL system, the
**clk out** port is connected to the feedback input
port of a PFD block. The output at the **clk out**
port is a square pulse train of 1 V amplitude.

**Data Types:** `double`

### **state** — Missing fractional pulse storage scalar

The fractional missing pulse storage. The value of the
**state** port goes up by *F* with
each rising edge of the **clk out** value of the
previous cycle. Whenever the **state** port value goes
over `1`, the value overflows and sets the
**carry** port value to
`1`.

**Data Types:** `double`

### **carry** — Activates the pulse swallow function when state port overflows `0` (default) | `1`

Output port that activates the pulse swallow function when
**state** port overflows. The pulse removal is
analogous to dividing the input frequency by *N*+1
instead of *N*.

**Data Types:** `Boolean`

## Parameters

### **Enable increased buffer size** — Enable increased buffer size off (default) | on

Select to enable increased buffer size during simulation. This increases
the buffer size of the Logic
Decision inside the Fractional Clock Divider with
Accumulator block. By default, this option is deselected.

### **Buffer size** — Number of samples of the input buffering available during simulation `1` (default) | positive integer scalar

Number of samples of the input buffering available during simulation,
specified as a positive integer scalar. This sets the buffer size of the
Logic
Decision inside the Fractional Clock Divider with
Accumulator block.

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

Clock divider that divides frequency of input signal by fractional number

The Fractional Clock Divider with Accumulator block divides the
frequency of the input signal by a tunable fractional value
(*N*.*FF*). When compared to the Single Modulus
Prescaler block, the Fractional Clock Divider with
Accumulator block helps to achieve a narrow channel spacing that can be less
than the reference frequency of a phase-locked loop (PLL) system.
