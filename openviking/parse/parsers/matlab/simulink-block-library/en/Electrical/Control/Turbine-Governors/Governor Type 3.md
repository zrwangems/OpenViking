---
type: simulink-block
title: 'Governor Type 3'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Turbine-Governors'
documentation_page: 'governortype3'
documentation_source_path: 'ref/governortype3.html'
language: en
---

# Governor Type 3

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

### **Pmech** — Mechanical power scalar

Mechanical power, returned as a scalar.

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

### **Gate servomotor time constant, T\_g (s)** — Time constant for gate servomotor `0.52` (default) | scalar

Time constant for the gate servomotor, in seconds.

### **Pilot value time constant, T\_p (s)** — Time constant for pilot value `0.07` (default) | scalar

Time constant for the pilot value, in seconds. This parameter is associated with the
block labeled "Low-Pass Filter" in the diagram.

### **Opening gate rate limit, U\_o (pu/s)** — Limit of opening gate rate `0.15` (default) | scalar

Per-unit limit of the opening gate rate. This parameter is associated with the block
labeled "Low-Pass Filter" in the diagram.

### **Closing gate rate limit, U\_c (pu/s)** — Limit of closing gate rate `-0.15` (default) | scalar

Per-unit limit of the closing gate rate. This parameter is associated with the block
labeled "Low-Pass Filter" in the diagram.

### **Maximum gate position, on MVA capability, P\_max (pu)** — Maximum position of gate `0.75` (default) | scalar

Maximum per-unit position of the gate, on MVA capability.

### **Minimum gate position, on MVA capability, P\_min (pu)** — Minimum position of gate `0` (default) | scalar

Minimum per-unit position of the gate, on MVA capability.

### **Permanent speed droop coefficient, R\_perm (pu)** — Permanent speed droop coefficient `0.05` (default) | scalar

Per-unit permanent speed droop coefficient.

### **Transient speed droop coefficient, R\_temp (pu)** — Transient speed droop coefficient `0.6` (default) | scalar

Per-unit transient speed droop coefficient. This parameter is associated with the block
labeled "Filtered Derivative" in the diagram.

### **Governor time constant, T\_r (s)** — Time constant of governor `25` (default) | scalar

Time constant of the governor. This parameter is associated with the block labeled
"Filtered Derivative" in the diagram.

### **Water starting time constant, T\_w (s)** — Water starting time constant `5` (default) | scalar

Water inertia time constant. This parameter is associated with the block labeled
"Lead-Lag" in the diagram.

### **Penstock coefficient, a\_11** — Penstock dynamics coefficient `0.75` (default) | scalar

Coefficient for the penstock dynamics. This parameter is associated with the block
labeled "Lead-Lag" in the diagram.

### **Penstock coefficient, a\_13** — Penstock dynamics coefficient `0.75` (default) | scalar

Coefficient for the penstock dynamics. This parameter is associated with the block
labeled "Lead-Lag" in the diagram.

### **Penstock coefficient, a\_21** — Penstock dynamics coefficient `0.75` (default) | scalar

Coefficient for the penstock dynamics. This parameter is associated with the block
labeled "Lead-Lag" in the diagram.

### **Penstock coefficient, a\_23** — Penstock dynamics coefficient `0.75` (default) | scalar

Coefficient for the penstock dynamics. This parameter is associated with the block
labeled "Lead-Lag" in the diagram.

## Libraries

Simscape / Electrical / Control / Turbine-Governors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

IEEE type 3 linearized speed-governing hydro turbine model

The Governor Type 3 block models a model IEEEG3 hydro
turbine-governor with penstock dynamics.

This block has a more detailed governor model than the Governor Type 1
block and uses a linearized model of the turbine, or water, column model and penstock
dynamics.

You can switch between continuous and discrete implementations of the block by using the
**Sample time (-1 for inherited)** parameter. To configure the
governor for continuous time, set the **Sample time (-1 for
inherited)** property to `0`. To configure the governor
for discrete time, set the **Sample time (-1 for inherited)** property
to a positive, nonzero value, or to `-1` to inherit the sample time
from an upstream block.

This diagram illustrates the overall structure of the block:
