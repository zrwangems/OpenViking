---
type: simulink-block
title: 'Circuit Breaker (with arc)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Switches and Breakers / Switches and Breakers'
documentation_page: 'circuitbreakerwitharc'
documentation_source_path: 'ref/circuitbreakerwitharc.html'
language: en
---

# Circuit Breaker (with arc)

## Ports

### Input

### **vT** — Scalar control port physical signal

Scalar physical signal control port.

#### Dependencies

To enable this port, set **Modeling option** to
`PS control port`.
### Conserving

### **1** — Port 1 electrical

Electrical conserving port.

### **2** — Port 2 electrical

Electrical conserving port.

### **+** — Positive port electrical

Positive electrical conserving port.

#### Dependencies

To enable this port, set **Modeling option** to
`Electrical control port`.

### **-** — Negative port electrical

Negative electrical conserving port.

#### Dependencies

To enable this port, set **Modeling option** to
`Electrical control port`.

## Parameters

### **Modeling option** — Whether to specify physical or electrical control port `PS control port` (default) | `Electrical control port`

Whether to specify physical or electrical control port for the switch gate.

### **Arc time constant, tau** — Arc time constant `0.3e-6` `s` (default)

Time constant for the Mayr arc..

### **Cooling power, P** — Cooling power `30900` `W` (default)

Cooling power.

### **Initial arc conductance, g0** — Initial arc conductance `1e4` `s` (default)

Conductance between ports **1** and
**2** when the breaker is closed.

### **Threshold** — Threshold voltage `0.5` `V` (default)

Threshold voltage for the control port *vT*. The block
uses the threshold voltage and the value of *vT* at the
start of the simulation to determine whether the breaker is initially open
or closed. When the voltage rises above the threshold, the breaker opens.
When the control port voltage falls below the threshold, the breaker
closes.

## Libraries

Simscape / Electrical / Switches & Breakers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015b**

## Description

Single-pole single-throw circuit breaker with Mayr arc representation

The Circuit Breaker (with arc) block represents a
single-phase circuit breaker with Mayr arc representation controlled by an external
control signal *vT*. If *vT* is less than the
threshold, then the breaker is closed. If *vT* is greater than or equal
to the threshold, then the breaker opens with an arc during the current interruption.
The external signal can open and close the breaker repeatedly.

The table shows how the external signal *vT* controls the block
behavior.

| Condition | Block Behavior |
| --- | --- |
| *vT* < **Threshold** | The circuit breaker is closed. Port **1** is connected to port **2**. |
| *vT* ≥ **Threshold** | The circuit breaker is either opening or open. Port **1** is connected to port **2** via a nonlinear conductance. |

The Circuit Breaker (with arc) block has a higher
computational overhead than the Circuit Breaker block. If the fidelity of the representation of arc
current or voltage is your overriding requirement, use the Circuit
Breaker (with arc) block and use a global Simulink® variable-step solver. Otherwise, use the Circuit
Breaker block.

### Mayr Arc Model Equations

The defining equations for the breaker are

x=ln(g)

and

i=gv,

where:

- *g* is the arc conductance.
- *x* is an internal state variable.
- *v* is the voltage across the breaker.
- *i* is the current through the breaker.

When the breaker is closed,

dxdt=0.

When the breaker is opening or open,

dxdt=1τ(gv2P−1),

where:

- *τ* is the arc time constant.
- *P* is the cooling power.
