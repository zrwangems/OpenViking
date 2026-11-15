---
type: simulink-block
title: 'Circuit Breaker'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Switches and Breakers / Switches and Breakers'
documentation_page: 'circuitbreaker'
documentation_source_path: 'ref/circuitbreaker.html'
language: en
---

# Circuit Breaker

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

### **Closed resistance** — Closed resistance `0.001` `Ohm` (default)

Resistance between ports **1** and **2**
when the breaker is closed.

### **Open conductance** — Open conductance `1e-6` `1/Ohm` (default)

Conductance between ports **1** and
**2** when the breaker is open.

### **Threshold** — Threshold voltage `0.5` `V` (default)

Threshold voltage for the control port **vT**. The block
uses the threshold voltage and the value of **vT** at the
start of the simulation to determine whether the breaker is initially open
or closed. If you set **Breaker Behavior** to
`Open when current crosses zero after vT >=
Threshold`, when the voltage rises above the threshold, the
breaker opens as its current crosses zero. If you set **Breaker
Behavior** to `Open when vT >=
Threshold`, the breaker opens as soon as the voltage rises
above the threshold. When the control port voltage falls below the
threshold, the breaker closes.

### **Breaker Behavior** — Breaker Behavior when *vT* rises above threshold `Open when current crosses zero after vT >= Threshold` (default) | `Open when vT >= Threshold`

Breaker Behavior when the value at the control port
**vT** is greater than or equal to the value of the
**Threshold** parameter. The breaker can open either as
soon as the voltage rises above the threshold, or when its current also
crosses zero.

## Libraries

Simscape / Electrical / Switches & Breakers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

## Description

Single-pole single-throw circuit breaker

The Circuit Breaker block models a single-phase circuit
breaker that uses an external signal and phase current information to break an
electrical circuit.

The table shows how the external signal **vT** and the
**Breaker Behavior** parameter control the block
behavior.

| Condition | | Block Behavior | Resistance Parameter Used |
| --- | --- | --- | --- |
| **vT** < **Threshold** | | The breaker is closed. Port **1** connects to port **2**. | **Closed Resistance** |
| **vT** ≥**Threshold** | `Open when current crosses zero after vT >= Threshold` | When the current in port **1** goes through zero, the phase disconnects from port **2**. The breaker is open. | **Open Conductance** |
| `Open when vT >= Threshold` | The breaker is open. |
