---
type: simulink-block
title: 'Machine Inertia'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Mechanical'
documentation_page: 'machineinertia'
documentation_source_path: 'ref/machineinertia.html'
language: en
---

# Machine Inertia

## Ports

### Conserving

### **R** — Machine rotor mechanical

Mechanical rotational conserving port associated with the machine
rotor.

## Parameters

### Main

### **Rated apparent power** — Rated apparent power `555e6` `V*A` (default)

Machine rated apparent power.

### **Rated electrical frequency** — Nominal electrical frequency `60` `Hz` (default)

Nominal electrical frequency corresponding to the machine rated
apparent power.

### **Number of pole pairs** — Number of pole pairs `1` (default)

Number of pole pairs of the connected machine.

### Inertia

### **Specify inertia parameterization by** — Inertia parameterization `Inertia constant, H` (default) | `Actual Inertia, J`

Inertia specification.

### **Inertia constant, H** — Inertia constant `3.525` `s*W/VA` (default)

Inertia constant.

#### Dependencies

To enable this parameter, set **Specify inertia
parameterization by** to `Inertia constant,
H`.

### **Actual inertia, J** — Actual inertia `27548` `kg*m^2` (default)

Total rotational mechanical inertia of machine rotor. This parameter
is visible only if you set **Specify inertia parameterization
by** to `Actual Inertia,
J`.

#### Dependencies

To enable this parameter, set **Specify inertia
parameterization by** to `Actual Inertia,
J`.

### **Specify damper parameterization by** — Damping parameterization `Per-unit damping coefficient, pu_D` (default) | `SI damping coefficient, D`

Damping specification.

### **Per-unit damping coefficient** — Per-unit damping coefficient `0.01` (default)

Damping coefficient in per-unit.

#### Dependencies

To enable this parameter, set **Specify damper
parameterization by** to `Per-unit damping
coefficient, pu_D`.

### **SI damping coefficient** — Damping coefficient `39.0509` `Nm/(rad/s)` (default)

Damping coefficient in SI units.

#### Dependencies

To enable this parameter, set **Specify damper
parameterization by** to `SI damping
coefficient, D`.

### Initial Conditions

### **Specify initialization by** — Frequency initialization `Initial electrical frequency` (default) | `Initial mechanical frequency`

Frequency initialization.

### **Initial electrical frequency** — Initial electrical frequency `60` `Hz` (default)

Initial electrical frequency, specified in SI frequency units, such as
`Hz`, `kHz`,
`MHz`, or `GHz`.

For more information about the unit of this parameter, see Units for Angular Velocity and Frequency.

#### Dependencies

To enable this parameter, set **Specify initialization
by** to `Initial electrical
frequency`.

### **Initial mechanical frequency** — Initial mechanical frequency `60` `Hz` (default)

Initial mechanical frequency, specified in SI frequency units, such as
`Hz`, `kHz`,
`MHz`, or `GHz`.

For more information about the unit of this parameter, see Units for Angular Velocity and Frequency.

#### Dependencies

To enable this parameter, set **Specify initialization
by** to `Initial mechanical
frequency`.

## Libraries

Simscape / Electrical / Electromechanical / Mechanical

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

## Description

Machine inertia parameterized using machine inertia constant or anchor inertia

The Machine Inertia block models inertia and damping
that you connect to the mechanical rotational R port of a three-phase machine. The block
has an internal connection to a mechanical rotational reference. The figure shows an
equivalent configuration to the Machine Inertia block
using Simscape™ mechanical rotational components.

Based on the value you select for the **Specify inertia parameterization
by** parameter, you specify inertia *J* directly or using
the machine inertia constant *H*.

If you specify the inertia constant, the block calculates inertia by

J=2HSrated(2πFrated/N)2,

where:

- *J* is inertia in
  kg⋅m2.
- *H* is the inertia constant in sW/VA.
- *Srated* is the machine rated
  apparent power in VA.
- *Frated* is the machine rated
  electrical frequency in Hz.
- *N* is the number of machine pole pairs.

You specify damping that represents viscous friction between the machine
rotor and mechanical rotational reference. Based on the value you select for the
**Specify damper parameterization by** parameter, you specify a
damping coefficient in SI units or in per-unit. If you specify the damping coefficient
in per-unit, the block calculates the damping coefficient in SI units by

ωbase=2πFratedN,

Tbase=Sratedωbase,

Dbase=Tbaseωbase,

and

D=DpuDbase,

where:

- *ωbase* is the base mechanical
  angular speed in rad/s.
- *Tbase* is the base damping torque
  in Nm.
- *Dbase* is the base damping
  coefficient in Nm/(rad/s).
- *Dpu* is the damping coefficient
  in per-unit.
- *D* is the damping coefficient in SI units of
  Nm/(rad/s).

### Display Option

You can display machine parameters using the **Electrical**
menu on the block context menu.

Right-click the block and, from the **Electrical** menu, select **Display Parameters** to display the
machine per-unit base values and inertia parameters in the MATLAB® Command Window.
