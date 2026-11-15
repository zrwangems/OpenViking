---
type: simulink-block
title: 'BLDC Configuration'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Motor Parameter Estimation and Plant Modeling / Electrical Systems'
documentation_page: 'bldcconfiguration'
documentation_source_path: 'ref/bldcconfiguration.html'
language: en
---

# BLDC Configuration

## Ports

### Output

### **Config** — Block configuration signal vector

Configuration signal for a BLDC motor, which includes the following
parameters that you configure using this block.

| Configuration element | | | Units |
| --- | --- | --- | --- |
| Number of pole pairs | | | - |
| Stator resistance per phase | | | ohm |
| Stator d-axis inductance | | | Henries |
| Stator q-axis inductance | | | Henries |
| Permanent magnet flux linkage constant | | | Weber |
| Inertia | | | kgm^2 |
| Back electromotive force, EMF | | | Vpk\_LL/krpm  Vpk\_LL is the peak voltage line-to-line measurement |
| Viscous damping | | | N·m/(rad/s) |
| Mechanical input configuration (Torque or Speed) | | | - |

**Data Types:** `single`

## Parameters

### Block Options

### **Mechanical input configuration** — Select port configuration `Torque` (default) | `Speed`

This table summarizes the input and output ports in each port
configuration.

| Mechanical input configuration parameter value | | | LdTrq/Spd port configuration |
| --- | --- | --- | --- |
| Torque | | | **LdTrq** |
| Speed | | | **Spd** |

### **Sample Time (Ts)** — Sample time after which block executes again `1e-6` (default) | scalar

The fixed time interval (in seconds) between every two consecutive instances
of block execution.

### Parameters

### **Number of pole pairs** — Pole pairs `4` (default) | scalar

Number of pole pairs, *P*, in the motor.

### **Stator resistance per phase (Ohm)** — Resistance of stator `0.02` (default) | scalar

Stator resistance per phase, *Rs*, in ohms.

### **Stator d-axis inductance (H)** — *d*-axis inductance `1.7e-3` (default) | scalar

Stator inductance, *Ld*, in H.

### **Stator q-axis inductance (H)** — *q*-axis inductance `3.2e-3` (default) | scalar

Stator inductance, *Lq*, in H.

### **Permanent flux linkage constant (Wb)** — Flux linkage constant `0.2205` (default) | scalar

Permanent flux linkage constant, *λpm*, in Wb.

### **Inertia (kgm^2)** — Physical inertia `0.0027` (default) | scalar

Physical inertia of the motor, *J*, in
kg.m2.

### **Viscous damping (Nm/rad/s)** — Viscous damping `4.924e-4` (default) | scalar

Viscous damping of the motor, *F*, in Nm/(rad/s).

### **Static friction (Nm)** — Static friction `0` (default) | scalar

Static friction in the motor, *Tf*, in Nm.

## Libraries

Motor Control Blockset HDL Support / Electrical Systems / Motors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023b**

## Description

Configure BLDC system parameters

The BLDC Configuration block generates the configuration signal for a
brushless DC (BLDC) machine or motor. You can use this signal to update parameters of BLDC
blocks that support FPGA deployment, such as the BLDC HDL
block.
