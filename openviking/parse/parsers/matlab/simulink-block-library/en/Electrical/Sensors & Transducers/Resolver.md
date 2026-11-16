---
type: simulink-block
title: 'Resolver'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'resolver'
documentation_source_path: 'ref/resolver.html'
language: en
---

# Resolver

## Ports

### Conserving

### **p1** — Primary winding positive terminal electrical

Electrical conserving port associated with the positive terminal of
the primary winding.

### **p2** — Primary winding negative terminal electrical

Electrical conserving port associated with the negative terminal of
the primary winding.

### **R** — Resolver rotor mechanical rotational

Mechanical rotational conserving port connected to the rotor.

### **C** — Resolver case mechanical rotational

Mechanical rotational conserving port connected to the resolver
case.

### **x1** — Secondary winding *x* positive terminal electrical

Electrical conserving port associated with the positive terminal of
secondary winding *x*.

### **x2** — Secondary winding *x* negative terminal electrical

Electrical conserving port associated with the negative terminal of
secondary winding *x*.

### **y1** — Secondary winding *y* positive terminal electrical

Electrical conserving port associated with the positive terminal of
secondary winding *y*.

### **y2** — Secondary winding *y* negative terminal electrical

Electrical conserving port associated with the negative terminal of
secondary winding *y*.

## Parameters

### **Parameterization** — Resolver parameterization `Specify transformation ratio and omit dynamics` (default) | `Specify transformation ratio and measured impedances` | `Specify equation parameters directly`

Select one of the following methods for block parameterization:

- `Specify transformation ratio and omit
  dynamics` — Provide values for transformation
  ratio, number of pole pairs, and initial rotor angle only. This
  model neglects the transformer inductive terms, and is only
  valid if the sensor is driven by a sine wave. The equations are
  based on the superposition of two ideal transformers, both with
  coupling coefficients that depend on rotor angle. For more
  information, see Equations when Omitting Dynamics.
- `Specify transformation ratio and measured
  impedances` — Provide additional values to
  determine the transformer inductive terms, to model the voltage
  amplitude loss and phase differences. This model is valid for
  any input waveform. The equations are based on the superposition
  of two mutual inductors, both with coupling coefficients that
  depend on rotor angle. For more information, see Equations when Including Dynamics.
- `Specify equation parameters
  directly` — Model the dynamics, but provide
  values for rotor and stator inductances and the peak coefficient
  of coupling, instead of transformation ratio and measured
  impedances. For more information, see Equations when Including Dynamics. This model is
  valid for any input waveform.

### **Transformation ratio** — Peak output to input voltage ratio `0.5` (default) | positive number

Ratio between the peak output voltage and the peak input voltage assuming
negligible secondary voltage drop due to resistance and inductance.

#### Dependencies

To enable this parameter, set the
**Parameterization** parameter to
`Specify transformation ratio and omit
dynamics` or `Specify transformation ratio
and measured impedances`. If you select
`Specify transformation ratio and measured
impedances` for the
**Parameterization** parameter, then the
transformation ratio takes the voltage drop due to primary winding
resistance into account.

### **Rotor resistance** — Primary resistance `70` `Ohm` (default) | positive number

Rotor ohmic resistance. This resistance is also referred to as the primary
resistance.

#### Dependencies

To enable this parameter, set the
**Parameterization** parameter to
`Specify transformation ratio and measured
impedances` or `Specify equation parameters
directly`.

### **Stator resistance** — Secondary resistance `180` `Ohm` (default) | positive number

Stator ohmic resistance. This resistance is also referred to as the
secondary resistance. It is assumed that both secondaries have the same
resistance.

#### Dependencies

To enable this parameter, set the
**Parameterization** parameter to
`Specify transformation ratio and measured
impedances` or `Specify equation parameters
directly`.

### **Rotor reactance** — Primary reactance `100` `Ohm` (default) | positive number

Rotor reactance when the secondary windings are open-circuit. This
reactance is also referred to as the primary reactance.

#### Dependencies

To enable this parameter, set the
**Parameterization** parameter to
`Specify transformation ratio and measured
impedances`.

### **Stator reactance** — Secondary reactance `300` `Ohm` (default) | positive number

Stator reactance when the primary winding is open-circuit. This reactance
is also referred to as the secondary reactance.

#### Dependencies

To enable this parameter, set the
**Parameterization** parameter to
`Specify transformation ratio and measured
impedances`.

### **Frequency at which reactances and transformation ratio are specified** — Sinusoidal source frequency `10` `kHz` (default) | positive number

Frequency of the sinusoidal source used when measuring the
reactances.

#### Dependencies

To enable this parameter, set the
**Parameterization** parameter to
`Specify transformation ratio and measured
impedances`.

### **Rotor inductance** — Primary reactance `0.0016` `H` (default) | positive number

Rotor or primary inductance,
*L*p.

#### Dependencies

To enable this parameter, set the
**Parameterization** parameter to
`Specify equation parameters
directly`.

### **Stator inductance** — Secondary reactance `0.0048` `H` (default) | positive number

Stator or secondary inductance,
*L*s.

#### Dependencies

To enable this parameter, set the
**Parameterization** parameter to
`Specify equation parameters
directly`.

### **Peak coefficient of coupling** — Maximum coupling coefficient `0.35` (default) | number between zero and one, exclusive

Peak coefficient of coupling between the primary and secondary
windings.

#### Dependencies

To enable this parameter, set the
**Parameterization** parameter to
`Specify equation parameters
directly`.

### **Number of pole pairs** — Rotor pole pairs `1` (default) | positive number

Number of pole pairs on the rotor.

## Libraries

Simscape / Electrical / Sensors & Transducers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Rotary transformer that measures angle of rotation

The Resolver block models a generic resolver, which
measures the electrical phase angle of a signal through electromagnetic coupling. The
resolver consists of a rotary transformer that couples an AC voltage applied to the
primary winding to two secondary windings. These secondary windings are physically
oriented at 90 degrees to each other. As the rotor angle changes, the relative coupling
between the primary and the two secondary windings varies. In the
Resolver block model, the first secondary winding is
oriented such that peak coupling occurs when the rotor is at zero degrees, and therefore
the second secondary winding has minimum coupling when the rotor is at zero
degrees.

Without loss of generality, it is assumed that the transformer between primary and
rotor circuit is ideal with a ratio of 1:1. This results in the rotor current and
voltage being equivalent to the primary current and voltage.

You have two options for defining the block equations:

- Omit the dynamics by neglecting the transformer inductive terms. This model is
  only valid if the sensor is driven by a sine wave because any DC component on
  the primary side will pass to the output side.
- Include the inductive terms, thereby capturing voltage amplitude loss and
  phase differences. This model is valid for any input waveform. Within this
  option, you can either specify the inductances and the peak coupling coefficient
  directly, or specify the transformation ratio and measured impedances, in which
  case the block uses these values to determine the inductive terms.

### Equations when Omitting Dynamics

The equations are based on the superposition of two ideal transformers, both with
coupling coefficients that depend on rotor angle. The two ideal transformers have a
common primary winding. See the Simscape™
Ideal Transformer block
reference page for more information on modeling ideal transformers. The equations
are:

*Kx* = *R* cos(
*N*
*Θ* )

*Ky* = *R* sin(
*N*
*Θ* )

*vx* =
*Kx*
*v*
p

*vy* =
*Ky*
*v*
p

*ip* = –
*Kx*
*ix* –
*Ky*
*iy*

where:

- *vp* and
  *ip* are the rotor (or
  equivalently primary) voltage and current, respectively.
- *vx* and
  *ix* are the first
  secondary voltage and current, respectively.
- *vy* and
  *iy* are the second
  secondary voltage and current, respectively.
- *Kx* is the coupling
  coefficient for the first secondary winding.
- *Ky* is the coupling
  coefficient for the second secondary winding.
- *R* is the transformation ratio.
- *N* is the number of pole pairs.
- *Θ* is the rotor angle.

### Equations when Including Dynamics

The equations are based on the superposition of two mutual inductors, both with
coupling coefficients that depend on rotor angle. The two mutual inductors have a
common primary winding. See the Simscape
Mutual Inductor block
reference page for more information on modeling mutual inductors. The equations
are:

vp=Rpip+Lpdipdt+LpLsk(cos(Nθ)dixdt+sin(Nθ)diydt)

vx=Rsix+Lsdixdt+LpLskcos(Nθ)dipdt

vy=Rsiy+Lsdiydt+LpLsksin(Nθ)dipdt

where:

- *vp* and
  *ip* are the rotor (or
  equivalently primary) voltage and current, respectively.
- *vx* and
  *ix* are the first secondary
  voltage and current, respectively.
- *vy* and
  *iy* are the second
  secondary voltage and current, respectively.
- *Rp* is the rotor (or primary)
  resistance.
- *Lp* is the rotor (or primary)
  inductance.
- *Rs* is the stator (or secondary)
  resistance.
- *Ls* is the stator (or secondary)
  inductance.
- *N* is the number of pole pairs.
- *k* is the coefficient of coupling.
- *Θ* is the rotor angle.

It is assumed that coupling between the two secondary windings is zero.

Datasheets typically do not quote the coefficient of coupling and inductance
parameters, but instead give the transformation ratio R and measured impedances. If
you select `Specify transformation ratio and measured
impedances` for the **Parameterization**
parameter, then the values you provide are used to determine values for the equation
coefficients, as defined above.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Use nominal values to specify the expected magnitude of a variable in a model. Using
system scaling based on nominal values increases the simulation robustness. Nominal values
can come from different sources. One of these sources is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
