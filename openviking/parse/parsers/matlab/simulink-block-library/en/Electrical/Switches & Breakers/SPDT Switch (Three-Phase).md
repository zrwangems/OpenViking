---
type: simulink-block
title: 'SPDT Switch (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Switches & Breakers'
documentation_page: 'spdtswitchthreephase'
documentation_source_path: 'ref/spdtswitchthreephase.html'
language: en
---

# SPDT Switch (Three-Phase)

## Ports
```yaml
ports:
- name: vT
  summary: Control port physical signal
  direction: input
- name: ~1
  summary: Expandable three-phase port electrical
  direction: conserving
- name: ~2
  summary: Expandable three-phase port electrical
  direction: conserving
- name: ~3
  summary: Expandable three-phase port electrical
  direction: conserving
- name: vT
  summary: Control port electrical
  direction: conserving
```

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

### **~3** — Expandable three-phase port electrical

Expandable three-phase electrical conserving port.

### **vT** — Control port electrical

Electrical conserving control port.

#### Dependencies

To enable this port, set **Modeling option** to
`Expanded three-phase ports| Electrical control
port` or `Composite three-phase ports|
Electrical control port`.
## Parameters
```yaml
parameters:
- name: Modeling option
  summary: Connection and gate control ports Composite three-phase ports | PS control port (default) | Composite three-phase
    ports| Electrical control port | Expanded three-phase ports | PS control port | Expanded three-phase ports| Electrical
    control port
  group: ''
- name: Closed resistance
  summary: Closed resistance 0.001 Ohm (default)
  group: ''
- name: Open conductance
  summary: Open conductance 1e-6 1/Ohm (default)
  group: ''
- name: Threshold
  summary: Threshold 0.5 V (default)
  group: ''
```

### **Modeling option** — Connection and gate control ports `Composite three-phase ports | PS control port` (default) | `Composite three-phase ports| Electrical control port` | `Expanded three-phase ports | PS control port` | `Expanded three-phase ports| Electrical control port`

Whether to model composite or expanded three-phase ports and physical signal or electrical control ports.

### **Closed resistance** — Closed resistance `0.001` `Ohm` (default)

Resistance between ports **~1** and
**~3** when the switch is closed.

### **Open conductance** — Open conductance `1e-6` `1/Ohm` (default)

Conductance between ports **~1** and
**~2** when the switch is open.

### **Threshold** — Threshold `0.5` `V` (default)

Threshold voltage for the control port *vT*. When the
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

Three-phase single-pole double-throw switch

The SPDT Switch (Three-Phase) block models a
three-phase single-pole double-throw switch that uses an external signal to connect each
phase of the port **~1** with the corresponding phase of either port
**~2** or **~3**.

The table shows how the external signal *vT* controls the block
behavior.

| Condition | Block Behavior | Resistance Parameter Used |
| --- | --- | --- |
| *vT* ≤ **Threshold** | Each phase of port **~1** is connected to the corresponding phase of port **~2** via internal resistance. Port **~3** is unconnected. | **Open conductance** (port **~1** to port **~3**). **Closed resistance** (port **~1** to port **~2**) |
| *vT* > **Threshold** | Each phase of port **~1** is connected to the corresponding phase of port **~3** via internal resistance. Port **~2** is unconnected. | **Open conductance** (port **~1** to port **~2**). **Closed resistance** (port **~1** to port **~3**) |
