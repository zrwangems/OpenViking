---
type: simulink-block
title: 'Machine Mechanical Power'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Mechanical'
documentation_page: 'machinemechanicalpower'
documentation_source_path: 'ref/machinemechanicalpower.html'
language: en
---

# Machine Mechanical Power

## Ports
```yaml
ports:
- name: Pm
  summary: Mechanical power physical | positive
  direction: input
- name: pu
  summary: Per-unit mechanical power physical | positive
  direction: input
- name: R
  summary: Machine rotor mechanical
  direction: conserving
- name: C
  summary: Machine case mechanical
  direction: conserving
```

### Input

### **Pm** — Mechanical power physical | positive

Physical signal input port associated with mechanical power, in
W.

#### Dependencies

This port is visible only if you set the **PS input
unit** parameter in the **Main**
setting to `SI`.

### **pu** — Per-unit mechanical power physical | positive

Physical signal input port associated with mechanical power, in
per-unit.

#### Dependencies

This port is visible only if you set the **PS input
unit** parameter in the **Main**
setting to `Per unit`.
### Conserving

### **R** — Machine rotor mechanical

Mechanical rotational conserving port associated with the machine
rotor.

### **C** — Machine case mechanical

Mechanical rotational conserving port associated with the machine
case.
## Parameters
```yaml
parameters:
- name: Input power sign convention
  summary: Type specification Generator (default) | Motor
  group: Main
- name: Rated apparent power
  summary: Rated apparent power 555e6 V*A (default)
  group: Main
- name: Rated electrical frequency
  summary: Nominal electrical frequency 60 Hz (default)
  group: Main
- name: Number of pole pairs
  summary: Number of pole pairs 1 (default)
  group: Main
- name: PS input unit
  summary: Physical signal unit system SI (default) | Per unit
  group: Main
- name: Peak torque to rated torque ratio
  summary: Peak torque to rated torque ratio 2 (default)
  group: Main
- name: Specify inertia parameterization by
  summary: Inertia parameterization Inertia constant, H (default) | Actual Inertia, J
  group: Inertia
- name: Inertia constant, H
  summary: Inertia constant 3.525 s*W/VA (default)
  group: Inertia
- name: Actual inertia, J
  summary: Actual inertia 27548 kg*m^2 (default)
  group: Inertia
- name: Specify damper parameterization by
  summary: Damping parameterization Per-unit damping coefficient, pu_D (default) | SI damping coefficient, D
  group: Inertia
- name: Per-unit damping coefficient
  summary: Per-unit damping coefficient 0.01 (default)
  group: Inertia
- name: SI damping coefficient
  summary: Damping coefficient 39.0509 Nm/(rad/s) (default)
  group: Inertia
- name: Specify initialization by
  summary: Frequency initialization Initial electrical frequency (default) | Initial mechanical frequency
  group: Initial Conditions
- name: Initial electrical frequency
  summary: Initial electrical frequency 60 Hz (default)
  group: Initial Conditions
- name: Initial mechanical frequency
  summary: Initial mechanical frequency 60 Hz (default)
  group: Initial Conditions
```

### Main

### **Input power sign convention** — Type specification `Generator` (default) | `Motor`

Machine type specification.

### **Rated apparent power** — Rated apparent power `555e6` `V*A` (default)

Rated apparent power of the connected machine.

### **Rated electrical frequency** — Nominal electrical frequency `60` `Hz` (default)

Nominal electrical frequency corresponding to the rated apparent power
of the connected machine.

### **Number of pole pairs** — Number of pole pairs `1` (default)

Number of pole pairs of the connected machine.

### **PS input unit** — Physical signal unit system `SI` (default) | `Per unit`

Unit system for physical signal input.

Select `SI` to expose the
**Pm** port or `Per unit`
to expose the **pu** port.

### **Peak torque to rated torque ratio** — Peak torque to rated torque ratio `2` (default)

Ratio that the block multiplies by the base torque to provide the
upper limit for the torque that accelerates the inertia.

### Inertia

### **Specify inertia parameterization by** — Inertia parameterization `Inertia constant, H` (default) | `Actual Inertia, J`

Inertia specification.

### **Inertia constant, H** — Inertia constant `3.525` `s*W/VA` (default)

Inertia constant.

#### Dependencies

This parameter is visible only if you set the **Specify
inertia parameterization by** parameter to
`Inertia constant, H`.

### **Actual inertia, J** — Actual inertia `27548` `kg*m^2` (default)

Total rotational mechanical inertia of machine rotor. This parameter
is visible only if you set **Specify inertia parameterization
by** to `Actual Inertia,
J`.

#### Dependencies

This parameter is visible only if you set the **Specify
inertia parameterization by** parameter to
`Actual Inertia, J`.

### **Specify damper parameterization by** — Damping parameterization `Per-unit damping coefficient, pu_D` (default) | `SI damping coefficient, D`

Damping specification.

### **Per-unit damping coefficient** — Per-unit damping coefficient `0.01` (default)

Damping coefficient in per-unit.

#### Dependencies

This parameter is visible only if you set the **Specify
damper parameterization by** parameter to
`Per-unit damping coefficient,
pu_D`.

### **SI damping coefficient** — Damping coefficient `39.0509` `Nm/(rad/s)` (default)

Damping coefficient in SI units.

#### Dependencies

This parameter is visible only if you set the **Specify
damper parameterization by** parameter to
`SI damping coefficient, D`.

### Initial Conditions

### **Specify initialization by** — Frequency initialization `Initial electrical frequency` (default) | `Initial mechanical frequency`

Frequency initialization.

### **Initial electrical frequency** — Initial electrical frequency `60` `Hz` (default)

Initial electrical frequency.

#### Dependencies

This parameter is visible only if you set the **Specify
initialization by** parameter to `Initial
electrical frequency`.

### **Initial mechanical frequency** — Initial mechanical frequency `60` `Hz` (default)

Initial mechanical frequency.

#### Dependencies

This parameter is visible only if you set the **Specify
initialization by** parameter to `Initial
mechanical frequency`.
## Libraries

Simscape / Electrical / Electromechanical / Mechanical

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2014b**

## Description

Machine mechanical power defined in the SI or per-unit system

The Machine Mechanical Power block supplies specified
power to, or draws specified power from, the machine that it connects to. It includes a
representation of machine inertia and a mechanical rotational reference. In generator
mode, the physical signal input defines the mechanical power that is input to the
machine. In motor mode, it defines the mechanical power output from the machine.

The figure shows an equivalent configuration to the per-unit variant model of the
Machine Mechanical Power block using Simscape™ mechanical rotational components.

### Electrical Defining Equations

The SI model converts the SI values that you enter in the dialog box to per-unit
values for simulation. For information on the relationship between SI and per-unit
machine parameters, see Per-Unit Conversion for Machine Parameters. For information on per-unit parameterization, see Per-Unit System of Units.

To calculate the torque that it applies to the inertia, the block divides the
power demand by the present speed. To set the peak torque limit, specify a value for
the **Peak torque to rated torque ratio** parameter. Use the
**Specify inertia parameterization by** parameter to specify
inertia, *J*, directly or indirectly, with the inertia constant for
the machine, *H*.

If you specify the inertia constant for the machine, the block calculates inertia as

J=2HSrated(2πFrated/N)2,

where:

- *J* is inertia in
  kg⋅m2.
- *H* is the inertia constant in sW/VA.
- *Srated* is the rated apparent
  power of the connected machine in VA.
- *Frated* is the rated
  electrical frequency of the connected machine in Hz.
- *N* is the number of machine pole pairs.

Damping represents viscous friction between the machine rotor and
mechanical rotational reference. Based on the value you select for the
**Specify damper parameterization by** parameter, you specify a
damping coefficient in per-unit or in SI units. If you specify the damping
coefficient in per-unit, the block calculates the damping coefficient in SI units
using these equations:

ωbase=2πFratedN,

Tbase=Sratedωbase,

Dbase=Tbaseωbase,

and

D=DpuDbase,

where:

- *ωbase* is the base mechanical
  speed in rad/s.
- *Tbase* is the base damping
  torque in Nm.
- *Dbase* is the base damping
  coefficient in Nm/(rad/s).
- *Dpu* is the damping
  coefficient in per-unit.
- *D* is the damping coefficient in SI units of
  Nm/(rad/s).
