---
type: simulink-block
title: 'Controller LCFB1'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Turbine-Governors\u200b'
documentation_page: 'controllerlcfb1'
documentation_source_path: 'ref/controllerlcfb1.html'
language: en
---

# Controller LCFB1

## Ports

### Input

### **speed\_pu** — Speed load scalar

Speed load, specified as a scalar.

**Data Types:** `single` | `double`

### **Pmwset** — Power setpoint scalar

Power setpoint value, specified as a scalar.

**Data Types:** `single` | `double`

### **Pelec** — Electrical power input scalar

Electrical power input, specified as a scalar.

**Data Types:** `single` | `double`
### Output

### **Pref** — Bias scalar

Bias to apply to a turbine-governor speed load reference, returned as
a scalar.

**Data Types:** `single` | `double`

## Parameters

### **Speed reference (pu)** — Speed reference `1` (default) | scalar

Per-unit speed reference.

### **Initial power reference, P\_ref0 (pu)** — Initial power reference `0.45` (default) | scalar

Per-unit power reference at the start of the simulation.

### **Controller deadband (pu)** — Deadband of controller `0` (default) | scalar

Per-unit deadband of the controller.

### **Maximum error, e\_max (pu)** — Maximum error `0.1` (default) | scalar

Maximum possible error.

### **Frequency bias gain, f\_b (pu)** — Gain of frequency bias `0` (default) | scalar

Per-unit gain of the frequency bias.

### **Proportional gain, K\_p (pu)** — Proportional gain for PI control `0` (default) | scalar

Per-unit proportional gain for PI control.

### **Integral gain, K\_i (pu/s)** — Integral gain for PI control `0.1` (default) | scalar

Per-unit integral gain for PI control.

### **Power transducer time constant, T\_pelec (s)** — Time constant of power transducer `3.5` (default) | scalar

Time constant of the power transducer, in seconds. The power transducer is represented by
the block labeled "Low-Pass Filter" in the diagram.

### **Maximum output, I\_rmax (pu)** — Upper limit of the output `0.035` (default) | scalar

Per-unit upper saturation limit for the output.

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

## Libraries

Simscape / Electrical / Control / Turbine-Governors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020a**

## Description

Load controller for turbine-governor model

The Controller LCFB1 block models a model LCFB1 turbine load
controller. You can use this load controller with any turbine-governor model, such as
the Governor Type 1
or Governor Type 3
blocks.

You can switch between continuous and discrete implementations of the block by using the
**Sample time (-1 for inherited)** parameter. To configure the
controller for continuous time, set the **Sample time (-1 for
inherited)** property to `0`. To configure the controller
for discrete time, set the **Sample time (-1 for inherited)** property
to a positive, nonzero value, or to `-1` to inherit the sample time
from an upstream block.

This diagram illustrates the overall structure of the block:
