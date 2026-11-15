---
type: simulink-block
title: 'Variable-Frequency Second-Order Filter'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / General Control\u200b / Filters'
documentation_page: 'variablefrequencysecondorderfilter'
documentation_source_path: 'ref/variablefrequencysecondorderfilter.html'
language: en
---

# Variable-Frequency Second-Order Filter

## Ports

### Input

### **u** — Filter input scalar

Filter input.

**Data Types:** `single` | `double`

### **fn** — Natural frequency scalar

Natural frequency.

**Data Types:** `single` | `double`
### Output

### **y** — Filtered output scalar

Filtered output.

**Data Types:** `single` | `double`

## Parameters

### Main

### **Filter type** — Filter type `Low-pass` (default) | `High-pass` | `Band-pass` | `Band-stop`

Type of second-order filter.

### **Initial natural frequency (Hz)** — Initial natural frequency `60` (default) | positive scalar

Natural frequency, in Hz, at the start of simulation.

### Initial Conditions

### **Damping factor** — Damping factor `0.707` (default) | nonnegative scalar

Damping factor of the filter.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | `0` | positive scalar

Time between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

For inherited discrete-time operation, set this parameter to `-1`.
For discrete-time operation, set this parameter to a positive integer. For
continuous-time operation, set this parameter to `0`.

If this block is in a masked subsystem or a variant subsystem that supports switching
between continuous operation and discrete operation, promote this parameter to ensure
correct switching between the continuous and discrete implementations of the block. For
more information, see Promote Block Parameters on a Mask.

### **Initial amplitude** — Initial amplitude `0` (default) | nonnegative scalar

Amplitude at the start of simulation.

### **Initial phase (rad)** — Initial phase `0` (default) | nonnegative scalar

Phase, in rad, at the start of simulation.

### **Initial frequency (Hz)** — Initial frequency `0` (default) | scalar

Frequency, in Hz, at the start of simulation.

### **Initial bias** — Initial bias `0` (default) | nonnegative scalar

Bias at the start of simulation.

## Libraries

Simscape / Electrical / Control / General Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

## Description

Discrete-time or continuous-time variable-frequency second-order filter

The Variable-Frequency Second-Order Filter block implements four different
types of second-order filters, each with external frequency input.. Filters are useful
for attenuating noise in measurement signals.

The block provides these filter types:

- Low pass — Allows signals, f, only in the range of frequencies below the cutoff
  frequency, fc, to pass.
- High pass — Allows signals, f, only in the range of frequencies above the cutoff
  frequency, fc, to pass.
- Band pass — Allows signals, f, only in the range of frequencies between two cutoff
  frequencies, fc1 and fc2, to pass.
- Band stop — Prevents signals, f, only in the range of frequencies between two cutoff
  frequencies, fc1 and fc2, from passing.

| Filter Type | Frequency Range, f | |
| --- | --- | --- |
| **Low-Pass** |  | f<fc |
| **High-Pass** |  | f>fc |
| **Band-Pass** |  | fc1<f<fc2 |
| **Band-Stop** |  | fc1<f<fc2 |

### Equations

The second order derivative state equation for the filter is:

d2xdt2=u−2ζωndxdt−ωn2x

Where:

- *x* is the filter internal state.
- *u* is the filter input.
- *ωn* is the filter natural
  frequency.
- *ζ* is the filter damping factor.

For each filter type, the table maps the block output, y(x), as a function of the internal state of the filter, to the
*s*-domain transfer function, G(s).

| Filter Type | Output, y(x) | Transfer Function, G(s) |
| --- | --- | --- |
| **Low-Pass** | ωn2x | ωn2s2+2ζωns+ωn2 |
| **High-Pass** | d2xdt2 | s2s2+2ζωns+ωn2 |
| **Band-Pass** | 2ζωndxdt | 2ζωnss2+2ζωns+ωn2 |
| **Band-Stop** | d2xdt2+x | s2+ωn2s2+2ζωns+ωn2 |

For Initialization:

x˙(0)=dxdt|t=0

u(0)=u1(0)+u2(0)

u1(0)=A0ejφ0

u2(0)=b0ejπ2

Where:

- x(0) is the initial state of the filter.
- u(0) is the initial input to the filter.
- u1(0) is the AC component of the steady-state initial
  input.
- A0 is the initial amplitude.
- φ0 is the initial phase.
- u2(0) is the DC component of the steady-state initial
  input.
- b0 is the initial bias.

In the *s*-domain s=jω0. Therefore, for the initial frequency, ω0:

x˙(0)=Im(jω0u1(0)−ω02+jω02ζωn+ωn2).

x(0)=Im(x˙(0)ωn2jω0+u2(0))
