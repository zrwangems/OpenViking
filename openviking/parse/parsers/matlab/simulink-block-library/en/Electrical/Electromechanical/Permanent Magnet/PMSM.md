---
type: simulink-block
title: 'PMSM'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Permanent Magnet'
documentation_page: 'pmsm'
documentation_source_path: 'ref/pmsm.html'
language: en
---

# PMSM

## Ports
```yaml
ports:
- name: '~'
  summary: Three-phase port electrical
  direction: conserving
- name: a
  summary: '*a*-phase electrical'
  direction: conserving
- name: b
  summary: '*b*-phase electrical'
  direction: conserving
- name: c
  summary: '*c*-phase electrical'
  direction: conserving
- name: ~1
  summary: Stator positive-end connections electrical
  direction: conserving
- name: ~2
  summary: Stator negative-end connections electrical
  direction: conserving
- name: a1
  summary: '*a* positive-end connection electrical'
  direction: conserving
- name: b1
  summary: '*b* positive-end connection electrical'
  direction: conserving
- name: c1
  summary: '*c* positive-end connection electrical'
  direction: conserving
- name: a2
  summary: '*a* negative-end connection electrical'
  direction: conserving
- name: b2
  summary: '*b* negative-end connection electrical'
  direction: conserving
- name: c2
  summary: '*c* negative-end connection electrical'
  direction: conserving
- name: n
  summary: Neutral phase electrical
  direction: conserving
- name: R
  summary: Motor rotor mechanical
  direction: conserving
- name: C
  summary: Motor case mechanical
  direction: conserving
- name: HA
  summary: Winding A thermal port thermal
  direction: conserving
- name: HB
  summary: Winding B thermal port thermal
  direction: conserving
- name: HC
  summary: Winding C thermal port thermal
  direction: conserving
- name: HR
  summary: Rotor thermal port thermal
  direction: conserving
```

### Conserving

### **~** — Three-phase port electrical

Expandable three-phase port. For more information, see Three-phase
port.

#### Dependencies

To enable this port, set **Electrical
connection** to `Composite three-phase
ports` and **Winding type** to
`Wye-wound` or
`Delta-wound`.

### **a** — *a*-phase electrical

Electrical conserving port associated with
*a*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports` and **Winding type** to
`Wye-wound` or
`Delta-wound`.

### **b** — *b*-phase electrical

Electrical conserving port associated with
*b*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports` and **Winding type** to
`Wye-wound` or
`Delta-wound`.

### **c** — *c*-phase electrical

Electrical conserving port associated with
*c*-phase.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports` and **Winding type** to
`Wye-wound` or
`Delta-wound`.

### **~1** — Stator positive-end connections electrical

*Since R2024a*

Expandable three-phase
port associated with the stator positive-end
connections.

#### Dependencies

To enable this port, set **Electrical
connection** to `Composite three-phase
ports` and **Winding type** to
`Open-end`.

### **~2** — Stator negative-end connections electrical

*Since R2024a*

Expandable three-phase
port associated with the stator negative-end
connections.

#### Dependencies

To enable this port, set **Electrical
connection** to `Composite three-phase
ports` and **Winding type** to
`Open-end`.

### **a1** — *a* positive-end connection electrical

*Since R2024a*

Electrical conserving port associated with the *a*
positive-end connection.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports` and **Winding type** to
`Open-end`.

### **b1** — *b* positive-end connection electrical

*Since R2024a*

Electrical conserving port associated with the *b*
positive-end connection.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports` and **Winding type** to
`Open-end`.

### **c1** — *c* positive-end connection electrical

*Since R2024a*

Electrical conserving port associated with the *c*
positive-end connection.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports` and **Winding type** to
`Open-end`.

### **a2** — *a* negative-end connection electrical

*Since R2024a*

Electrical conserving port associated with the *a*
negative-end connection.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports` and **Winding type** to
`Open-end`.

### **b2** — *b* negative-end connection electrical

*Since R2024a*

Electrical conserving port associated with the *b*
negative-end connection.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports` and **Winding type** to
`Open-end`.

### **c2** — *c* negative-end connection electrical

*Since R2024a*

Electrical conserving port associated with the *c*
negative-end connection.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports` and **Winding type** to
`Open-end`.

### **n** — Neutral phase electrical

Electrical conserving port associated with the neutral phase.

#### Dependencies

To enable this port, set **Winding Type** to
`Wye-wound` and **Zero
sequence** to
`Include`.

### **R** — Motor rotor mechanical

Mechanical rotational conserving port associated with the motor
rotor.

### **C** — Motor case mechanical

Mechanical rotational conserving port associated with the motor
case.

### **HA** — Winding A thermal port thermal

Thermal conserving port associated with winding A.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **HB** — Winding B thermal port thermal

Thermal conserving port associated with winding B.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **HC** — Winding C thermal port thermal

Thermal conserving port associated with winding C.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **HR** — Rotor thermal port thermal

Thermal conserving port associated with the rotor.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.
## Parameters
```yaml
parameters:
- name: Selected part
  summary: Predefined parameterization option <click to select> (default)
  group: ''
- name: Modeling option
  summary: Whether to enable thermal ports No thermal port (default) | Show thermal port
  group: ''
- name: Electrical connection
  summary: Electrical connection Composite three-phase ports (default) | Expanded three-phase ports
  group: Main
- name: Winding type
  summary: Windings configuration Wye-wound (default) | Delta-wound | Open-end
  group: Main
- name: Modeling fidelity
  summary: Modeling fidelity Constant Ld, Lq and PM (default) | Tabulated Ld, Lq and PM
  group: Main
- name: Number of pole pairs
  summary: Number of pole pairs 6 (default)
  group: Main
- name: Permanent magnet flux linkage parameterization
  summary: Permanent magnet flux linkage parameterization Specify flux linkage (default) | Specify torque constant | Specify
    back EMF constant
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
  summary: Stator parameterization Specify Ld, Lq, and L0 (default) | Specify Ls, Lm, and Ms
  group: Main
- name: Stator d-axis inductance, Ld
  summary: Stator d-axis inductance 0.00022 H (default)
  group: Main
- name: Stator q-axis inductance, Lq
  summary: Stator q-axis inductance 0.00022 H (default)
  group: Main
- name: Direct-axis current vector, iD
  summary: Direct-axis current vector [-200, 0, 200] A (default)
  group: Main
- name: Quadrature-axis current vector, iQ
  summary: Quadrature-axis current vector [-200, 0, 200] A (default)
  group: Main
- name: Ld matrix, Ld(id,iq)
  summary: Ld matrix 0.0002 * ones(3, 3) H (default)
  group: Main
- name: Lq matrix, Lq(id,iq)
  summary: Lq matrix 0.0002 * ones(3, 3) H (default)
  group: Main
- name: Permanent magnet flux linkage, PM(id,iq)
  summary: Permanent magnet flux linkage 0.1 * ones(3, 3) Wb (default)
  group: Main
- name: Torque constant matrix, kt(id,iq)
  summary: Force constant matrix 0.18 * ones(3, 3) N*m/A (default)
  group: Main
- name: Back EMF constant matrix, ke(id,iq)
  summary: Permanent magnet flux linkage 0.18 * ones(3, 3) V/(rad/s) (default)
  group: Main
- name: Stator zero-sequence inductance, L0
  summary: Stator zero-sequence inductance 0.00016 H (default)
  group: Main
- name: Stator self-inductance per phase, Ls
  summary: Stator self-inductance per phase 0.0002 H (default)
  group: Main
- name: Stator inductance fluctuation, Lm
  summary: Stator inductance fluctuation -0.0002 H (default)
  group: Main
- name: Stator mutual inductance, Ms
  summary: Stator mutual inductance 0.00002 H (default)
  group: Main
- name: Stator resistance per phase, Rs
  summary: Stator resistance per phase 0.013 Ohm (default)
  group: Main
- name: Zero sequence
  summary: Zero sequence option Include (default) | Exclude
  group: Main
- name: Rotor angle definition
  summary: Reference point for rotor angle measurement Angle between the a-phase magnetic axis and the d-axis (default) |
    Angle between the a-phase magnetic axis and the q-axis
  group: Main
- name: Model
  summary: Enable Iron losses computation None (default) | Empirical
  group: Iron Losses
- name: Open-circuit iron losses, [P_hysteresis P_eddy P_excess]
  summary: Open-circuit iron losses [0, 0, 0] W (default)
  group: Iron Losses
- name: Short-circuit iron losses, [P_hysteresis P_eddy P_excess]
  summary: Short-circuit iron losses [0, 0, 0] W (default)
  group: Iron Losses
- name: Electrical frequency at which losses determined
  summary: Electrical frequency at which losses determined 60 Hz (default)
  group: Iron Losses
- name: Short-circuit RMS current for short-circuit iron losses
  summary: Short-circuit RMS current for short-circuit iron losses 95 A (default)
  group: Iron Losses
- name: Rotor inertia
  summary: Rotor inertia 0.01 kg*m^2 (default) | nonnegative scalar
  group: Mechanical
- name: Rotor damping
  summary: Rotor damping 0 N*m/(rad/s) (default) | nonnegative scalar
  group: Mechanical
- name: Measurement temperature
  summary: Temperature at which block quotes motor parameters 298.15 K (default)
  group: Temperature Dependence
- name: Resistance temperature coefficient
  summary: Resistance temperature coefficient 3.93e-3 1/K (default)
  group: Temperature Dependence
- name: Permanent magnet flux temperature coefficient
  summary: Fractional rate at which permanent magnet flux density changes with temperature -0.001 1/K (default) | scalar
  group: Temperature Dependence
- name: Thermal mass for each stator winding
  summary: Thermal mass for each stator winding 100 J/K (default)
  group: Thermal Port
- name: Rotor thermal mass
  summary: Rotor thermal mass 200 J/K (default)
  group: Thermal Port
- name: Percentage of main flux path iron losses associated with the rotor
  summary: Percentage of main flux path iron losses associated with the rotor 90 (default)
  group: Thermal Port
- name: Percentage of cross-tooth flux path iron losses associated with the rotor
  summary: Percentage of cross-tooth flux path iron losses associated with the rotor 30 (default)
  group: Thermal Port
```

### **Selected part** — Predefined parameterization option `<click to select>` (default)

Option to parameterize the block to represent components by specific suppliers. Click the
**<click to select>** hyperlink to open the Block
Parameterization Manager window. For more information about the Block Parameterization
Manager, see Load Predefined Parameterizations.

### **Modeling option** — Whether to enable thermal ports `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal ports of the block and model the effects of losses that
convert power to heat.

### Main

### **Electrical connection** — Electrical connection `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to have composite or expanded three-phase ports.

### **Winding type** — Windings configuration `Wye-wound` (default) | `Delta-wound` | `Open-end`

Select the configuration for the windings:

- `Wye-wound` — The windings are
  wye-wound.
- `Delta-wound` — The windings are
  delta-wound. The *a*-phase is connected
  between ports **a** and
  **b**, the *b*-phase
  between ports **b** and
  **c** and the
  *c*-phase between ports
  **c** and
  **a**.
- `Open-end` — The windings are in
  an open-end configuration. The block exposes each end of the
  windings as electrical connections.

### **Modeling fidelity** — Modeling fidelity `Constant Ld, Lq and PM` (default) | `Tabulated Ld, Lq and PM`

Select the modeling fidelity:

- `Constant Ld, Lq and PM` —
  *Ld*, *Lq* and
  *PM* values are constant and defined by
  their respective parameters.
- `Tabulated Ld, Lq and PM` —
  *Ld*, *Lq* and
  *PM* values are computed online from DQ
  currents look-up tables as follows:

  Ld=f1(id,iq)

  Ld=f2(id,iq)

  λPM=f2(id,iq)

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify Ld, Lq, and
L0`.

### **Number of pole pairs** — Number of pole pairs `6` (default)

Number of permanent magnet pole pairs on the rotor.

### **Permanent magnet flux linkage parameterization** — Permanent magnet flux linkage parameterization `Specify flux linkage` (default) | `Specify torque constant` | `Specify back EMF constant`

Choose `Specify flux linkage`,
`Specify torque constant`, or
`Specify back EMF constant`.

### **Permanent magnet flux linkage** — Permanent magnet flux linkage `0.03` `Wb` (default)

Peak permanent magnet flux linkage with any of the stator
windings.

#### Dependencies

To enable this parameter, set **Permanent magnet flux
linkage parameterization** to `Specify flux
linkage` and **Modeling fidelity**
to `Constant Ld, Lq and PM`.

### **Torque constant** — Torque constant `0.18` `N*m/A` (default)

Torque constant with any of the stator windings.

#### Dependencies

To enable this parameter, set **Permanent magnet flux
linkage parameterization** to `Specify
torque constant` and **Modeling
fidelity** to `Constant Ld, Lq and
PM`.

### **Back EMF constant** — Back EMF constant `0.18` `V*s/rad` (default)

Back EMF constant with any of the stator windings.

**Note**

The back EMF constant is the peak voltage induced by the
permanent magnet in the per-unit rotational speed of each of the
phases. For a wye-wound motor, this voltage is the
line-to-neutral voltage.

#### Dependencies

To enable this parameter, set **Permanent magnet flux
linkage parameterization** to `Specify back
EMF constant` and **Modeling
fidelity** to `Constant Ld, Lq and
PM`.

### **Stator parameterization** — Stator parameterization `Specify Ld, Lq, and L0` (default) | `Specify Ls, Lm, and Ms`

Choose `Specify Ld, Lq, and L0` or
`Specify Ls, Lm, and Ms`.

### **Stator d-axis inductance, Ld** — Stator d-axis inductance `0.00022` `H` (default)

D-axis inductance.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify Ld, Lq, and
L0` and **Modeling fidelity** to
`Constant Ld, Lq and PM`.

### **Stator q-axis inductance, Lq** — Stator q-axis inductance `0.00022` `H` (default)

Q-axis inductance.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify Ld, Lq, and
L0` and **Modeling fidelity** to
`Constant Ld, Lq and PM`.

### **Direct-axis current vector, iD** — Direct-axis current vector `[-200, 0, 200]` `A` (default)

Direct-axis current vector, iD.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify Ld, Lq, and
L0` and **Modeling fidelity** to
`Tabulated Ld, Lq and PM`.

### **Quadrature-axis current vector, iQ** — Quadrature-axis current vector `[-200, 0, 200]` `A` (default)

Quadrature-axis current vector, iQ.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify Ld, Lq, and
L0` and **Modeling fidelity** to
`Tabulated Ld, Lq and PM`.

### **Ld matrix, Ld(id,iq)** — Ld matrix `0.0002 * ones(3, 3)` `H` (default)

Ld matrix.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify Ld, Lq, and
L0` and **Modeling fidelity** to
`Tabulated Ld, Lq and PM`.

### **Lq matrix, Lq(id,iq)** — Lq matrix `0.0002 * ones(3, 3)` `H` (default)

Lq matrix.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify Ld, Lq, and
L0` and **Modeling fidelity** to
`Tabulated Ld, Lq and PM`.

### **Permanent magnet flux linkage, PM(id,iq)** — Permanent magnet flux linkage `0.1 * ones(3, 3)` `Wb` (default)

Permanent magnet flux linkage.

#### Dependencies

To enable this parameter, set:

- **Stator parameterization** to
  `Specify Ld, Lq, and
  L0`
- **Modeling fidelity** to
  `Tabulated Ld, Lq and
  PM`
- **Permanent magnet flux linkage
  parameterization** to `Specify
  flux linkage`

### **Torque constant matrix, kt(id,iq)** — Force constant matrix `0.18 * ones(3, 3)` `N*m/A` (default)

Torque constant matrix.

#### Dependencies

To enable this parameter, set:

- **Stator parameterization** to
  `Specify Ld, Lq, and
  L0`
- **Modeling fidelity** to
  `Tabulated Ld, Lq and
  PM`
- **Permanent magnet flux linkage
  parameterization** to `Specify
  torque constant`

### **Back EMF constant matrix, ke(id,iq)** — Permanent magnet flux linkage `0.18 * ones(3, 3)` `V/(rad/s)` (default)

Back EMF constant matrix.

#### Dependencies

To enable this parameter, set:

- **Stator parameterization** to
  `Specify Ld, Lq, and
  L0`
- **Modeling fidelity** to
  `Tabulated Ld, Lq and
  PM`
- **Permanent magnet flux linkage
  parameterization** to `Specify
  back EMF constant`

### **Stator zero-sequence inductance, L0** — Stator zero-sequence inductance `0.00016` `H` (default)

Zero-sequence inductance.

#### Dependencies

To enable this parameter either:

- Set **Winding Type** to
  `Wye-wound`, **Zero
  sequence** to
  `Include`, and
  **Stator parameterization** to
  `Specify Ld, Lq, and
  L0`.
- Set **Winding Type** to
  `Delta-wound` and
  **Stator parameterization** to
  `Specify Ld, Lq, and
  L0`.

### **Stator self-inductance per phase, Ls** — Stator self-inductance per phase `0.0002` `H` (default)

Average self-inductance of each of the three stator windings.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify Ls, Lm, and
Ms`.

### **Stator inductance fluctuation, Lm** — Stator inductance fluctuation `-0.0002` `H` (default)

Amount that the self-inductance and mutual inductance of the stator
windings fluctuate with the rotor angle.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify Ls, Lm, and
Ms`.

### **Stator mutual inductance, Ms** — Stator mutual inductance `0.00002` `H` (default)

Average mutual inductance between the stator windings.

#### Dependencies

To enable this parameter, set **Stator
parameterization** to `Specify Ls, Lm, and
Ms`.

### **Stator resistance per phase, Rs** — Stator resistance per phase `0.013` `Ohm` (default)

Resistance of each of the stator windings.

### **Zero sequence** — Zero sequence option `Include` (default) | `Exclude`

Option to include or exclude zero-sequence terms.

- `Include` — Include zero-sequence terms. To prioritize model fidelity, use this default setting. Using this option:

  - Results in an error for simulations that use the Partitioning solver. For more information, see Increase Simulation Speed Using the Partitioning Solver.
  - Exposes the **Stator zero-sequence inductance,
    L0** parameter.
- `Exclude` — Exclude zero-sequence terms. To prioritize simulation speed for desktop simulation or real-time deployment, select this option.

#### Dependencies

To enable this parameter, set **Winding Type** to
`Wye-wound`.

### **Rotor angle definition** — Reference point for rotor angle measurement `Angle between the a-phase magnetic axis and the d-axis` (default) | `Angle between the a-phase magnetic axis and the q-axis`

Reference point for the rotor angle measurement. The figure in the
Motor Construction section shows the
default value, `Angle between the a-phase magnetic axis and
the d-axis`. When you select this value, the rotor and
*a*-phase fluxes align when the rotor angle is
zero.

When you select `Angle between the a-phase magnetic axis
and the q-axis`, the *a*-phase current
generates maximum torque when the rotor angle is zero.

### Iron Losses

### **Model** — Enable Iron losses computation `None` (default) | `Empirical`

Specify the iron losses computational model.

### **Open-circuit iron losses, [P\_hysteresis P\_eddy P\_excess]** — Open-circuit iron losses `[0, 0, 0]` `W` (default)

Row vector, of length 3, of the open-circuit iron losses due to
hysteresis, Eddy, and excess losses, respectively, at the frequency
specified by **Electrical frequency at which losses
determined**.

#### Dependencies

To enable this parameter, set **Model** to
`Empirical`.

### **Short-circuit iron losses, [P\_hysteresis P\_eddy P\_excess]** — Short-circuit iron losses `[0, 0, 0]` `W` (default)

Row vector, of length 3, of the short-circuit iron losses due to
hysteresis, Eddy, and excess losses, respectively, at the frequency
specified by **Electrical frequency at which losses
determined**.

#### Dependencies

To enable this parameter, set **Model** to
`Empirical`.

### **Electrical frequency at which losses determined** — Electrical frequency at which losses determined `60` `Hz` (default)

Electrical frequency at which the block measures the open-circuit and
short-circuit iron losses.

#### Dependencies

To enable this parameter, set **Model** to
`Empirical`.

### **Short-circuit RMS current for short-circuit iron losses** — Short-circuit RMS current for short-circuit iron losses `95` `A` (default)

Resulting short-circuit RMS phase current when measuring the
short-circuit losses.

#### Dependencies

To enable this parameter, set **Model** to
`Empirical`.

### Mechanical

### **Rotor inertia** — Rotor inertia `0.01` `kg*m^2` (default) | nonnegative scalar

Inertia of the rotor attached to mechanical translational port
**R**. The value can be zero.

### **Rotor damping** — Rotor damping `0` `N*m/(rad/s)` (default) | nonnegative scalar

Rotary damping.

### Temperature Dependence

### **Measurement temperature** — Temperature at which block quotes motor parameters `298.15` `K` (default)

Temperature at which the block quotes the motor parameters.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Show thermal port`.

### **Resistance temperature coefficient** — Resistance temperature coefficient `3.93e-3` `1/K` (default)

Coefficient α in the equation relating resistance to temperature. For
more information, see Thermal Model for Actuator Blocks. The default value is for
copper.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Show thermal port`.

### **Permanent magnet flux temperature coefficient** — Fractional rate at which permanent magnet flux density changes with temperature `-0.001` `1/K` (default) | scalar

Fractional rate at which the permanent magnet flux density changes
with the temperature. Use this parameter to linearly reduce the torque
and the induced back EMF as the temperature rises.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Show thermal port`.

### Thermal Port

### **Thermal mass for each stator winding** — Thermal mass for each stator winding `100` `J/K` (default)

Thermal mass value for the A, B, and C windings. The thermal mass is
the energy required to raise the temperature by one degree.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Show thermal port`.

### **Rotor thermal mass** — Rotor thermal mass `200` `J/K` (default)

Thermal mass of the rotor, that is, the energy required to raise the
temperature of the rotor by one degree.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Show thermal port`.

### **Percentage of main flux path iron losses associated with the rotor** — Percentage of main flux path iron losses associated with the rotor `90` (default)

Percentage of the main flux path iron losses associated with the
magnetic path through the rotor. It determines how much of the iron loss
heating is attributed to the rotor thermal port **HR**,
and how much is attributed to the three winding thermal ports
**HA**, **HB**, and
**HC**.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Show thermal port` and, in the
**Iron Losses** tab, set
**Model** to
`Empirical`.

### **Percentage of cross-tooth flux path iron losses associated with the rotor** — Percentage of cross-tooth flux path iron losses associated with the rotor `30` (default)

Percentage of the cross-tooth flux path iron losses associated with
the magnetic path through the rotor. It determines how much of the iron
loss heating is attributed to the rotor thermal port
**HR**, and how much is attributed to the three
winding thermal ports **HA**, **HB**,
and **HC**.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Show thermal port` and, in the
**Iron Losses** tab, set
**Model** to
`Empirical`.
## Libraries

Simscape / Electrical / Electromechanical / Permanent Magnet

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

### R2024a: Open-end configuration for stator windings

To model the stator windings of the machine in an open-end configuration, set the
**Winding type** parameter to
`Open-end`. The PMSM block then exposes each end
of the windings by enabling the corresponding electrical conserving ports.

### R2021b: Electrical connection ports update

From R2021b forward, to switch between composite and expanded ports, set the
**Electrical connection** parameter to either
`Composite three-phase ports` or `Expanded
three-phase ports`.

As a result of these changes, inside a model saved in an earlier release, review
the **Electrical connection** parameter of this block.

## Description

Permanent magnet synchronous motor with sinusoidal flux distribution

The PMSM block models a permanent magnet synchronous
motor (PMSM) with a three-phase wye-wound, delta-wound, or open-ended stator. Use this
block to model an interior permanent magnet synchronous motor (IPMSM), surface permanent
magnet synchronous motor (SPMSM), transverse flux motor, axial flux (pancake) motor, or
PMSM servomotor.

PMSMs have a permanent magnet rotor and a wound stator. You can use these motors in
traction applications like electric vehicles (EVs) and in actuation systems. In
actuation systems, PMSMs are also called *brushless servomotors*. A
PMSM typically has a sinusoidal back EMF profile to reduce undesirable high-frequency
mechanical and electrical current harmonics compared to brushless direct current
(BLDC) motors, which have a
trapezoidal back EMF profile.

The PMSM block models the motor with fixed
*d*-axis and *q*-axis inductances,
*Ld* and *Lq*. You can use this block to model the
two main types of PMSM:

- SPMSM or surface permanent magnet (SPM) motor — The rotor magnets are
  surface mounted. *Ld* and *Lq* are
  equal.
- IPMSM or interior permanent magnet (IPM) motor — The rotor magnets are
  interior to the rotor. *Ld* and *Lq* are
  not equal.

You can also categorize PMSMs based on the main flux paths. The main flux paths are
commonly radial but can be axial, which causes much higher torques for the same physical
size of motor. You can use the PMSM block to model both
radial- and axial-flux PMSMs.

You can use the **Winding type** parameter to specify the
configuration for the windings. This figure shows the equivalent electrical circuit for
a wye-wound stator.

You can also model a delta-wound or open-end stator by setting **Winding
type** to `Delta-wound` or
`Open-end`, respectively.

You can choose different built-in parameterizations for this block. For more
information, see the Predefined Parameterization section.

**Note**

Simscape™
Electrical™ includes several blocks that can model the same type of motor or actuator.
Choose a block that has sufficient modeling detail for the engineering design questions that
you need to answer. Do not use a block that has more modeling detail than you need, because
higher-fidelity models slow down simulation and are more complex to parameterize.

Blocks like the PMSM block model motors with fixed or
parameter-dependent coefficients with a simple equivalent circuit. These models have an
intermediate level of fidelity. Use this block to design controls or systems in actuation
applications, such as robotics and mechatronics, and for efficiency predictions when saturation
and harmonics only weakly impact losses. For more information about choosing the right block to
model your motor at the right level of fidelity, see Choose Blocks to Model Motors or Actuators.

### Motor Construction

This figure shows the motor construction with a single pole-pair on the rotor.

Permanent magnets generate a rotor magnetic field that creates a sinusoidal rate
of change of flux based on the rotor angle.

For the axes convention, when you set the **Rotor angle
definition** parameter to `Angle between the a-phase
magnetic axis and the d-axis`, the *a*-phase and
permanent magnet fluxes align when the rotor mechanical angle,
*θr*, is zero. When you set the
**Rotor angle definition** parameter to `Angle
between the a-phase magnetic axis and the q-axis`, the rotor
mechanical angle is the angle between the *a*-phase magnetic axis
and the rotor *q*-axis.

### Equations

Voltages across the stator windings are

[vavbvc]=[Rs000Rs000Rs][iaibic]+[dψadtdψbdtdψcdt],

where:

- *va*,
  *vb*, and
  *vc* are the individual
  phase voltages across the stator windings.
- *Rs* is the equivalent resistance
  of each stator winding.
- *ia*,
  *ib*, and
  *ic* are the currents
  flowing in the stator windings.
- dψadt,dψbdt, and dψcdt are the rates of change for the magnetic flux in each
  stator winding.

The permanent magnet and the three windings contribute to the total flux linking
each winding. The total flux is

[ψaψbψc]=[LaaLabLacLbaLbbLbcLcaLcbLcc][iaibic]+[ψamψbmψcm],

where:

- *ψa*,
  *ψb*, and
  *ψc* are the total fluxes
  linking each stator winding.
- *Laa*,
  *Lbb*, and
  *Lcc* are the
  self-inductances of the stator windings.
- *Lab*,
  *Lac*,
  *Lba*, and so on, are the
  mutual inductances of the stator windings.
- *ψam*,
  *ψbm*, and
  *ψcm* are the permanent
  magnet fluxes linking the stator windings.

The inductances in the stator windings are functions of the rotor electrical angle
and defined by

θe=Nθr+rotor offset

Laa=Ls+Lmcos(2θe)

Lbb=Ls+Lmcos(2(θe−2π/3))

Lcc=Ls+Lmcos(2(θe+2π/3))

Lab=Lba=−Ms−Lmcos(2(θe+π/6))

Lbc=Lcb=−Ms−Lmcos(2(θe+π/6−2π/3))

Lca=Lac=−Ms−Lmcos(2(θe+π/6+2π/3))

where:

- *θr* is the rotor mechanical
  angle.
- *θe* is the rotor electrical
  angle.
- *rotor offset* is `0` if you define the
  rotor electrical angle with respect to the *d*-axis, or
  `-pi/2` if you define the rotor electrical angle with
  respect to the *q*-axis.
- *Ls* is the stator self-inductance
  per phase. This value is the average self-inductance of each of the stator
  windings.
- *Lm* is the stator inductance
  fluctuation. This value is the amount the self-inductance and mutual
  inductance fluctuate with the changing of the rotor angle.
- *Ms* is the stator mutual
  inductance. This value is the average mutual inductance between the stator
  windings.

The permanent magnet flux linking winding *a* is a maximum when
*θe* = 0° and zero when
*θe* = 90°. Therefore, the
linked motor flux is defined by:

[ψamψbmψcm]=[ψmcosθeψmcos(θe−2π/3)ψmcos(θe+2π/3)]

where *ψm* is the permanent magnet flux
linkage.

### Simplified Electrical Equations

Applying Park’s transformation to the block electrical equations produces an
expression for torque that is independent of the rotor angle.

Park’s transformation is defined by:

P=2/3[cosθecos(θe−2π/3)cos(θe+2π/3)−sinθe−sin(θe−2π/3)−sin(θe+2π/3)0.50.50.5]

where *θe* is the electrical angle defined
as *Nθr*. *N* is the number
of pole pairs.

Using Park's transformation on the stator winding voltages and currents transforms
them to the dq0 frame, which is independent of the rotor angle:

[vdvqv0]=P[vavbvc]

[idiqi0]=P[iaibic]

Applying Park’s transformation to the first two electrical equations produces
these equations that define the block behavior:

vd=Rsid+Lddiddt−NωiqLq

vq=Rsiq+Lqdiqdt+Nω(idLd+ψm)

v0=Rsi0+L0di0dt

T=32N(iq(idLd+ψm)−idiqLq)

where:

- *Ld* =
  *Ls* +
  *Ms* + 3/2
  *Lm*.
  *Ld* is the stator
  *d*-axis inductance.
- *Lq* =
  *Ls* +
  *Ms* − 3/2
  *Lm*.
  *Lq* is the stator
  *q*-axis inductance.
- *L0* =
  *Ls* –
  2*Ms*.
  *L0* is the stator
  zero-sequence inductance.
- *ω* is the rotor mechanical rotational speed.
- *N* is the number of rotor permanent magnet pole
  pairs.
- *T* is the rotor torque. Torque flows from the motor case
  (block physical port **C**) to the motor rotor (block physical port
  **R**).

The PMSM block uses the original, non-orthogonal
implementation of the Park transform. If you try to apply the alternative
implementation, you get different results for the dq0 voltage and currents.

### Alternative Flux Linkage Parameterization

You can parameterize the motor using the back EMF or torque constants which are
more commonly given on motor datasheets by using the **Permanent magnet flux
linkage** parameter.

The back EMF constant is the peak voltage induced by the permanent magnet in the
per-unit rotational speed of each of the phases. The relationship between the peak
permanent magnet flux linkage and the back EMF is:

ke=Nψm.

The back EMF, *eph*, for one phase
is:

eph=keω.

The torque constant is the peak torque induced by the per-unit current of each of
the phases. It is numerically identical in value to the back EMF constant when both
are expressed in SI units:

kt=Nψm.

When
*Ld*=*Lq*
and the currents in all three phases are balanced, the combined torque
*T* is:

T=32ktiq=32ktIpk,

where *Ipk* is the peak current in any of
the three windings.

The factor 3/2 follows from this being the steady-state sum of the torques from
all phases. Therefore, the torque constant
*kt* can also be:

kt=23(TIpk),

where *T* is the measured total torque when
testing with a balanced three-phase current with peak line voltage
*Ipk*. The RMS line current is:

kt=23Tiline,rms.

### Calculating Iron Losses

Iron losses are divided into two terms, one representing the main magnetizing
path, and the other representing the cross-tooth tip path that becomes active during
field weakened operation. The iron losses model is based on [3].

The term representing the main magnetizing path depends on the induced RMS
line-to-neutral stator voltage, Vmrms:

POC(Vmrms)=ahkVmrms+ajk2Vmrms2+aexk1.5Vmrms1.5.

This is the dominant term during no-load operation. *k* is the
back EMF constant relating RMS volts per Hz. It is defined as k=Vmrms/f, where *f* is the electrical frequency. The first
term on the right-hand side is the magnetic hysteresis loss, the second is the eddy
current loss and the third is the excess loss. The three coefficients appearing on
the numerators are derived from the values that you provide for the open-circuit
hysteresis, eddy, and excess losses.

The term representing the cross-tooth tip path becomes important when a
demagnetizing field is set up and can be determined from a finite element analysis
short-circuit test. It depends on the RMS EMF associated with the cross-tooth tip
flux, Vdrms\*:

PSC(Vdrms\*)=bhkVdrms\*+bjk2Vdrms\*2+bexk1.5Vdrms\*1.5.

The three numerator terms are derived from the values you provide for the
short-circuit hysteresis, eddy, and excess losses.

### Predefined Parameterization

There are multiple available built-in parameterizations for the PMSM block.

This pre-parameterization data allows you to set up the block to represent
components by specific suppliers. The parameterizations of these permanent magnet
synchronous motors match the manufacturer data sheets. To load a predefined
parameterization, double-click the PMSM block, click the **<click to select>** hyperlink of the **Selected
part** parameter and, in the Block Parameterization Manager window,
select the part you want to use from the list of available components.

**Note**

The predefined parameterizations of Simscape components use available data sources for the parameter values. Engineering
judgment and simplifying assumptions are used to fill in for missing data. As a result,
expect deviations between simulated and actual physical behavior. To ensure accuracy,
validate the simulated behavior against experimental data and refine component models as
necessary.

For more information about pre-parameterization and for a list of the available
components, see List of Pre-Parameterized Components.

### Model Thermal Effects

You can expose thermal ports to model the effects of losses that convert power to heat. To
expose the thermal ports, set the **Modeling option** parameter to either:

- `No thermal port` — The block contains expanded
  electrical conserving ports associated with the stator windings, but does not
  contain thermal ports.
- `Show thermal port` — The block contains expanded
  electrical conserving ports associated with the stator windings and thermal
  conserving ports for each of the windings and for the rotor.

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
