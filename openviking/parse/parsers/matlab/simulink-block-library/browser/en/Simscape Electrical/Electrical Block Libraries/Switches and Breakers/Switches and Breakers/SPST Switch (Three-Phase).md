---
type: simulink-block
title: 'SPST Switch (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Switches and Breakers / Switches and Breakers'
documentation_page: 'spstswitchthreephase'
documentation_source_path: 'ref/spstswitchthreephase.html'
language: en
---

# SPST Switch (Three-Phase)

## Ports

### Input

### **vT** — Control port physical signal

Physical control port.

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

### **vT** — Control port electrical

Electrical conserving control port.

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
**~2** when the switch is closed.

### **Open conductance** — Open conductance `1e-6` `1/Ohm` (default)

Conductance between ports **~1** and
**~2** when the switch is open.

### **Threshold** — Threshold `0.5` `V` (default)

Threshold voltage for the control port **vT**. When the
voltage is above the threshold, the switch is closed.

## Libraries

Simscape / Electrical / Switches & Breakers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

## Description

Three-phase single-pole single-throw switch

The SPST Switch (Three-Phase) block models a
three-phase single-throw switch that uses an external signal to connect each phase of
port **~1** with the corresponding phase of port
**~2** via internal resistance.

The table shows how the external signal *vT* controls the block
behavior.

| Condition | Block Behavior | Resistance Parameter Used |
| --- | --- | --- |
| *vT* ≤**Threshold** | The switch is open. Each phase in the composite three-phase port **~1** connects to the corresponding phase in the port **~2** via large internal resistance. | **Open conductance** |
| *vT* >**Threshold** | The switch is closed. Each phase in the composite three-phase port **~1** connects to the corresponding phase in the port **~2** via small internal resistance. | **Closed resistance** |
