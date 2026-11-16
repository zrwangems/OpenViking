---
type: simulink-block
title: 'Governor Type 1'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Turbine-Governors'
documentation_page: 'governortype1'
documentation_source_path: 'ref/governortype1.html'
language: en
---

# Governor Type 1

## Ports

### Input

### **speed\_pu** — Turbine speed scalar

Speed of the turbine, in per-unit representation, specified as a scalar.

**Data Types:** `single` | `double`

### **Pref** — Speed reference bias scalar

Bias to the speed load reference, specified as a scalar. Connect this
port to the **Pref** output port of a turbine load
controller block, such as the Controller LCFB1 block.

**Data Types:** `single` | `double`
### Output

### **Pmech(HP)** — High-pressure mechanical power scalar

High-pressure mechanical power, returned as a scalar.

**Data Types:** `single` | `double`

### **Pmech(LP)** — Low-pressure mechanical power scalar

Low-pressure mechanical power, returned as a scalar.

**Data Types:** `single` | `double`

## Parameters

### General

### **Speed reference (pu)** — Speed reference `1` (default) | scalar

Per-unit speed reference.

### **Initial torque (pu)** — Initial torque `0.45` (default) | scalar

Per-unit initial torque at the start of the simulation.

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

### Governor

### **Governor gain (1/droop), K (pu)** — Gain of governor `20` (default) | scalar

Per-unit gain of the governor.

### **Lag time constant, T\_1 (s)** — Governor lag time constant `0.2` (default) | scalar

Equivalent lag time constant. This parameter is associated with the block labeled
"Lead-Lag" in the diagram. Set this parameter to `0`
when the additional lag dynamics are negligible.

### **Lead time constant, T\_2 (s)** — Governor lead time constant `0` (default) | scalar

Equivalent lead time constant. This parameter is associated with the block labeled
"Lead-Lag" in the diagram. Set this parameter to `0`
when the additional lead dynamics are negligible.

### **Valve position time constant, T\_3 (s)** — Time constant of valve position `0.1` (default) | scalar

Time constant of the valve position, in seconds.

### **Maximum valve opening rate, U\_o (pu/s)** — Maximum opening rate of the valve `0.1` (default) | scalar

Per-unit maximum opening rate of the valve.

### **Maximum valve closing rate, U\_c (pu/s)** — Maximum closing rate of the valve `-0.1` (default) | scalar

Per-unit maximum closing rate of the valve.

### **Maximum valve opening, on MW capability, P\_max (pu)** — Maximum opening of the valve on MW capability `0.98` (default) | scalar

Per-unit maximum opening of the valve, on MW capability.

### **Minimum valve opening, on MW capability, P\_min (pu)** — Minimum opening of the valve, on MW capability `0` (default) | scalar

Per-unit minimum opening of the valve, on MW capability.

### **Time constant for steam inlet, T\_4 (s)** — Time constant of the inlet steam `0.25` (default) | scalar

Time constant of the inlet steam bowl, in seconds. This parameter is associated with the
block labeled "Low-Pass Filter" in the diagram.

### **HP fraction, K\_1** — Fraction of high-pressure shaft power `0.22` (default) | scalar

Fraction of the high-pressure shaft power after the first boiler
pass.

### **LP fraction, K2** — Fraction of low-pressure shaft power `0` (default) | scalar

Fraction of the low-pressure shaft power after the first boiler
pass.

### **Time constant for second boiler pass, T\_5 (s)** — Time constant for second boiler pass `4` (default) | scalar

Time constant of the second boiler pass, in seconds. This parameter is associated with
the block labeled "Low-Pass Filter1" in the diagram.

### **HP fraction, K\_3** — Fraction of high-pressure shaft power `0.22` (default) | scalar

Fraction of the high-pressure shaft power after the second boiler
pass.

### **LP fraction, K\_4** — Fraction of low-pressure shaft power `0` (default) | scalar

Fraction of the low-pressure shaft power after the second boiler
pass.

### **Time constant for third boiler pass, T\_6 (s)** — Time constant for third boiler pass `4` (default) | scalar

Time constant of the third boiler pass, in seconds. This parameter is associated with
the block labeled "Low-Pass Filter2" in the diagram.

### **HP fraction, K\_5** — Fraction of high-pressure shaft power `0.3` (default) | scalar

Fraction of the high-pressure shaft power after the third boiler
pass.

### **LP fraction, K\_6** — Fraction of low-pressure shaft power `0` (default) | scalar

Fraction of the low-pressure shaft power after the third boiler
pass.

### **Time constant for fourth boiler pass, T\_7 (s)** — Time constant for fourth boiler pass `0.4` (default) | scalar

Time constant of the fourth boiler pass, in seconds. This parameter is associated with
the block labeled "Low-Pass Filter3" in the diagram.

### **HP fraction, K\_7** — Fraction of high-pressure shaft power `0.26` (default) | scalar

Fraction of the high-pressure shaft power after the fourth boiler
pass.

### **LP fraction, K\_8** — Fraction of low-pressure shaft power `0` (default) | scalar

Fraction of the low-pressure shaft power after the fourth boiler
pass.

### **Deadband** — Deadband width `0.02` (default) | scalar

Intentional deadband width.

## Libraries

Simscape / Electrical / Control / Turbine-Governors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

IEEE type 1 linearized speed-governing steam turbine model

The Governor Type 1 block models a model IEEEG1 steam
turbine-governor model IEEEG1.

This block allows the modeling of cross-compound units and it has two sets of turbine fractions:

- **LP Fraction, K\_2**, **LP Fraction,
  K\_4**, **LP Fraction, K\_6**, **LP
  Fraction, K\_8** for low-pressure (LP).
- **HP Fraction, K\_1**, **HP Fraction,
  K\_3**, **HP Fraction, K\_5**, **HP
  Fraction, K\_7** for high-pressure (HP).

You can switch between continuous and discrete implementations of the block by using the
**Sample time (-1 for inherited)** parameter. To configure the
governor for continuous time, set the **Sample time (-1 for
inherited)** property to `0`. To configure the governor
for discrete time, set the **Sample time (-1 for inherited)** property
to a positive, nonzero value, or to `-1` to inherit the sample time
from an upstream block.

This diagram illustrates the overall structure of the block:
