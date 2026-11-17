---
type: simulink-block
title: 'PMSM (DQ0)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Permanent Magnet'
documentation_page: 'pmsmdq0'
documentation_source_path: 'ref/pmsmdq0.html'
language: en
---

# PMSM (DQ0)

## Ports
```yaml
ports:
- name: d
  summary: '*d*-axis component electrical'
  direction: conserving
- name: q
  summary: '*q*-axis component electrical'
  direction: conserving
- name: '0'
  summary: Zero-sequence component electrical
  direction: conserving
- name: R
  summary: Motor rotor mechanical
  direction: conserving
- name: C
  summary: Motor case mechanical
  direction: conserving
- name: HR
  summary: Rotor thermal port thermal
  direction: conserving
- name: HS
  summary: Stator windings thermal port thermal
  direction: conserving
```

### Conserving

### **d** — *d*-axis component electrical

Electrical conserving port associated with the *d*-axis
component.

### **q** — *q*-axis component electrical

Electrical conserving port associated with the *q*-axis
component.

### **0** — Zero-sequence component electrical

Electrical conserving port associated with the zero-sequence component.

#### Dependencies

To enable this port, set **Zero sequence** to
`Include`.

### **R** — Motor rotor mechanical

Mechanical rotational conserving port associated with the motor rotor.

### **C** — Motor case mechanical

Mechanical rotational conserving port associated with the motor case.

### **HR** — Rotor thermal port thermal

Thermal conserving port associated with the rotor.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **HS** — Stator windings thermal port thermal

Thermal conserving port associated with the stator windings.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.
## Parameters
```yaml
parameters:
- name: Modeling option
  summary: Whether to enable thermal ports No thermal port (default) | Show thermal port
  group: ''
- name: Modeling fidelity
  summary: Modeling fidelity Constant Ld, Lq and PM (default) | Tabulated Ld, Lq and PM
  group: Main
- name: Number of pole pairs
  summary: Number of permanent magnet pole pairs on rotor 6 (default) | positive scalar
  group: Main
- name: Permanent magnet flux linkage parameterization
  summary: Parameterization option for permanent magnet flux linkage Specify flux linkage (default) | Specify torque constant
    | Specify back EMF constant
  group: Main
- name: Permanent magnet flux linkage
  summary: Permanent magnet flux linkage 0.03 Wb (default)
  group: Main
- name: Torque constant
  summary: Torque constant 0.18 N*m/A (default)
  group: Main
- name: Back EMF constant
  summary: Back EMF constant 0.18 V*s/rad (default)
  group: Main
- name: Stator parameterization
  summary: Parameterization option for stator Specify Ld, Lq, and L0 (default) | Specify Ls, Lm, and Ms
  group: Main
- name: Stator d-axis inductance, Ld
  summary: Stator *d*-axis inductance 0.00022 H (default)
  group: Main
- name: Stator q-axis inductance, Lq
  summary: Stator *q*-axis inductance 0.00022 H (default)
  group: Main
- name: Direct-axis current vector, iD
  summary: Direct-axis current vector [-200, 0, 200] A (default) | vector of two or more values
  group: Main
- name: Quadrature-axis current vector, iQ
  summary: Quadrature-axis current vector [-200, 0, 200] A (default) | vector of two or more values
  group: Main
- name: Ld matrix, Ld(id,iq)
  summary: Ld matrix 0.0002 * ones(3, 3) H (default) | matrix of scalars
  group: Main
- name: Lq matrix, Lq(id,iq)
  summary: Lq matrix 0.0002 * ones(3, 3) H (default) | matrix of scalars
  group: Main
- name: Permanent magnet flux linkage, PM(id,iq)
  summary: Flux linkage of permanent magnet 0.1 * ones(3, 3) Wb (default) | matrix of scalars
  group: Main
- name: Torque constant matrix, kt(id,iq)
  summary: Torque constant matrix 0.18 * ones(3, 3) N*m/A (default) | matrix of scalars
  group: Main
- name: Back EMF constant matrix, ke(id,iq)
  summary: Permanent magnet flux linkage 0.18 * ones(3, 3) V/(rad/s) (default) | matrix of scalars
  group: Main
- name: Stator zero-sequence inductance, L0
  summary: Stator zero-sequence inductance 0.00016 H (default) | positive scalar
  group: Main
- name: Stator self-inductance per phase, Ls
  summary: Stator self-inductance per phase 0.0002 H (default) | positive scalar
  group: Main
- name: Stator inductance fluctuation, Lm
  summary: Stator inductance fluctuation -0.0002 H (default) | scalar
  group: Main
- name: Stator mutual inductance, Ms
  summary: Average mutual inductance between stator windings 0.00002 H (default) | scalar
  group: Main
- name: Stator resistance per phase, Rs
  summary: Resistance of each of stator windings 0.013 Ohm (default) | positive scalar
  group: Main
- name: Zero sequence
  summary: Option to include or exclude zero-sequence terms Include (default) | Exclude
  group: Main
- name: Model
  summary: Option to enable iron losses computation None (default) | Empirical
  group: Iron Losses
- name: Open-circuit iron losses, [P_hysteresis P_eddy P_excess]
  summary: Open-circuit iron losses due to hysteresis, eddy, and excess losses [0, 0, 0] W (default) | row vector of three
    nonnegative elements
  group: Iron Losses
- name: Short-circuit iron losses, [P_hysteresis P_eddy P_excess]
  summary: Short-circuit iron losses [0, 0, 0] W (default) | row vector of three nonnegative elements
  group: Iron Losses
- name: Electrical frequency at which losses determined
  summary: Electrical frequency at which losses are determined 60 Hz (default) | positive scalar
  group: Iron Losses
- name: Short-circuit RMS current for short-circuit iron losses
  summary: Short-circuit RMS current for short-circuit iron losses 95 A (default) | positive scalar
  group: Iron Losses
- name: Rotor inertia
  summary: Rotor inertia 0.01 kg*m^2 (default) | nonnegative scalar
  group: Mechanical
- name: Rotor damping
  summary: Rotary damping 0 N*m/(rad/s) (default) | nonnegative scalar
  group: Mechanical
- name: Measurement temperature
  summary: Temperature at which block quotes motor parameters 298.15 K (default) | positive scalar
  group: Temperature Dependence
- name: Resistance temperature coefficient
  summary: Resistance temperature coefficient 3.93e-3 1/K (default) | nonnegative scalar
  group: Temperature Dependence
- name: Permanent magnet flux temperature coefficient
  summary: Fractional rate at which permanent magnet flux density changes with temperature -0.001 1/K (default) | nonpositive
    scalar
  group: Temperature Dependence
- name: Thermal mass for each stator winding
  summary: Thermal mass for each stator winding 100 J/K (default) | positive scalar
  group: Thermal Port
- name: Rotor thermal mass
  summary: Thermal mass of rotor 200 J/K (default) | positive scalar
  group: Thermal Port
- name: Percentage of main flux path iron losses associated with the rotor
  summary: Percentage of iron losses on main flux path associated with rotor 90 (default) | positive scalar
  group: Thermal Port
- name: Percentage of cross-tooth flux path iron losses associated with the rotor
  summary: Percentage of iron losses on cross-tooth flux path associated with rotor 30 (default) | positive scalar
  group: Thermal Port
```

### **Modeling option** — Whether to enable thermal ports `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal ports of the block and model the effects of losses that
convert power to heat.

### Main

### **Modeling fidelity** — Modeling fidelity `Constant Ld, Lq and PM` (default) | `Tabulated Ld, Lq and PM`

Select the modeling fidelity of the block:

- `Constant Ld, Lq and PM` — *Ld*,
  *Lq*, and *PM* values are constant. The
  respective parameters define their values.
- `Tabulated Ld, Lq and PM` — The block computes
  *Ld*, *Lq*, and *PM* online
  from the DQ currents lookup tables by using these equations:

  Ld=f1(id,iq)

  Ld=f2(id,iq)

  λPM=f2(id,iq)

#### Dependencies

To enable this parameter, set **Stator parameterization** to
`Specify Ld, Lq, and L0`.

### **Number of pole pairs** — Number of permanent magnet pole pairs on rotor `6` (default) | positive scalar

Number of permanent magnet pole pairs on the rotor.

### **Permanent magnet flux linkage parameterization** — Parameterization option for permanent magnet flux linkage `Specify flux linkage` (default) | `Specify torque constant` | `Specify back EMF constant`

Parameterization option for the flux linkage of the permanent magnet.

### **Permanent magnet flux linkage** — Permanent magnet flux linkage `0.03` `Wb` (default)

Peak permanent magnet flux linkage with any of the stator windings.

#### Dependencies

To enable this parameter, set **Permanent magnet flux linkage
parameterization** to `Specify flux linkage` and
**Modeling fidelity** to `Constant Ld, Lq and
PM`.

### **Torque constant** — Torque constant `0.18` `N*m/A` (default)

Torque constant with any of the stator windings.

#### Dependencies

To enable this parameter, set **Permanent magnet flux linkage
parameterization** to `Specify torque constant`
and **Modeling fidelity** to `Constant Ld, Lq and
PM`.

### **Back EMF constant** — Back EMF constant `0.18` `V*s/rad` (default)

Back EMF constant with any of the stator windings.

**Note**

The back EMF constant is the peak voltage that the permanent magnet induces in
the per-unit rotational speed of each of the phases.

#### Dependencies

To enable this parameter, set **Permanent magnet flux linkage
parameterization** to `Specify back EMF
constant` and **Modeling fidelity** to
`Constant Ld, Lq and PM`.

### **Stator parameterization** — Parameterization option for stator `Specify Ld, Lq, and L0` (default) | `Specify Ls, Lm, and Ms`

Parameterization option for the stator.

### **Stator d-axis inductance, Ld** — Stator *d*-axis inductance `0.00022` `H` (default)

*d*-axis inductance of the stator.

#### Dependencies

To enable this parameter, set **Stator parameterization** to
`Specify Ld, Lq, and L0` and **Modeling
fidelity** to `Constant Ld, Lq and PM`.

### **Stator q-axis inductance, Lq** — Stator *q*-axis inductance `0.00022` `H` (default)

*q*-axis inductance of the stator.

#### Dependencies

To enable this parameter, set **Stator parameterization** to
`Specify Ld, Lq, and L0` and **Modeling
fidelity** to `Constant Ld, Lq and PM`.

### **Direct-axis current vector, iD** — Direct-axis current vector `[-200, 0, 200]` `A` (default) | vector of two or more values

Direct-axis current vector.

#### Dependencies

To enable this parameter, set **Stator parameterization** to
`Specify Ld, Lq, and L0` and **Modeling
fidelity** to `Tabulated Ld, Lq and PM`.

### **Quadrature-axis current vector, iQ** — Quadrature-axis current vector `[-200, 0, 200]` `A` (default) | vector of two or more values

Quadrature-axis current vector.

#### Dependencies

To enable this parameter, set **Stator parameterization** to
`Specify Ld, Lq, and L0` and **Modeling
fidelity** to `Tabulated Ld, Lq and PM`.

### **Ld matrix, Ld(id,iq)** — Ld matrix `0.0002 * ones(3, 3)` `H` (default) | matrix of scalars

Ld matrix. The number of rows of this matrix must be equal to the value of the
**Direct-axis current vector, iD** parameter. The number of columns
of this matrix must be equal to the value of the **Quadrature-axis current
vector, iQ** parameter.

#### Dependencies

To enable this parameter, set **Stator parameterization** to
`Specify Ld, Lq, and L0` and **Modeling
fidelity** to `Tabulated Ld, Lq and PM`.

### **Lq matrix, Lq(id,iq)** — Lq matrix `0.0002 * ones(3, 3)` `H` (default) | matrix of scalars

Lq matrix. The number of rows of this matrix must be equal to the value of the
**Direct-axis current vector, iD** parameter. The number of columns
of this matrix must be equal to the value of the **Quadrature-axis current
vector, iQ** parameter.

#### Dependencies

To enable this parameter, set **Stator parameterization** to
`Specify Ld, Lq, and L0` and **Modeling
fidelity** to `Tabulated Ld, Lq and PM`.

### **Permanent magnet flux linkage, PM(id,iq)** — Flux linkage of permanent magnet `0.1 * ones(3, 3)` `Wb` (default) | matrix of scalars

Flux linkage of the permanent magnet. The number of rows of this matrix must be
equal to the value of the **Direct-axis current vector, iD**
parameter. The number of columns of this matrix must be equal to the value of the
**Quadrature-axis current vector, iQ** parameter.

#### Dependencies

To enable this parameter, set:

- **Stator parameterization** to `Specify Ld,
  Lq, and L0`
- **Modeling fidelity** to `Tabulated Ld, Lq
  and PM`
- **Permanent magnet flux linkage parameterization** to
  `Specify flux linkage`

### **Torque constant matrix, kt(id,iq)** — Torque constant matrix `0.18 * ones(3, 3)` `N*m/A` (default) | matrix of scalars

Torque constant matrix. The number of rows of this matrix must be equal to the
value of the **Direct-axis current vector, iD** parameter. The number
of columns of this matrix must be equal to the value of the **Quadrature-axis
current vector, iQ** parameter.

#### Dependencies

To enable this parameter, set:

- **Stator parameterization** to `Specify Ld,
  Lq, and L0`
- **Modeling fidelity** to `Tabulated Ld, Lq
  and PM`
- **Permanent magnet flux linkage parameterization** to
  `Specify torque constant`

### **Back EMF constant matrix, ke(id,iq)** — Permanent magnet flux linkage `0.18 * ones(3, 3)` `V/(rad/s)` (default) | matrix of scalars

Back EMF constant matrix. The number of rows of this matrix must be equal to the
value of the **Direct-axis current vector, iD** parameter. The number
of columns of this matrix must be equal to the value of the **Quadrature-axis
current vector, iQ** parameter.

#### Dependencies

To enable this parameter, set:

- **Stator parameterization** to `Specify Ld,
  Lq, and L0`
- **Modeling fidelity** to `Tabulated Ld, Lq
  and PM`
- **Permanent magnet flux linkage parameterization** to
  `Specify back EMF constant`

### **Stator zero-sequence inductance, L0** — Stator zero-sequence inductance `0.00016` `H` (default) | positive scalar

Zero-sequence inductance of the stator.

#### Dependencies

To enable this parameter, set **Zero sequence** to
`Include`.

### **Stator self-inductance per phase, Ls** — Stator self-inductance per phase `0.0002` `H` (default) | positive scalar

Average self-inductance of each of the three stator windings.

#### Dependencies

To enable this parameter, set **Stator parameterization** to
`Specify Ls, Lm, and Ms`.

### **Stator inductance fluctuation, Lm** — Stator inductance fluctuation `-0.0002` `H` (default) | scalar

Amount that the self-inductance and mutual inductance of the stator windings
fluctuate with the rotor angle.

#### Dependencies

To enable this parameter, set **Stator parameterization** to
`Specify Ls, Lm, and Ms`.

### **Stator mutual inductance, Ms** — Average mutual inductance between stator windings `0.00002` `H` (default) | scalar

Average mutual inductance between the stator windings.

#### Dependencies

To enable this parameter, set **Stator parameterization** to
`Specify Ls, Lm, and Ms`.

### **Stator resistance per phase, Rs** — Resistance of each of stator windings `0.013` `Ohm` (default) | positive scalar

Resistance of each of the stator windings.

### **Zero sequence** — Option to include or exclude zero-sequence terms `Include` (default) | `Exclude`

Option to include or exclude zero-sequence terms.

- `Include` — Include zero-sequence terms. To
  prioritize model fidelity, use this default setting. Using this option:

  - Results in an error for simulations that use the Partitioning solver.
    For more information, see Increase Simulation Speed Using the Partitioning Solver.
  - Enables the **Stator zero-sequence inductance, L0**
    parameter.
- `Exclude` — Exclude zero-sequence terms. To
  prioritize simulation speed for desktop simulation or real-time deployment,
  select this option.

### Iron Losses

### **Model** — Option to enable iron losses computation `None` (default) | `Empirical`

Option to enable the iron losses computational model.

### **Open-circuit iron losses, [P\_hysteresis P\_eddy P\_excess]** — Open-circuit iron losses due to hysteresis, eddy, and excess losses `[0, 0, 0]` `W` (default) | row vector of three nonnegative elements

Open-circuit iron losses due to the hysteresis, eddy, and excess losses,
respectively, at the frequency you specify in the **Electrical frequency at
which losses determined** parameter.

#### Dependencies

To enable this parameter, set **Model** to
`Empirical`.

### **Short-circuit iron losses, [P\_hysteresis P\_eddy P\_excess]** — Short-circuit iron losses `[0, 0, 0]` `W` (default) | row vector of three nonnegative elements

Short-circuit iron losses due to the hysteresis, eddy, and excess losses,
respectively, at the frequency you specify in the **Electrical frequency at
which losses determined** parameter.

#### Dependencies

To enable this parameter, set **Model** to
`Empirical`.

### **Electrical frequency at which losses determined** — Electrical frequency at which losses are determined `60` `Hz` (default) | positive scalar

Electrical frequency at which the block measures the open-circuit and
short-circuit iron losses.

#### Dependencies

To enable this parameter, set **Model** to
`Empirical`.

### **Short-circuit RMS current for short-circuit iron losses** — Short-circuit RMS current for short-circuit iron losses `95` `A` (default) | positive scalar

Resulting short-circuit RMS phase current when measuring the short-circuit
losses.

#### Dependencies

To enable this parameter, set **Model** to
`Empirical`.

### Mechanical

### **Rotor inertia** — Rotor inertia `0.01` `kg*m^2` (default) | nonnegative scalar

Inertia of the rotor that attaches to the mechanical translational port
**R**.

### **Rotor damping** — Rotary damping `0` `N*m/(rad/s)` (default) | nonnegative scalar

Rotary damping.

### Temperature Dependence

### **Measurement temperature** — Temperature at which block quotes motor parameters `298.15` `K` (default) | positive scalar

Temperature at which the block quotes the motor parameters.

#### Dependencies

To enable this parameter, set **Modeling option** to
`Show thermal port`.

### **Resistance temperature coefficient** — Resistance temperature coefficient `3.93e-3` `1/K` (default) | nonnegative scalar

Coefficient α in the equation relating resistance to temperature. For more
information, see Thermal Model for Actuator Blocks. The
default value is for copper.

#### Dependencies

To enable this parameter, set **Modeling option** to
`Show thermal port`.

### **Permanent magnet flux temperature coefficient** — Fractional rate at which permanent magnet flux density changes with temperature `-0.001` `1/K` (default) | nonpositive scalar

Fractional rate at which the permanent magnet flux density changes with the
temperature. Use this parameter to linearly reduce the torque and the induced back EMF
as the temperature rises.

#### Dependencies

To enable this parameter, set **Modeling option** to
`Show thermal port`.

### Thermal Port

### **Thermal mass for each stator winding** — Thermal mass for each stator winding `100` `J/K` (default) | positive scalar

Thermal mass value for the A, B, and C windings. The thermal mass is the energy
required to raise the temperature by one degree.

#### Dependencies

To enable this parameter, set **Modeling option** to
`Show thermal port`.

### **Rotor thermal mass** — Thermal mass of rotor `200` `J/K` (default) | positive scalar

Thermal mass of the rotor. This value is the energy required to raise the
temperature of the rotor by one degree.

#### Dependencies

To enable this parameter, set **Modeling option** to
`Show thermal port`.

### **Percentage of main flux path iron losses associated with the rotor** — Percentage of iron losses on main flux path associated with rotor `90` (default) | positive scalar

Percentage of the iron losses on the main flux path associated with the magnetic
path through the rotor. This parameter determines how much of the iron loss heating
the block attributes to the rotor thermal port, **HR**, and to the
stator thermal port, **HS**.

#### Dependencies

To enable this parameter, set **Modeling option** to
`Show thermal port` and, in the **Iron
Losses** tab, set **Model** to
`Empirical`.

### **Percentage of cross-tooth flux path iron losses associated with the rotor** — Percentage of iron losses on cross-tooth flux path associated with rotor `30` (default) | positive scalar

Percentage of the iron losses on the cross-tooth flux path associated with the
magnetic path through the rotor. This parameter determines how much of the iron loss
heating the block attributes to the rotor thermal port, **HR**, and
to the stator thermal port, **HS**.

#### Dependencies

To enable this parameter, set **Modeling option** to
`Show thermal port` and, in the **Iron
Losses** tab, set **Model** to
`Empirical`.
## Libraries

Simscape / Electrical / Electromechanical / Permanent Magnet

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

## Description

Direct-quadrature-zero representation of permanent magnet synchronous machine

The PMSM (DQ0) block models the direct-quadrature-zero
(dq0) frame representation of a permanent magnet synchronous motor (PMSM) with a three-phase
stator. Use this block to model an interior permanent magnet synchronous machine (IPMSM),
surface permanent magnet synchronous machine (SPMSM), transverse flux motor, axial flux
(pancake) motor, or PMSM servomotor.

PMSMs have a permanent magnet rotor and a wound stator. You use these motors in traction
applications such as electric vehicles (EVs) and in actuation systems. In actuation systems,
PMSMs are also called *brushless servomotors*. You typically design a
PMSM to have a sinusoidal back electromotive force (EMF) profile. This design reduces
undesirable high-frequency mechanical and electrical current harmonics compared to motors like
the brushless DC (BLDC) motor that have a trapezoidal back EMF
profile.

Use this block to model the two main types of PMSM:

- SPSM or surface permanent magnet (SPM) motor — The "S" signifies that the rotor
  magnets are surface mounted. *Ld* and *Lq* are
  equal.
- IPSM or interior permanent magnet (IPM) motor — The "I" signifies that the rotor
  magnets are interior to the rotor. *Ld* and *Lq* are
  not equal.

You can also categorize PMSMs based on the main flux paths. The main flux paths are
commonly radial but can be axial, which causes higher torques for the same physical size of
motor. You can use the PMSM (DQ0) block to model both
categories of PMSM.

**Note**

Simscape™
Electrical™ includes several blocks that can model the same type of motor or actuator.
Choose a block that has sufficient modeling detail for the engineering design questions that
you need to answer. Do not use a block that has more modeling detail than you need, because
higher-fidelity models slow down simulation and are more complex to parameterize.

Blocks like the PMSM (DQ0) block model motors with fixed or
parameter-dependent coefficients with a simple equivalent circuit. These models have an
intermediate level of fidelity. Use this block to design controls or systems in actuation
applications, such as robotics and mechatronics, and for efficiency predictions when saturation
and harmonics only weakly impact losses. For more information about choosing the right block to
model your motor at the right level of fidelity, see Choose Blocks to Model Motors or Actuators.

### Equations

Applying Park’s transformation to the block electrical equations produces an expression
for torque that is independent of the rotor angle.

This equation defines the Park’s transformation:

P=2/3[cosθecos(θe−2π/3)cos(θe+2π/3)−sinθe−sin(θe−2π/3)−sin(θe+2π/3)0.50.50.5],

where *θe* is the electrical angle and is equal
to *Nθr*. *N* is the number of pole
pairs.

The block uses the Park's transformation on the stator winding voltages and currents to
transform them to the dq0 frame, which is independent of the rotor angle:

[vdvqv0]=P[vavbvc]

[idiqi0]=P[iaibic]

vd=Rsid+Lddiddt−NωiqLq

vq=Rsiq+Lqdiqdt+Nω(idLd+ψm)

v0=Rsi0+L0di0dt

T=32N(iq(idLd+ψm)−idiqLq)

where:

- *Ld* =
  *Ls* +
  *Ms* + 3/2
  *Lm*.
  *Ld* is the stator *d*-axis
  inductance.
- *Lq* =
  *Ls* +
  *Ms* − 3/2
  *Lm*.
  *Lq* is the stator *q*-axis
  inductance.
- *L0* =
  *Ls* –
  2*Ms*.
  *L0* is the stator zero-sequence
  inductance.
- *ω* is the rotor mechanical rotational speed.
- *N* is the number of rotor permanent magnet pole pairs.
- *T* is the rotor torque. Torque flows from the port **C**,
  which represents the motor case, to port **R**, which represents the motor
  rotor.

The PMSM (DQ0) block uses the original, non-orthogonal
implementation of the Park transform. If you try to apply the alternative implementation,
you get different results for the dq0 voltage and currents.

### Alternative Flux Linkage Parameterization

You can parameterize the motor by using the back EMF or torque constants by using the
**Permanent magnet flux linkage** parameter.

The back EMF constant is the peak voltage that the permanent magnet induces in the
per-unit rotational speed of each of the phases. The relationship between the peak permanent
magnet flux linkage and the back EMF is:

ke=Nψm.

The back EMF, *eph*, for one phase is:

eph=keω.

The torque constant is the peak torque that the per-unit current of each of the phases
induces. The torque constant is numerically identical in value to the back EMF constant when
both are expressed in SI units:

kt=Nψm.

When
*Ld*=*Lq*
and the currents in all three phases are balanced, the combined torque *T* is:

T=32ktiq=32ktIpk,

where *Ipk* is the peak current in any of the
three windings.

The factor 3/2 follows from this being the steady-state sum of the torques from all
phases. Therefore, the torque constant *kt* is also
equal to:

kt=23(TIpk),

where *T* is the measured total torque when testing with
a balanced three-phase current with peak line voltage
*Ipk*. The RMS line current is:

kt=23Tiline,rms.

### Calculating Iron Losses

Iron losses consist of two terms, one representing the main magnetizing path and the
other representing the cross-tooth tip path that becomes active during the field-weakening
operation. The iron losses model is based on [3].

The term that represents the main magnetizing path depends on the induced RMS
line-to-neutral stator voltage, Vmrms:

POC(Vmrms)=ahkVmrms+ajk2Vmrms2+aexk1.5Vmrms1.5.

This term is dominant during the no-load operation. *k* is the back EMF
constant relating the RMS volts per Hz. This term is equal to k=Vmrms/f, where *f* is the electrical frequency. The first term on
the right side is the magnetic hysteresis loss, the second is the eddy current loss, and the
third is the excess loss. The block derives the three coefficients on the numerators from
the values that you specify for the open-circuit hysteresis, eddy, and excess losses.

The term representing the cross-tooth tip path is relevant when a demagnetizing field is
set up and can be determined from a finite element analysis short-circuit test. This term
depends on the RMS EMF associated with the cross-tooth tip flux, Vdrms\*:

PSC(Vdrms\*)=bhkVdrms\*+bjk2Vdrms\*2+bexk1.5Vdrms\*1.5.

The block derives the three numerator terms from the values you specify for the
short-circuit hysteresis, eddy, and excess losses.

### Model Thermal Effects

You can expose the thermal ports to model the effects of losses that convert power to
heat. To expose the thermal ports, set the **Modeling option** parameter to
one of these values:

- `No thermal port` — The block contains the electrical
  conserving ports associated with the stator dq0 quantities but does not contain
  thermal ports.
- `Show thermal port` — The block contains the electrical
  conserving ports associated with the stator dq0 quantities and the thermal conserving
  ports for the stator and for the rotor.

For more information about using thermal ports in actuator blocks, see Simulating Thermal Effects in Rotational and Translational Actuators.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. You can
specify nominal values using different sources, including the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
