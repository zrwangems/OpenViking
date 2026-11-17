---
type: simulink-block
title: 'Induction Motor Configuration'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Electrical Systems / Motors'
documentation_page: 'inductionmotorconfiguration'
documentation_source_path: '../mcb/ref/inductionmotorconfiguration.html'
language: en
---

# Induction Motor Configuration

## Ports
```yaml
ports:
- name: Config
  summary: Block configuration signal vector
  direction: output
  data_types: single
```

### Output

### **Config** — Block configuration signal vector

Configuration signal for induction machine or motor, which includes the following
parameters that you configure using this block.

| Configuration element | | | Units |
| --- | --- | --- | --- |
| Number of pole pairs | | | - |
| Stator resistance per phase | | | ohm |
| Stator leakage inductance | | | Henries |
| Rotor resistance | | | ohm |
| Rotor leakage inductance | | | Henries |
| Magnetizing inductance | | | Henries |
| Inertia | | | kgm^2 |
| Back electromotive force, EMF | | | Vpk\_LL/krpm  Vpk\_LL is the peak voltage line-to-line measurement |
| Viscous damping | | | N·m/(rad/s) |
| Port configuration (Torque or Speed) | | | - |

**Data Types:** `single`
## Parameters
```yaml
parameters:
- name: Port configuration
  summary: Select port configuration Torque (default) | Speed
  group: Block Options
- name: Sample Time (Ts)
  summary: Sample time after which block executes again 1e-6 (default) | scalar
  group: Block Options
- name: Number of pole pairs
  summary: Pole pairs 2 (default) | scalar
  group: Parameters
- name: Stator resistance (Ohm)
  summary: Stator resistance 1.77 (default) | scalar
  group: Parameters
- name: Leakage inductance (H)
  summary: Stator leakage inductance 0.0139 (default) | scalar
  group: Parameters
- name: Rotor resistance (Ohm)
  summary: Rotor resistance 1.34 (default) | scalar
  group: Parameters
- name: Leakage inductance (H)
  summary: Rotor leakage inductance 0.0121 (default) | scalar
  group: Parameters
- name: Magnetizing inductance (H)
  summary: Inductance 0.3876 (default) | scalar
  group: Parameters
- name: Physical Inertia (kg\*m^2)
  summary: Physical inertia 0.001 (default) | scalar
  group: Parameters
- name: Viscous damping (N\*m/rad/s)
  summary: Viscous damping 0 (default) | scalar
  group: Parameters
- name: Static friction (N\*m)
  summary: Static friction 0 (default) | scalar
  group: Parameters
```

### Block Options

### **Port configuration** — Select port configuration `Torque` (default) | `Speed`

This table summarizes the input and output ports in each
configuration.

| Mechanical input configuration parameter value | | | LdTrq/Spd port configuration |
| --- | --- | --- | --- |
| Torque | | | **LdTrq** |
| Speed | | | **Spd** |

### **Sample Time (Ts)** — Sample time after which block executes again `1e-6` (default) | scalar

The fixed time interval (in seconds) between every two consecutive instances of
block execution.

### Parameters

### **Number of pole pairs** — Pole pairs `2` (default) | scalar

Number of pole pairs, *P*, in the motor.

### **Stator resistance (Ohm)** — Stator resistance `1.77` (default) | scalar

Stator resistance, *Rs*, in ohm.

### **Leakage inductance (H)** — Stator leakage inductance `0.0139` (default) | scalar

Stator leakage inductance, *Lls*, in
H.

### **Rotor resistance (Ohm)** — Rotor resistance `1.34` (default) | scalar

Rotor resistance, *Rr*, in ohm.

### **Leakage inductance (H)** — Rotor leakage inductance `0.0121` (default) | scalar

Rotor leakage inductance, *Llr*, in
H.

### **Magnetizing inductance (H)** — Inductance `0.3876` (default) | scalar

Magnetizing inductance, *Lm*, in H.

### **Physical Inertia (kg\*m^2)** — Physical inertia `0.001` (default) | scalar

Physical inertia of the motor, *J*, in kg.m^2.

### **Viscous damping (N\*m/rad/s)** — Viscous damping `0` (default) | scalar

Viscous damping of the motor, *F*, in N·m/(rad/s).

### **Static friction (N\*m)** — Static friction `0` (default) | scalar

Static friction in the motor, *Tf*, in
N·m.
## Libraries

Motor Control Blockset HDL Support / Electrical Systems / Motors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022b**

## Description

Configure system parameters of induction motor

The Induction Motor Configuration block generates the configuration signal
for an induction machine or motor. You can use this signal to update the parameters of
induction motor blocks that support FPGA deployment, such as the Induction Motor HDL
block.
