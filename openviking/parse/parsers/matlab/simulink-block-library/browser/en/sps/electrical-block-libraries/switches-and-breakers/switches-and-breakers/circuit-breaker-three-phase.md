---
type: simulink-block
title: 'Circuit Breaker (Three Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Switches and Breakers / Switches and Breakers'
documentation_page: 'circuitbreakerthreephase'
documentation_source_path: 'ref/circuitbreakerthreephase.html'
language: en
---

# Circuit Breaker (Three Phase)

## Ports

### Input

### **vT** — Scalar control port physical signal

Scalar physical signal control port.

#### Dependencies

To enable this port, set **Modeling option** to
`Expanded three-phase ports | PS control
port` or `Composite three-phase ports |
PS control port`.
### Conserving

### **~1** — Expandable three-phase port electrical

Expandable three-phase electrical conserving port.

### **~2** — Expandable three-phase port electrical

Expandable three-phase electrical conserving port.

### **+** — Positive port electrical

Positive electrical conserving port.

#### Dependencies

To enable this port, set **Modeling option** to
`Expanded three-phase ports| Electrical control
port` or `Composite three-phase ports|
Electrical control port`.

### **-** — Negative port electrical

Negative electrical conserving port.

#### Dependencies

To enable this port, set **Modeling option** to
`Expanded three-phase ports| Electrical control
port` or `Composite three-phase ports|
Electrical control port`.

## Parameters

### **Modeling option** — Connection and gate control ports `Composite three-phase ports | PS control port` (default) | `Composite three-phase ports| Electrical control port` | `Expanded three-phase ports | PS control port` | `Expanded three-phase ports| Electrical control port`

Whether to model composite or expanded three-phase ports and physical signal or electrical control ports.

### **Closed resistance** — Closed resistance `0.001` `Ohm` (default)

Resistance between ports **~1** and
**~2** when the breaker is closed.

### **Open conductance** — Open conductance `1e-6` `1/Ohm` (default)

Conductance between ports **~1** and
**~2** when the breaker is open.

### **Threshold** — Threshold voltage `0.5` `V` (default)

Threshold voltage for the control port **vT**. The block
uses the threshold voltage and the value of **vT** at the
start of the simulation to determine whether the breaker is initially open
or closed. If you set **Breaker Behavior** to
`Open when current crosses zero after vT >=
Threshold`, when the voltage rises above the threshold, the
breaker opens each phase as its current crosses zero. If you set
**Breaker Behavior** to `Open when vT >=
Threshold`, the breaker opens each phase as soon as the
voltage rises above the threshold. When the control port voltage falls below
the threshold, the breaker closes.

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

Three-phase circuit breaker controlled by external signal

The Circuit Breaker (Three-Phase) block models a
three-phase circuit breaker that uses an external signal and phase current information
to break an electrical circuit.

The table shows how the external signal **vT** and the
**Breaker Behavior** parameter control the block
behavior.

| Condition | | Block Behavior | Resistance Parameter Used |
| --- | --- | --- | --- |
| **vT** < **Threshold** | | The breaker is closed. Each phase in the composite three-phase port **~1** connects to the corresponding phase in the port **~2**. | **Closed Resistance** |
| **vT** ≥**Threshold** | `Open when current crosses zero after vT >= Threshold` | When the current in any phase of the composite port **~1** crosses zero, the phase disconnects from the corresponding phase at port **~2**. The breaker is open. | **Open Conductance** |
| `Open when vT >= Threshold` | The breaker is open. |
