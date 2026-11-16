---
type: simulink-block
title: 'Synchronous Machine GENTPJ'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Synchronous'
documentation_page: 'synchronousmachinegentpj'
documentation_source_path: 'ref/synchronousmachinegentpj.html'
language: en
---

# Synchronous Machine GENTPJ

## Ports

### Input

### **Efd** — Per-unit field voltage physical

Physical signal port associated with the per-unit field voltage.
### Output

### **pu** — Machine per-unit measurements physical

Physical signal vector port associated with the machine per-unit measurements. The
vector elements are:

- Field voltage (field circuit base, Efd), *pu\_fd\_Efd*
- Field current (field circuit base, Ifd), *pu\_fd\_Ifd*
- Electrical torque, *pu\_torque*
- Rotor velocity, *pu\_velocity*
- Stator d-axis voltage, *pu\_ed*
- Stator q-axis voltage, *pu\_eq*
- Stator zero-sequence voltage, *pu\_e0*
- Stator d-axis current, *pu\_id*
- Stator q-axis current, *pu\_iq*
- Stator zero-sequence current, *pu\_i0*
- Rotor electrical angle, *electrical\_angle\_out*

To connect to this port, use the Synchronous Machine Measurement
block.
### Conserving

### **R** — Machine rotor mechanical

Mechanical rotational conserving port associated with the machine rotor.

### **C** — Machine case mechanical

Mechanical rotational conserving port associated with the machine case.

### **~** — Stator windings electrical

Expandable three-phase electrical conserving port associated with the stator
windings. For more information, see Three-phase ports.

#### Dependencies

To enable this port, set **Electrical connection** to
`Composite three-phase ports`.

### **a** — *a*-phase electrical

Electrical conserving port associated with the *a*-phase.

#### Dependencies

To enable this port, set **Electrical connection** to
`Expanded three-phase ports`.

### **b** — *b*-phase electrical

Electrical conserving port associated with the *b*-phase.

#### Dependencies

To enable this port, set **Electrical connection** to
`Expanded three-phase ports`.

### **c** — *c*-phase electrical

Electrical conserving port associated with the *c*-phase.

#### Dependencies

To enable this port, set **Electrical connection** to
`Expanded three-phase ports`.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Electrical connection** — Electrical connection `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to have composite or expanded three-phase ports.

### **Rated apparent power** — Rated apparent power `555e6` `A*V` (default)

Rated apparent power.

### **Rated voltage** — RMS rated line-line voltage `24e3` `V` (default)

Root mean square (RMS) of the rated line-line voltage.

### **Rated electrical frequency** — Nominal electrical frequency `60` `Hz` (default)

Nominal electrical frequency at which the block quotes the rated apparent
power.

### **Number of pole pairs** — Number of machine pole pairs `1` (default)

Number of pole pairs of the machine.

### **Rotor angle definition** — Reference point for the rotor angle measurement `Angle between the a-phase magnetic axis and the d-axis` (default) | `Angle between the a-phase magnetic axis and the q-axis`

Reference point for the rotor angle measurement.

When you select the default value, the rotor *d*-axis and stator *a*-phase magnetic axis are aligned when the rotor angle is zero.

The other value you can choose for this parameter is `Angle between the a-phase magnetic axis and the q-axis`. When you select this value, the rotor *q*-axis and stator *a*-phase magnetic axis are aligned when the rotor angle is zero.

### Impedances

### **Stator resistance, Ra** — Resistance of stator `0.003` (default) | positive scalar

Resistance of the stator.

### **Stator leakage reactance, Xl** — Leakage reactance of stator `0.15` (default) | positive scalar

Leakage reactance of the stator.

### **d-axis synchronous reactance, Xd** — *d*-axis synchronous reactance `1.81` (default) | positive scalar

*d*-axis synchronous reactance.

### **q-axis synchronous reactance, Xq** — *q*-axis synchronous reactance `1.76` (default) | positive scalar

*q*-axis synchronous reactance.

### **d-axis transient reactance, Xd'** — *d*-axis transient reactance `0.3` (default) | positive scalar

*d*-axis transient reactance.

### **q-axis transient reactance, Xq'** — *q*-axis transient reactance `0.65` (default) | positive scalar

*q*-axis transient reactance.

### **d-axis subtransient reactance, Xd''** — *d*-axis subtransient reactance `0.23` (default) | positive scalar

*d*-axis subtransient reactance.

### **q-axis subtransient reactance, Xq''** — *q*-axis subtransient reactance `0.25` (default) | positive scalar

*q*-axis subtransient reactance.

### Time Constants

### **d-axis transient open-circuit, Td0'** — *d*-axis transient open-circuit `8` `s` (default) | positive scalar

*d*-axis transient open-circuit time constant. This parameter
value must be:

- Greater than 0
- Greater than **d-axis subtransient open-circuit,
  Td0''**

### **d-axis subtransient open-circuit, Td0''** — *d*-axis subtransient open-circuit `0.03` `s` (default) | positive scalar

*d*-axis subtransient open-circuit time constant.

### **q-axis transient open-circuit, Tq0'** — *q*-axis transient open-circuit `1` `s` (default) | positive scalar

*q*-axis transient open-circuit time constant. This parameter
value must be:

- Greater than 0
- Greater than **q-axis subtransient open-circuit,
  Tq0''**

### **q-axis subtransient open-circuit, Tq0''** — *q*-axis subtransient open-circuit `0.07` `s` (default) | positive scalar

*q*-axis subtransient open-circuit time constant.

### Saturation

### **Magnetic saturation representation** — Magnetic saturation representation `None` (default) | `Quadratic` | `Scaled quadratic` | `Exponential` | `Open-circuit lookup table`

Option to represent the magnetic saturation of the block:

- `None` — The block does not model the magnetic
  saturation.
- `Quadratic` — The block models the magnetic
  saturation by using a quadratic function.
- `Scaled quadratic` — The block models the magnetic
  saturation by using a scaled function.
- `Exponential` — The block models the magnetic
  saturation by using an exponential function.
- `Open-circuit lookup table` — The block models the
  magnetic saturation by using per-unit non-reciprocal field current and per-unit
  air-gap voltage saturation data.

### **Saturation factor, S10** — Saturation factor, S10 `0.005` (default) | positive scalar

Saturation factor that corresponds to 1.0 per-unit terminal voltage.

#### Dependencies

To enable this parameter, set **Magnetic saturation
representation** to `Quadratic`,
`Scaled quadratic`, or
`Exponential`.

### **Saturation factor, S12** — Saturation factor, S12 `0.08` (default) | positive scalar

Saturation factor that corresponds to 1.2 per-unit terminal voltage. The value of
this parameter must be greater than the value of the **Saturation factor,
S10** parameter.

#### Dependencies

To enable this parameter, set **Magnetic saturation
representation** to `Quadratic`,
`Scaled quadratic`, or
`Exponential`.

### **Non-reciprocal per-unit field current saturation data, ifd** — Per-unit field current saturation data `[0, .8, 1.26, 2.29, 2.97]` (default) | vector of nonnegative values

Nonreciprocal field current, *ifd*, data
that populates the air-gap voltage, *Vag*,
versus field current, *ifd*, lookup table.
This parameter value must contain a vector with at least five elements.

#### Dependencies

To enable this parameter, set **Magnetic saturation
representation** to `Open-circuit lookup
table`.

### **Per-unit air-gap voltage saturation data, Vag** — Per-unit air-gap voltage saturation data `[0, .8, 1.08, 1.31, 1.4]` (default) | vector of nonnegative values

Air-gap voltage, *Vag*, data that
populates the air-gap voltage, *Vag*, versus
field current, *ifd*, lookup table. This
parameter value must contain a vector with at least five elements.

#### Dependencies

To enable this parameter, set **Magnetic saturation
representation** to `Open-circuit lookup
table`.

### **Kis** — Effect of stator current on saturation `0.05` (default) | nonnegative scalar

Effect of the stator current on the saturation. The block uses the value of this
parameter to calculate the *d*-axis and *q*-axis
saturation factors.

### Initial Conditions

### **Initialization option** — Option for specifying values at start of simulation `Set real power, reactive power, terminal voltage, and terminal phase` (default) | `Set targets for rotor angle and Park's transform variables` | `Set targets for load flow variables`

Option for specifying values for certain parameters and variables at the start of simulation:

- `Set real power, reactive power, terminal voltage, and terminal
  phase` — Set an operating point regardless of the connected
  network.
- `Set targets for rotor angle and Park's transform
  variables` — Specify the priority and initial target values for
  block variables before simulation using the **Variables**
  settings. For more information, see Set Priority and Initial Target for Block Variables.
- `Set targets for load flow variables` — Select a
  bus type and specify the related parameters for a load-flow analysis in the
  **Initial Conditions** settings.

### **Source type** — Voltage source model `Swing bus` (default) | `PV bus` | `PQ bus`

Type of voltage source that the block models.

#### Dependencies

To enable this parameter, set **Initialization option** to
`Set targets for load flow variables`.

### **Terminal voltage magnitude** — Terminal voltage magnitude `24e3` `V` (default) | positive scalar

Terminal voltage magnitude.

#### Dependencies

To enable this parameter, set **Initialization option** to
`Set real power, reactive power, terminal voltage, and terminal
phase`. Alternatively, set **Initialization option**
to `Set targets for load flow variables` and
**Source type** to `Swing bus` or
`PV bus`.

### **Terminal voltage angle** — Terminal voltage angle `0` `deg` (default) | scalar

Terminal voltage angle.

#### Dependencies

To enable this parameter, set **Initialization option** to
`Set real power, reactive power, terminal voltage, and terminal
phase`. Alternatively, set **Initialization option**
to `Set targets for load flow variables` and
**Source type** to `Swing bus`.

### **Active power generated** — Generated active power `500e6` `V*A` (default) | scalar

Active power that the machine generates.

#### Dependencies

To enable this parameter, set **Initialization option** to
`Set real power, reactive power, terminal voltage, and terminal
phase`. Alternatively, set **Initialization option**
to `Set targets for load flow variables` and
**Source type** to `PV bus` or
`PQ bus`.

### **Reactive power generated** — Generated reactive power `0` `V*A` (default) | scalar

Reactive power that the machine generates.

#### Dependencies

To enable this parameter, set **Initialization option** to
`Set real power, reactive power, terminal voltage, and terminal
phase`. Alternatively, set **Initialization option**
to `Set targets for load flow variables` and
**Source type** to `PQ bus`.

### **Minimum terminal voltage magnitude (pu)** — Minimum terminal voltage magnitude `0.95` (default) | positive scalar

Per-unit minimum steady-state voltage magnitude.

#### Dependencies

To enable this parameter, set **Initialization option** to
`Set targets for load flow variables` and
**Source type** to `PQ bus`.

### **Phase search range at terminals** — Phase search range at terminals `[-inf, inf]` `deg` (default) | vector of two elements

Vector that defines the search range of the phase angle at the terminals.

#### Dependencies

To enable this parameter, set **Initialization option** to
`Set targets for load flow variables` and
**Source type** to `PV bus` or
`PQ bus`.

### **Parasitic conductance to electrical reference** — Parasitic conductance to electrical reference `1e-6` `S` (default) | positive scalar

Parasitic conductance to the electrical reference.

#### Dependencies

To enable this parameter, set **Initialization option** to
`Set targets for load flow variables`.

## Libraries

Simscape / Electrical / Electromechanical / Synchronous

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

## Description

GENTPJ synchronous machine

The Synchronous Machine GENTPJ block models a GENTPJ
synchronous generator model. GENTPJ synchronous generator models are widely used in power
plant model verification and power system transient stability studies.

### Synchronous Machine Initialization Using Load-Flow Target Values

If the block is in a network that is compatible with the
frequency-time simulation mode, you can perform a load-flow analysis on the network. A
load-flow analysis provides steady-state values that you can use to initialize the
machine.

For more information, see Perform a Load-Flow Analysis Using Simscape Electrical and Frequency and Time Simulation Mode. For an example that shows how to initialize
a synchronous machine using data from a load-flow analysis, see Synchronous Machine Initialization with Loadflow.

### Equations

The synchronous machine equations are expressed with respect to a rotating reference
frame,

θe(t)=Nθr(t),

where:

- *θe* is the electrical angle.
- *N* is the number of pole pairs.
- *θr* is the rotor angle.

The Park transformation maps the synchronous machine equations to the rotating reference
frame with respect to the electrical angle. This equation defines the Park
transformation:

Ps=23[cosθecos(θe−2π3)cos(θe+2π3)−sinθe−sin(θe−2π3)−sin(θe+2π3)121212].

The block uses the Park transformation to define the per-unit synchronous machine
equations. These equations define the *d*-axis and
*q*-axis stator voltages:

vd=ed''ωr−Raid+(Xq''−Xl1+Sq+Xl)iqvq=eq''ωr−Raiq−(Xd''−Xl1+Sd+Xl)id

In these equations:

- *e''d* is the
  *d*-axis voltage behind the subtransient reactance.
- *Ra* is the stator resistance.
- *id* is the *d*-axis
  stator current.
- *X''q* is the
  *q*-axis subtransient reactance.
- *Xl* is the stator leakage
  reactance.
- *Sq* is the *q*-axis
  saturation factor.
- *iq* is the *q*-axis
  stator current.
- *e''q* is the
  *q*-axis voltage behind the subtransient reactance.
- *X''d* is the
  *d*-axis subtransient reactance.
- *Sd* is the *d*-axis
  saturation factor.

These equations define the voltages behind the transient reactances:

de″ddt=1T″q0[(1+Sq)(e′d−e″d)+iq(X′q−X″q)]de″qdt=1T″d0[(1+Sd)(e′q−e″q)−id(X′d−X″d)]de′ddt=1+SqT′q0(e″dXq−X′qX′q−X″q−e′dXq−X″qX′q−X″q)de′qdt=EfdT′d0+1+SdT′d0(e″qXd−X′dX′d−X″d−e′qXd−X″dX′d−X″d)

In these equations:

- *e'd* is the
  *d*-axis voltage behind the transient reactance.
- *e'q* is the
  *q*-axis voltage behind the transient reactance.
- *T'd0* is the
  *d*-axis transient open-circuit time constant.
- *T'q0* is the
  *q*-axis transient open-circuit time constant.
- *T''d0* is the
  *d*-axis subtransient open-circuit time constant.
- *T''q0* is the
  *q*-axis subtransient open-circuit time constant.
- *X'd* is the
  *d*-axis transient reactance.
- *X'q* is the
  *q*-axis transient reactance.
- *Efd* is the per-unit field
  voltage.

These equations define the machine saturations,

ψad=vq+Raiq+Xlidψaq=vd+Raid−Xliqψat=ψad2+ψaq2Sd=f(ψat+Kisid2+iq2)Sq=XqXdf(ψat+Kisid2+iq2)

where:

- *ψad* is the *d*-axis
  air-gap flux linkage.
- *ψaq* is the *q*-axis
  air-gap flux linkage.
- *ψat* is the air-gap flux linkage.
- *Kis* represents the effect of the stator
  current on the saturation.
- *Sd* and
  *Sq* are the *d*-axis and
  *q*-axis saturation factors, respectively. If you set the
  **Magnetic saturation representation** parameter to
  `None`, *Sd* and
  *Sq* are equal to zero. If you set the
  **Magnetic saturation representation** parameter to
  `Quadratic`, `Scaled quadratic`,
  or `Exponential`, the block calculates the saturation factor
  function, *f*, from the value of the **Saturation factor,
  S10** and **Saturation factor, S12** parameters. If you
  set the **Magnetic saturation representation** parameter to
  `Open-circuit lookup table`, the block calculates the
  saturation factor function, *f*, from the per-unit field current and
  air-gap voltage saturation data.

This equation defines the per-unit field current in a non-reciprocal per-unit system:

Ifd=(1+Sd)(e′qXd−X″dX′d−X″d−e″qXd−X′dX′d−X″d).

This equation defines the rotor torque:

Te=e″did+e″qiq−(X″d−Xl1+Sd−X″q−Xl1+Sq)idiq.

### Plotting and Display Options

You can perform plotting and display actions using the
**Electrical** menu on the block context menu.

Right-click the block. From the **Electrical** menu, select an option:

- **Display Base Values** — Display the machine per-unit base
  values in the MATLAB® Command Window.
- **Display Associated Initial Conditions** — Display
  associated initial conditions in the MATLAB Command Window.
- **Plot Open-Circuit Saturation (pu)** — Plot air-gap voltage,
  *Vag*, versus field current,
  *ifd*, both measured in per-unit, in a
  MATLAB figure window. The plot contains two traces:

  - Unsaturated — **Stator d-axis mutual inductance (unsaturated),
    Ladu** that you specify
  - Saturated — **Per-unit open-circuit lookup table (Vag versus
    ifd)** that you specify
- **Plot Saturation Factor (pu)** — Plot the saturation factor,
  *f*, versus magnetic flux linkage,
  *ψat*, both measured in per-unit, in a
  MATLAB figure window using the machine parameters. If you set the
  **Magnetic saturation representation** parameter to
  `Quadratic`, `Scaled quadratic`, or
  `Exponential`, the block derives the saturation factor
  function from the value of the **Saturation factor, S10** and
  **Saturation factor, S12** parameters.

  If you set the **Magnetic saturation representation** to
  `Open-circuit lookup table`, the block derives the saturation
  factor function from the value of the **Non-reciprocal per-unit field current
  saturation data, ifd**  and **Per-unit air-gap voltage saturation
  data, Vag** parameters.
- **Plot Power Capability Curves** — Plot active power P versus
  reactive power Q, both measured in per-unit, in a MATLAB figure window. The plot can contain multiple traces. Each trace
  corresponds to a maximum field circuit voltage measured per unit (non-reciprocal
  per-unit system). The plot shows the maximum reactive power that the generator produces
  when operating with a lagging power factor and the minimum reactive power that the
  generator absorbs when operating with a leading power factor.

### Variables

To set the priority and initial target values for the block variables prior to simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

For this block, the **Initial Targets** settings are visible only if, in
the **Initial Conditions** section, you set the **Initialization
option** parameter to `Set targets for rotor angle and Park's
transform variables`.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
