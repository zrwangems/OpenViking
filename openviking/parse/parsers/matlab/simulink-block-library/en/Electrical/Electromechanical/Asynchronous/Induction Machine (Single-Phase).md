---
type: simulink-block
title: 'Induction Machine (Single-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Asynchronous'
documentation_page: 'inductionmachinesinglephase'
documentation_source_path: 'ref/inductionmachinesinglephase.html'
language: en
---

# Induction Machine (Single-Phase)

## Ports

### Output

### **pu** — Machine per-unit measurements physical signal | vector

Physical signal vector port associated with the machine per-unit
measurements. The vector elements are:

- pu\_torque
- pu\_velocity
- pu\_vds
- pu\_vqs
- pu\_v0s = 0
- pu\_ids
- pu\_iqs
- pu\_i0s = 0
### Conserving

### **a1** — Main winding positive terminal electrical | scalar

Electrical conserving port associated with the main winding positive
terminal.

### **a2** — Main winding negative terminal electrical | scalar

Electrical conserving port associated with the main winding negative
terminal.

### **b1** — Auxiliary winding positive terminal electrical | scalar

Electrical conserving port associated with the auxiliary winding
positive terminal.

#### Dependencies

This port is visible only if you set the **Type** to `Main
and auxiliary windings`.

### **b2** — Auxiliary winding negative terminal electrical | scalar

Electrical conserving port associated with the auxiliary winding
negative terminal.

#### Dependencies

This port is visible only if you set the **Type** to `Main
and auxiliary windings`.

### **R** — Machine rotor mechanical rotational

Mechanical rotational conserving port associated with the machine
rotor.

### **C** — Machine case mechanical rotational

Mechanical rotational conserving port associated with the machine
case.

### **HA** — Main winding thermal port thermal

Thermal conserving port associated with stator main winding.

#### Dependencies

To enable this port, set **Modeling option** to `Show
thermal port`.

### **HB** — Auxiliary winding thermal port thermal

Thermal conserving port associated with stator auxiliary
winding.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

### **HR** — Rotor thermal port thermal

Thermal conserving port associated with the rotor.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

## Parameters

### **Modeling option** — Whether to enable thermal ports `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal ports of the block and model the effects of generated heat and motor temperature.

### Main

### **Type** — Induction machine type `Split-phase` (default) | `Capacitor-start` | `Capacitor-start-capacitor-run` | `Main and auxiliary windings`

Type of induction machine.

### **Rated apparent power** — Rated apparent power `180` `V*A` (default) | positive scalar

Rated apparent power of the induction machine.

### **Rated voltage** — Rated voltage `220` `V` (default) | positive scalar

RMS voltage.

### **Rated electrical frequency** — Rated electrical frequency `60` `Hz` (default) | positive scalar

Nominal electrical frequency corresponding to the rated apparent
power.

### **Number of pole pairs** — Number of pole pairs `2` (default) | positive integer

Number of machine pole pairs. The value is used as a
back-electromotive force constant.

### **Parameterization unit** — SI or per-unit parameterization option `SI` (default) | `Per unit`

Unit system for block parameterization.

#### Dependencies

Selecting:

- `SI` exposes SI
  **Electrical** parameters.
- `Per unit` exposes per-unit
  **Electrical** parameters.

### Electrical

For the **Parameterization unit** parameter in the
**Main** settings, select `SI` to
expose the SI **Electrical** parameters, or `Per
unit` to expose the per-unit **Electrical**
parameters.

### **Main winding stator resistance, Ras** — Main winding stator resistance `1.8180` `Ohm` (default) | positive scalar

SI stator resistance for the main winding.

#### Dependencies

Selecting `SI` for the
**Parameterization unit** parameter in the
**Main** settings exposes SI
**Electrical** parameters.

### **Main winding stator leakage inductance, Llas** — Main winding stator leakage inductance `0.0067` `H` (default) | positive scalar

SI leakage inductance for the main winding.

#### Dependencies

Selecting `SI` for the
**Parameterization unit** parameter in the
**Main** settings exposes SI
**Electrical** parameters.

### **Main winding rotor resistance, Rar'** — Main winding rotor resistance `3.7080` `Ohm` (default) | positive scalar

SI rotor resistance for the main winding.

#### Dependencies

Selecting `SI` for the
**Parameterization unit** parameter in the
**Main** settings exposes SI
**Electrical** parameters.

### **Main winding rotor leakage inductance, Llar'** — Main winding rotor leakage inductance `0.0050` `H` (default) | positive scalar

SI rotor leakage inductance for the main winding.

#### Dependencies

Selecting `SI` for the
**Parameterization unit** parameter in the
**Main** settings exposes SI
**Electrical** parameters.

### **Main winding mutual inductance, Lms** — Main winding mutual inductance `0.1595` `H` (default) | positive scalar

SI mutual inductance for the main winding.

#### Dependencies

Selecting `SI` for the
**Parameterization unit** parameter in the
**Main** settings exposes SI
**Electrical** parameters.

### **Auxiliary winding stator resistance, Rbs** — Auxiliary winding stator resistance `6.4260` `Ohm` (default) | positive scalar

SI stator resistance for the auxiliary winding.

#### Dependencies

Selecting `SI` for the
**Parameterization unit** parameter in the
**Main** settings exposes SI
**Electrical** parameters.

### **Auxiliary winding stator leakage inductance, Llbs** — Auxiliary winding stator leakage inductance `0.0077` `H` (default) | positive scalar

SI stator leakage inductance for the auxiliary winding.

#### Dependencies

Selecting `SI` for the
**Parameterization unit** parameter in the
**Main** settings exposes SI
**Electrical** parameters.

### **Auxiliary/main windings turn ratio** — Turn ratio `1.1` (default) | positive scalar

Winding ratio between the main and auxiliary winding.

### **Main winding stator resistance, Ras (pu)** — Main winding stator resistance `0.0135` (default) | positive scalar

Per-unit stator resistance for the main winding.

#### Dependencies

Selecting `Per unit` for the
**Parameterization unit** parameter in the
**Main** settings exposes per-unit
**Electrical** parameters.

### **Main winding stator leakage inductance, Llas (pu)** — Main winding stator leakage inductance `0.0188` (default) | positive scalar

Per-unit leakage inductance for the main winding.

#### Dependencies

Selecting `Per unit` for the
**Parameterization unit** parameter in the
**Main** settings exposes per-unit
**Electrical** parameters.

### **Main winding rotor resistance, Rar' (pu)** — Main winding rotor resistance `0.0276` (default) | positive scalar

Per-unit rotor resistance for the main winding.

#### Dependencies

Selecting `Per unit` for the
**Parameterization unit** parameter in the
**Main** settings exposes per-unit
**Electrical** parameters.

### **Main winding rotor leakage inductance, Llar' (pu)** — Main winding rotor leakage inductance `0.0140` (default) | positive scalar

Per-unit rotor leakage inductance for the main winding.

#### Dependencies

Selecting `Per unit` for the
**Parameterization unit** parameter in the
**Main** settings exposes per-unit
**Electrical** parameters.

### **Main winding mutual inductance, Lms (pu)** — Main winding mutual inductance `0.4472` (default) | positive scalar

Per-unit mutual inductance for the main winding.

#### Dependencies

Selecting `Per unit` for the
**Parameterization unit** parameter in the
**Main** settings exposes per-unit
**Electrical** parameters.

### **Auxiliary winding stator resistance, Rbs (pu)** — Auxiliary winding stator resistance `0.0478` (default) | positive scalar

Per-unit stator resistance for the auxiliary winding.

#### Dependencies

Selecting `Per unit` for the
**Parameterization unit** parameter in the
**Main** settings exposes per-unit
**Electrical** parameters.

### **Auxiliary winding stator leakage inductance, Llbs (pu)** — Auxiliary winding stator leakage inductance `0.0216` (default) | positive scalar

Per-unit stator leakage inductance for the auxiliary winding.

#### Dependencies

Selecting `Per unit` for the
**Parameterization unit** parameter in the
**Main** settings exposes per-unit
**Electrical** parameters.

### **Auxiliary/main windings turn ratio** — Turn ratio `1.1` (default) | positive scalar

Winding ratio between the main and auxiliary winding.

### **Capacitor-start resistance, Rs** — Capacitor-start resistance `3` `Ohm` (default) | positive scalar

SI capacitor-start resistance.

#### Dependencies

To enable this parameter, set **Type** to either
`Capacitor-start-capacitor-run` or
`Capacitor-start` and
**Parameterization unit** to
`SI`.

### **Capacitor-start capacitance, Cs** — Capacitor-start capacitance `0.00018` `F` (default) | positive scalar

SI capacitor-start capacitance.

#### Dependencies

To enable this parameter, set **Type** to either
`Capacitor-start-capacitor-run` or
`Capacitor-start` and
**Parameterization unit** to
`SI`.

### **Capacitor-run resistance, Rr** — Capacitor-run resistance `9` `Ohm` (default) | positive scalar

SI capacitor-run resistance.

#### Dependencies

To enable this parameter, set **Type** to
`Capacitor-start-capacitor-run` and
**Parameterization unit** to
`SI`.

### **Capacitor-run capacitance, Cr** — Capacitor-run capacitance `0.000015` `F` (default) | positive scalar

SI capacitor-run capacitance.

#### Dependencies

To enable this parameter, set **Type** to
`Capacitor-start-capacitor-run` and
**Parameterization unit** to
`SI`.

### **Capacitor-start resistance, Rs (pu)** — Capacitor-start resistance `0.0223` (default) | positive scalar

Per-unit capacitor-start resistance.

#### Dependencies

To enable this parameter, set **Type** to
`Capacitor-start-capacitor-run` and
**Parameterization unit** to `Per
unit`.

### **Capacitor-start capacitance, Cs (pu)** — Capacitor-start capacitance `9.1232` (default) | positive scalar

Per-unit capacitor-start capacitance.

#### Dependencies

To enable this parameter, set **Type** to
`Capacitor-start-capacitor-run` and
**Parameterization unit** to `Per
unit`.

### **Capacitor-run resistance, Rr (pu)** — Capacitor-run resistance `0.0669` (default) | positive scalar

Per-unit capacitor-run resistance.

#### Dependencies

To enable this parameter, set **Type** to
`Capacitor-start-capacitor-run` and
**Parameterization unit** to `Per
unit`.

### **Capacitor-run resistance, Cr (pu)** — Capacitor-run capacitance `0.000015` (default) | positive scalar

Per-unit capacitor-run capacitance.

#### Dependencies

To enable this parameter, set **Type** to
`Capacitor-start-capacitor-run` and
**Parameterization unit** to `Per
unit`.

### **Disconnection speed (% of rated speed)** — Disconnection speed `80` (default) | scalar in range [0,100]

Speed when capacitor is disconnected, expressed as a percentage of
rated speed. The value must be between `0` and
`100`, inclusive.

#### Dependencies

To enable this parameter, set **Type** to either
`Split-phase`,
`Capacitor-start`, or
`Capacitor-start-capacitor-run`.

### Mechanical

### **Rotor inertia** — Rotor inertia `0.01` `kg*m^2` (default) | positive scalar

Inertia of the rotor.

### **Rotor damping** — Rotor damping `0` `N*m/(rad/s)` (default) | scalar

Damping of the rotor.

### Thermal

These parameters appear only for blocks with exposed thermal ports.

### **Measurement temperature** — Rated temperature `298.15` `K` (default) | real scalar

Temperature for which motor parameters are quoted.

### **Resistance temperature coefficient** — Temperature coefficient `3.93e-3` `1/K` (default) | positive scalar

Coefficient α in the equation relating resistance to temperature for
all three windings, as described in Thermal Model for Actuator Blocks. The default value,
`3.93e-3` 1/K, is for copper.

### **Cage resistance temperature coefficient** — Rotor temperature coefficient `4.4e-3` (default) | `1/K` | scalar

Coefficient relating cage resistance to temperature for the rotor. The
default value, `4.4e-3` 1/K, is for aluminium.

### **Thermal mass for each stator winding** — Winding thermal mass `100` `J/K` (default) | positive scalar

Thermal mass value for each stator winding. The thermal mass is the
energy required to raise the temperature by one degree.

### **Rotor thermal mass** — Rotor thermal mass `200` `J/K` (default) | positive scalar

Thermal mass of the rotor. The thermal mass is the energy required to
raise the temperature of the rotor by one degree.

## Libraries

Simscape / Electrical / Electromechanical / Asynchronous

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

### R2021b: Induction machine type parameter

From R2021b forward, to model the different types of induction machine, set the
**Type** parameter to either
`Split-phase`,
`Capacitor-start`,
`Capacitor-start-capacitor-run`, or `Main
and auxiliary windings`.

As a result of these changes, inside a model saved in an earlier release, review
the **Type** parameter of this block.

## Description

Single-phase induction machine with SI or pu fundamental parameterization

The Induction Machine (Single-Phase) block represents a
single-phase induction machine with a squirrel cage rotor with fundamental parameters
expressed in per-unit or in the International System of Units (SI).

This block models four types of single-phase induction machines:

- `Split-phase`
- `Capacitor-start`
- `Capacitor-start-capacitor-run`
- `Main and auxiliary windings`

The single phase induction machine consists of a squirrel cage rotor and two stator
windings, the main and the auxiliary windings. The auxiliary winding is typically only
active during startup. However, to improve performance, the auxiliary winding can be
active during running for low-power applications. The figure shows the equivalent
*d*- and *q*-axis circuits for the main and
auxiliary windings.

The table defines the variables.

| Variable | Definition |
| --- | --- |
| *vqs**vds* | Stator voltages in the *d*-*q* representation |
| *iqs**ids* | Stator currents in the *d*-*q* representation |
| *Ψqr**Ψdr* | Rotor fluxes in the *d*-*q* representation |
| *⍵* | Rotor electrical speed |
| *a* | Auxiliary/main windings turn ratio |
| *Ras* | Main winding stator resistance |
| *Las* | Main winding stator leakage inductance |
| *R'ar* | Main winding rotor resistance |
| *L'lar* | Main winding rotor leakage inductance |
| *Lmas* | Main winding mutual inductance |
| *Rbs* | Auxiliary winding stator resistance |
| *Rlbs* | Auxiliary winding stator leakage inductance |
| *R'br* | Auxiliary winding rotor resistance |
| *L'lbr* | Auxiliary winding rotor leakage inductance |
| *Lmbs* | Auxiliary winding mutual inductance |

### Equations

The SI model converts the SI values that you enter in the dialog box to per-unit
values for simulation. For information on the relationship between SI and per-unit
machine parameters, see Per-Unit Conversion for Machine Parameters. For information on per-unit parameterization, see Per-Unit System of Units.

These transformations reduce the rotor resistance, rotor leakage inductance, and
stator mutual inductance to a single set of values by defining the equivalent
circuits with respect to the main winding:

Lms=Lmas=1a2Lmbs

Rar'=1a2Rbr'

Llar'=1a2Llbr'

The voltage equations for the stator and rotor are:

vqs=Rasiqs+dψqsdt

vds=Rbsids+dψdsdt

0=Rar'iqr'+dψqr'dt−1aωrψdr'

0=a2Rar'idr'+dψdr'dt+aωrψqr'

ψqs=(Llas+Lms)iqs+Lmsiqr'

ψds=(Llbs+a2Lms)ids+a2Lmsidr'

ψqr'=(Llar'+Lms)iqr'+Lmsiqs

ψdr'=a2(Llar'+Lms)idr'+a2Lmsids

The expression for the electromagnetic torque, *T*, is obtained
by applying the principle of virtual displacement [1].

T=p(aψqr'idr'−1aψdr'iqr')

The mechanical equation is

Jdωmdt=T−TL−Bmωm,

where *ωm* is the rotor
angular velocity.

In split-phase machines, the auxiliary winding is displaced at 90 electrical
degrees from the main winding and operates only until the speed reaches the
disconnection speed, which is typically 70 to 80 percent of rated speed. In this
configuration, the auxiliary winding has high resistance and small reactance
compared to the main winding. The resulting phase difference makes the machine
behave like a two-phase machine.

The capacitor-start machine is a type of split-phase machine that uses a capacitor
in series with the auxiliary winding to start the machine. In this configuration,
auxiliary and main windings have the same number of turns. The value of the
capacitor ensures that the current in the auxiliary coil leads the current in the
main winding by approximately 80 electrical degrees.

The capacitor-start voltage is:

vc=Rsids+∫​1Csωrids.

When a capacitor is connected in series with the auxiliary winding, the voltage
equation for the *d*-axis is

vds=Rbsids+dψdsdt−Rsids−∫​1Csωrids.

The extension is obtained immediately for capacitor-start-capacitor-run machines.
In this configuration, two capacitors are connected in parallel.

The *d*-axis voltage after disconnecting the capacitor-start is

vds=Rbsids+dψdsdt−Rrids−∫​1Crωrids.

### Display Option

To display the machine per-unit base values in the MATLAB® Command Window, right-click the block and, from the
**Electrical** menu, select **Display Base
Values**.

### Model Thermal Effects

You can expose thermal ports to simulate the effects of generated heat and motor temperature. To expose the thermal ports and the **Thermal** parameters, set the **Modeling option** parameter to either:

- `No thermal port` — The block contains electrical conserving ports associated with the stator windings, but does not contain thermal ports.
- `Show thermal port` — The block contains expanded electrical conserving ports associated with the stator windings and thermal conserving ports for each of the windings and for the rotor.

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
