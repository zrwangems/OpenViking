---
type: simulink-block
title: 'SPMT Switch'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Switches & Breakers'
documentation_page: 'spmtswitch'
documentation_source_path: 'ref/spmtswitch.html'
language: en
---

# SPMT Switch

## Ports

### Input

### **vT** — Switch control port physical signal

Signal that opens and closes the switch, specified as a physical signal.
### Conserving

### **p** — Common port electrical

Electrical conserving port associated with the common pole.

### **n1** — Throw port 1 electrical

Electrical conserving port associated with the first throw.

### **n2** — Throw port 2 electrical

Electrical conserving port associated with the second throw.

### **n3** — Throw port 3 electrical

Electrical conserving port associated with the third throw.

### **n4** — Throw port 4 electrical

Electrical conserving port associated with the fourth throw.

#### Dependencies

To enable this port, set **Number of throw ports** to
`4`, `5`,
`6`, `7`, or
`8`.

### **n5** — Throw port 5 electrical

Electrical conserving port associated with the fifth throw.

#### Dependencies

To enable this port, set **Number of throw
ports** to `5`,
`6`, `7`, or
`8`.

### **n6** — Throw port 6 electrical

Electrical conserving port associated with the sixth throw.

#### Dependencies

To enable this port, set **Number of throw
ports** to `6`,
`7`, or
`8`.

### **n7** — Throw port 7 electrical

Electrical conserving port associated with the seventh throw.

#### Dependencies

To enable this port, set **Number of throw
ports** to `7` or
`8`.

### **n8** — Throw port 8 electrical

Electrical conserving port associated with the eighth throw.

#### Dependencies

To enable this port, set **Number of throw
ports** to `8`.

## Parameters

### Main

### **Number of throw ports** — Number of throw ports `4` (default) | `3` | `5` | `6` | `7` | `8`

Number of throw connections.

### **Closed resistance** — Closed resistance `0.01` `Ohm` (default) | positive scalar

Resistance between the **p** port and the throw
ports when the switch is closed. The value must be greater than
zero.

### **Open conductance** — Open conductance `1e-6` `S` (default) | positive scalar

Conductance between the **p** port and the throw
ports when the switch is open. The value must be greater than
zero.

### Faults

### **Stuck throw fault** — Option to add stuck throw fault `Add fault` (default)

Option to add a stuck throw fault in the SPMT Switch block.

To add a fault, click the **Add fault**
hyperlink.

### **Trigger fault at time** — Time before entering faulted state `0` `s` (default) | nonnegative scalar

Simulation time at which the block enters the faulted state.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Timed`.

### **Maximum permissible common port current** — Maximum permissible common port current `inf` `A` (default) | positive scalar

Maximum current that is permitted to flow through the common port, above which a fault
may be triggered.

To enable this parameter, set **Trigger Type** to
`Behavioral`.

### **Time to fail when exceeding current** — Time to fail when exceeding current `1` `s` (default) | positive scalar

Amount of time that the common port current must continuously exceed
the maximum permissible current before a behavioral fault is
triggered.

To enable this parameter, set **Trigger Type** to
`Behavioral`.

## Libraries

Simscape / Electrical / Switches & Breakers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Single-pole multiple-throw switch

The SPMT Switch block models a single-pole multiple-throw
switch. You can specify three to eight throw connections by setting the **Number
of throw ports** parameter to the desired amount. If you only need one or
two throw ports, see the SPST Switch and SPDT Switch
blocks.

The switch control port physical signal, **vT**, specifies which
throw port connects to the pole:

- When **vT** is in the `[-inf, 1.5]`
  range, the pole always connects to throw port 1,
  **n1**.
- When **vT** is between one and the number of throw ports,
  the signal value is rounded to the nearest integer. The pole then connects
  to the throw port that corresponds to the integer value.
- When **vT** is higher than the number of throw ports, the
  pole always connects to the last throw port.

Open connections are modeled by a resistor with a value equal to the reciprocal of the
**Open conductance** parameter value. Closed connections are
modeled by a resistor with a value equal to the **Closed resistance**
parameter value.

### Faults

To model a fault in the SPMT Switch block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.
