---
type: simulink-block
title: 'SPST Switch'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Switches & Breakers'
documentation_page: 'spstswitch'
documentation_source_path: 'ref/spstswitch.html'
language: en
---

# SPST Switch

## Ports

### Input

### **vT** — Switch control port physical signal

Physical port associated with the signal that
opens and closes the switch.

#### Dependencies

To enable this port, set **Modeling
option** to `PS control
port`.
### Conserving

### **p** — Electrical port electrical

Electrical conserving port.

### **n** — Electrical port electrical

Electrical conserving port.

### **+** — Electrical port electrical

Electrical conserving port for the positive
voltage associated with opening and closing the
switch.

#### Dependencies

To enable this port, set **Modeling
option** to `Electrical
control port`.

### **-** — Electrical port electrical

Electrical conserving port for the negative
voltage associated with opening and closing the
switch.

#### Dependencies

To enable this port, set **Modeling
option** to `Electrical
control port`.

## Parameters

### **Modeling option** — Whether to specify physical or electrical control port `PS control port` (default) | `Electrical control port`

Whether to specify physical or electrical control port for the switch gate.

### Main

### **Closed resistance** — Closed resistance `0.01` `Ohm` (default) | positive scalar

Resistance between the **p**
port and **n** when the switch is
closed. The value must be greater than
zero.

### **Open conductance** — Open conductance `1e-6` `S` (default) | positive scalar

Conductance between the **p**
port and **n** when the switch is
open. The value must be greater than zero.

### **Threshold** — Threshold voltage `0.5` `V` (default)

The threshold voltage above which the switch
will turn on.

### **Threshold width** — Threshold width `0` `V` (default)

The minimum voltage increase above the
threshold value that will move the switch from
fully open to fully closed.

### Dynamics

### **Model dynamics** — Model dynamics `No dynamics` (default) | `Model turn-on and turn-off times`

Select whether the block models a switching delay:

- `No dynamics`
  — Do not model the delay. This is the
  default option.
- `Model turn-on and turn-off
  times` — Use additional
  parameters to model a delay between the point at
  which the voltage at **vT** or
  **+** and **-**
  passes the threshold and the switch opening or
  closing.

### **Turn-on delay** — Turn-on delay `1e-3` (default) | positive scalar

Time between the input voltage exceeding the
threshold voltage and the switch closing. The
value must be greater than zero.

#### Dependencies

This parameter is visible only when you
select `Model turn-on and turn-off
times` for the **Model
dynamics** parameter.

### **Turn-off delay** — Turn-off delay `1e-3` (default) | positive scalar

Time between the input voltage falling below
the threshold voltage and the switch opening. The
value must be greater than zero.

#### Dependencies

This parameter is visible only when you
select `Model turn-on and turn-off
times` for the **Model
dynamics** parameter.

### **Initial input value, vT** — Initial input value, *vT* `0` (default)

The value of the physical signal input
*vT* at time zero. This value is
used to initialize the delayed control voltage
parameter internally.

#### Dependencies

This parameter is visible only when you
select `Model turn-on and turn-off
times` for the **Model
dynamics** parameter.

## Libraries

Simscape / Electrical / Switches & Breakers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012b**

## Description

Single-pole single-throw switch

The SPST Switch block models a single-pole
single-throw switch:

- When the switch is open, port **p**
  is connected to port **n** through
  a resistance with value equal to the reciprocal of
  the **Open conductance** parameter
  value.
- When the switch is closed, port **p**
  is connected to port **n** through
  a resistance with value equal to the
  **Closed resistance** parameter
  value.

If the **Threshold width** parameter is
set to zero, the switch is closed if the voltage presented at the
**vT** control port exceeds the value of the
**Threshold** parameter.

If the **Threshold width** parameter is greater
than zero, then switch conductance *G* varies smoothly
between off-state and on-state values:

G=xRclosed+(1−x)Gopen

λ=vT−ThresholdThreshold width

x={0for λ≤03λ2−2λ3for 0<λ<11for λ≥1

The block uses the function 3*λ*2 –
2*λ*3 because its
derivative is zero for *λ* =
0 and *λ* =
1.

Defining a small positive **Threshold width** can help solver convergence in
some models, particularly if the control port signal *vT* varies
continuously as a function of other network variables. However, defining a nonzero threshold
width precludes the solver making use of switched linear optimizations. Therefore, if the
rest of your network is switched linear, set **Threshold width** to
zero.

Optionally, you can add a delay between the point at which the voltage at
**vT** passes the threshold and the switch opening
or closing. To enable the delay, on the **Dynamics** tab,
set the **Model dynamics** parameter to `Model
turn-on and turn-off times`.

### Model Gate Control Port

You can control the switch gates by using a physical signal port or electrical conserving
ports. To select the gate control port, set the **Modeling option**
parameter to either:

- `PS control port` — The block contains a physical
  signal port that is associated with the threshold voltage.
- `Electrical control port` — The block contains
  electrical conserving ports that are associated with the threshold
  voltage.
