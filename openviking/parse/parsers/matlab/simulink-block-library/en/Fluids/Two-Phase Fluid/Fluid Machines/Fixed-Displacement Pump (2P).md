---
type: simulink-block
title: 'Fixed-Displacement Pump (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Fluid Machines'
documentation_page: 'fixeddisplacementpump2p'
documentation_source_path: 'ref/fixeddisplacementpump2p.html'
language: en
---

# Fixed-Displacement Pump (2P)

## Ports
```yaml
ports:
- name: EV
  summary: Volumetric efficiency, unitless physical signal
  direction: input
- name: EM
  summary: Mechanical efficiency, unitless physical signal
  direction: input
- name: LV
  summary: Volumetric loss, m^3/s physical signal
  direction: input
- name: LM
  summary: Mechanical loss, N\*m physical signal
  direction: input
- name: A
  summary: Pump inlet two-phase fluid
  direction: conserving
- name: B
  summary: Pump outlet two-phase fluid
  direction: conserving
- name: C
  summary: Pump case mechanical rotational
  direction: conserving
- name: R
  summary: Pump shaft mechanical rotational
  direction: conserving
```

### Input

### **EV** — Volumetric efficiency, unitless physical signal

Physical signal input port for the volumetric efficiency coefficient. The input
signal has an upper bound at the **Maximum volumetric efficiency**
parameter value and a lower bound at the **Minimum volumetric
efficiency** parameter value.

#### Dependencies

To enable this port, set **Leakage and friction
parameterization** to `Input signal - volumetric and
mechanical efficiencies`.

### **EM** — Mechanical efficiency, unitless physical signal

Physical signal input port for the mechanical efficiency coefficient. The input
signal has an upper bound at the **Maximum mechanical efficiency**
parameter value and a lower bound at the **Minimum mechanical
efficiency** parameter value.

#### Dependencies

To enable this port, set **Leakage and friction
parameterization** to `Input signal - volumetric and
mechanical efficiencies`.

### **LV** — Volumetric loss, m^3/s physical signal

Physical signal input port for the volumetric loss which is the internal leakage
flow rate between the pump inlets.

#### Dependencies

To enable this port, set **Leakage and friction
parameterization** to `Input signal - volumetric and
mechanical losses`.

### **LM** — Mechanical loss, N\*m physical signal

Physical signal input port for the mechanical loss which is the friction torque on
the rotating pump shaft.

#### Dependencies

To enable this port, set **Leakage and friction
parameterization** to `Input signal - volumetric and
mechanical losses`.
### Conserving

### **A** — Pump inlet two-phase fluid

Two-phase fluid conserving port associated with the pump inlet.

### **B** — Pump outlet two-phase fluid

Two-phase fluid conserving port associated with the pump outlet.

### **C** — Pump case mechanical rotational

Mechanical rotational conserving port associated with the pump case.

### **R** — Pump shaft mechanical rotational

Mechanical rotational conserving port associated with the rotational pump
shaft.
## Parameters
```yaml
parameters:
- name: Leakage and friction parameterization
  summary: Parameterization of leakage flow rate and friction torque Analytical (default) | Tabulated data - volumetric and
    mechanical efficiencies | Tabulated data - volumetric and mechanical losses | Input signal - volumetric and mechanical
    efficiencies | Input signal - volumetric and mechanical losses
  group: Parameters
- name: Displacement
  summary: Fluid volume displaced per shaft rotation 30 cm^3/rev (default) | positive scalar
  group: Parameters
- name: Nominal shaft angular velocity
  summary: Shaft angular velocity for given volumetric efficiency 1800 rpm (default) | scalar
  group: Parameters
- name: Nominal pressure gain
  summary: Pressure gain for corresponding volumetric efficiency 10 MPa (default) | scalar
  group: Parameters
- name: Nominal dynamic viscosity
  summary: Dynamic viscosity at which to specify the volumetric efficiency 0.9 cP (default) | scalar
  group: Parameters
- name: Volumetric efficiency at nominal conditions
  summary: Volumetric efficiency at specified nominal conditions 0.92 (default) | positive scalar
  group: Parameters
- name: Mechanical efficiency at nominal conditions
  summary: Ratio of ideal-to-actual mechanical power 0.88 (default) | positive scalar
  group: Parameters
- name: No-load torque
  summary: Minimum torque required to induce shaft rotation 0 N*m (default) | scalar
  group: Parameters
- name: Pressure gain vector, dp
  summary: Pressure gains for given volumetric and mechanical efficiencies or losses [.1, 1, 2] MPa (default) | vector
  group: Parameters
- name: Shaft angular velocity vector, w
  summary: Angular velocities at which to specify volumetric and mechanical efficiencies or losses [250, 500, 1000, 2000,
    3000, 4000] rpm (default) | vector
  group: Parameters
- name: Volumetric efficiency table, e_v(dp,w)
  summary: Volumetric efficiencies for given pressure gains and angular velocities [.816, .908, .954, .977, .981, .984; .325,
    .663, .831, .916, .925, .946; .137, .568, .78, .892, .893, .91] (default) | matrix
  group: Parameters
- name: Mechanical efficiency table, e_m(dp,w)
  summary: Mechanical efficiencies for given pressure gains and angular velocities [.996, .996, .996, .996, .996, .996; .988,
    .989, .989, .989, .989, .99; .981, .981, .982, .982, .983, .984] (default) | matrix
  group: Parameters
- name: Volumetric loss table, q_loss(dp,w)
  summary: Internal leakage flow rates for corresponding pressure gains and angular velocities [.023, .023, .023, .023, .0285,
    .032; .0844, .0842, .0845, .084, .1125, .108; .1079, .108, .11, .108, .1605, .18] * 1e-3 m^3/s (default) | matrix
  group: Parameters
- name: Mechanical loss table, torque_loss(dp,w)
  summary: Friction torques for corresponding pressure gains and angular velocities [.002, .002, .002, .002, .002, .002; .0607,
    .0556, .0556, .0556, .0556, .0505; .1937, .1937, .1833, .1833, .1729, .1626] N*m (default) | matrix
  group: Parameters
- name: Minimum volumetric efficiency
  summary: Lower saturation bound on volumetric efficiency input signal 1e-3 (default) | scalar in the range (0,1)
  group: Parameters
- name: Maximum volumetric efficiency
  summary: Upper saturation bound on volumetric efficiency input signal 1 (default) | positive scalar
  group: Parameters
- name: Minimum mechanical efficiency
  summary: Lower saturation bound on volumetric efficiency input signal 1e-3 (default) | scalar in the range (0,1)
  group: Parameters
- name: Maximum mechanical efficiency
  summary: Upper saturation bound on volumetric efficiency input signal 1 (default) | scalar in the range (0,1)
  group: Parameters
- name: Pressure gain threshold for motor-pump transition
  summary: Pressure gain at which to initiate smooth transition between motor and pump modes 1e-3 MPa (default) | scalar
  group: Parameters
- name: Angular velocity threshold for motor-pump transition
  summary: Angular velocity at which to initiate smooth transition between pump and motor modes 100 rpm (default) | scalar
  group: Parameters
- name: Cross-sectional area at ports A and B
  summary: Flow area at component inlet and outlet 0.01 m^2 (default) | positive scalar
  group: Parameters
- name: Report when fluid is not fully liquid
  summary: Notification when fluid is not fully liquid None (default) | Warning | Error
  group: Parameters
- name: Check if operating beyond the range of supplied tabulated data
  summary: Simulation warning mode for operating conditions outside range of tabulated data None (default) | Warning | Error
  group: Parameters
- name: Check if operating outside of pump mode
  summary: Simulation warning mode for operating conditions outside pump mode None (default) | Warning | Error
  group: Parameters
- name: Displacement fault
  summary: Option to model displacement fault Add fault
  group: Faults
- name: Faulted displacement factor
  summary: Factor by which to scale faulted displacement 0.5 (default) | positive scalar
  group: Faults
- name: Leakage fault
  summary: Option to model leakage fault Add fault
  group: Faults
- name: Faulted leakage factor
  summary: Factor by which to scale leakage fault 2.0 (default) | positive scalar
  group: Faults
- name: Shaft friction torque fault
  summary: Option to model shaft friction torque fault Add fault
  group: Faults
- name: Faulted shaft friction torque factor
  summary: Factor by which to scale shaft friction torque fault 2.0 (default) | positive scalar
  group: Faults
```

### Parameters

### **Leakage and friction parameterization** — Parameterization of leakage flow rate and friction torque `Analytical` (default) | `Tabulated data - volumetric and mechanical efficiencies` | `Tabulated data - volumetric and mechanical losses` | `Input signal - volumetric and mechanical efficiencies` | `Input signal - volumetric and mechanical losses`

Method to compute the flow-rate and torque losses due to internal leaks and
friction. Use the `Analytical` if the block parameters are
generally available from component data sheets. When you select `Tabulated
data - volumetric and mechanical efficiencies` or
`Tabulated data - volumetric and mechanical losses`, the
block uses lookup tables to map pressure gains and shaft angular velocities to
component efficiencies or losses.

When you select `Input signal - volumetric and mechanical
efficiencies` or `Input signal - volumetric and mechanical
losses`, the block performs the leakage flow rate and friction torque
calculations the same as the `Tabulated data - volumetric and mechanical
efficiencies` or `Tabulated data - volumetric and
mechanical losses` settings, respectively. When you select
`Input signal - volumetric and mechanical efficiencies`,
the block enables the **EV** and **EM** ports. You
use these ports to specify the volumetric and mechanical efficiency. When you select
`Input signal - volumetric and mechanical losses`, the
block enables the **LV** and **LM** ports. You use
these ports to specify the volumetric and mechanical losses.

### **Displacement** — Fluid volume displaced per shaft rotation `30` `cm^3/rev` (default) | positive scalar

Fluid volume displaced per shaft rotation. The block maintains this value
throughout the simulation.

### **Nominal shaft angular velocity** — Shaft angular velocity for given volumetric efficiency `1800` `rpm` (default) | scalar

Angular velocity of the rotary shaft that corresponds to the given volumetric
efficiency. The standard operating conditions in the manufacturer data sheet typically
list these values. The block uses this parameter to calculate the leakage flow rate
and friction torque.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Analytical`.

### **Nominal pressure gain** — Pressure gain for corresponding volumetric efficiency `10` `MPa` (default) | scalar

Pressure gain that corresponds to the given volumetric efficiency. The standard
operating conditions in the manufacturer data sheet typically list these values. The
block uses this parameter to calculate the internal leakage flow rate.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Analytical`.

### **Nominal dynamic viscosity** — Dynamic viscosity at which to specify the volumetric efficiency `0.9` `cP` (default) | scalar

Dynamic viscosity of the hydraulic fluid for the given volumetric efficiency. The
standard operating conditions in the manufacturer data sheet typically list these
values. The block uses this parameter to calculate the internal leakage flow
rate.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Analytical`.

### **Volumetric efficiency at nominal conditions** — Volumetric efficiency at specified nominal conditions `0.92` (default) | positive scalar

Volumetric efficiency for the given conditions. The block defines the volumetric
efficiency as the ratio of actual to ideal volumetric flow rates. The standard
operating conditions in the manufacturer data sheet typically list these values. The
block uses this parameter to calculate the internal leakage flow rate.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Analytical`.

### **Mechanical efficiency at nominal conditions** — Ratio of ideal-to-actual mechanical power `0.88` (default) | positive scalar

Ratio of ideal mechanical power to actual mechanical power at nominal
conditions.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Analytical`.

### **No-load torque** — Minimum torque required to induce shaft rotation `0` `N*m` (default) | scalar

Torque to overcome the seal friction and induce rotation of the mechanical shaft.
This torque is the load-independent component of the total friction torque.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Analytical`.

### **Pressure gain vector, dp** — Pressure gains for given volumetric and mechanical efficiencies or losses `[.1, 1, 2]` `MPa` (default) | vector

Pressure gains for the corresponding tabular efficiency or loss data. The vector
must be at least two elements in strictly increasing order.

Specify the data for a single quadrant, (*ɷ*,
*Δp*). Refer to Operating Modes for the operation
modes corresponding to parameter specifications and the resulting quadrants.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data - volumetric and
mechanical efficiencies` or `Tabulated data - volumetric
and mechanical losses`.

### **Shaft angular velocity vector, w** — Angular velocities at which to specify volumetric and mechanical efficiencies or losses `[250, 500, 1000, 2000, 3000, 4000]` `rpm` (default) | vector

Shaft angular velocities for the corresponding tabular efficiency or loss data.
The vector must be at least two elements in strictly increasing order.

Specify the data for a single quadrant, (*ɷ*,
*Δp*). Refer to Operating Modes for the operation
modes corresponding to parameter specifications and the resulting quadrants.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data - volumetric and
mechanical efficiencies` or `Tabulated data - volumetric
and mechanical losses`.

### **Volumetric efficiency table, e\_v(dp,w)** — Volumetric efficiencies for given pressure gains and angular velocities `[.816, .908, .954, .977, .981, .984; .325, .663, .831, .916, .925, .946; .137, .568, .78, .892, .893, .91]` (default) | matrix

Volumetric efficiencies for the given fluid pressure gains and shaft angular
velocities. The efficiencies must be in the range (0,1]. *M* and
*N* are the sizes of the specified lookup-table vectors:

- *M* is the number of vector elements in the
  **Pressure gain vector, dp** parameter.
- *N* is the number of vector elements in the
  **Shaft angular velocity vector, w** parameter.

Specify the data for a single quadrant, (*ɷ*,
*Δp*). Refer to Operating Modes for the operation
modes corresponding to parameter specifications and the resulting quadrants.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data - volumetric and
mechanical efficiencies`.

### **Mechanical efficiency table, e\_m(dp,w)** — Mechanical efficiencies for given pressure gains and angular velocities `[.996, .996, .996, .996, .996, .996; .988, .989, .989, .989, .989, .99; .981, .981, .982, .982, .983, .984]` (default) | matrix

Mechanical efficiencies for the given fluid pressure gains and shaft angular
velocities. The efficiencies must be in the range (0,1]. *M* and
*N* are the sizes of the specified lookup-table vectors:

- *M* is the number of vector elements in the
  **Pressure gain vector, dp** parameter.
- *N* is the number of vector elements in the
  **Shaft angular velocity vector, w** parameter.

Specify the data for a single quadrant, (*ɷ*,
*Δp*). Refer to Operating Modes for the operation
modes corresponding to parameter specifications and the resulting quadrants.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data - volumetric and
mechanical efficiencies`.

### **Volumetric loss table, q\_loss(dp,w)** — Internal leakage flow rates for corresponding pressure gains and angular velocities `[.023, .023, .023, .023, .0285, .032; .0844, .0842, .0845, .084, .1125, .108; .1079, .108, .11, .108, .1605, .18] * 1e-3` `m^3/s` (default) | matrix

Volumetric losses at the specified fluid pressure gains and shaft angular
velocities. Volumetric loss is the internal leakage volumetric flow rate between port
**A** and port **B**. *M* and
*N* are the sizes of the specified lookup-table vectors:

- *M* is the number of vector elements in the
  **Pressure gain vector, dp** parameter.
- *N* is the number of vector elements in the **Shaft
  angular velocity vector, w** parameter.

Specify the data for a single quadrant, (*ɷ*,
*Δp*). Refer to Operating Modes for the operation
modes corresponding to parameter specifications and the resulting quadrants.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data - volumetric and
mechanical losses`.

### **Mechanical loss table, torque\_loss(dp,w)** — Friction torques for corresponding pressure gains and angular velocities `[.002, .002, .002, .002, .002, .002; .0607, .0556, .0556, .0556, .0556, .0505; .1937, .1937, .1833, .1833, .1729, .1626]` `N*m` (default) | matrix

Mechanical losses for the given pressure gains and shaft angular velocities. The
block defines mechanical loss as the friction torque due to seals and internal
components. *M* and *N* are the sizes of the
specified lookup-table vectors:

- *M* is the number of vector elements in the
  **Pressure gain vector, dp** parameter.
- *N* is the number of vector elements in the **Shaft
  angular velocity vector, w** parameter.

Specify the data for a single quadrant, (*ɷ*,
*Δp*). Refer to Operating Modes for the operation
modes corresponding to parameter specifications and the resulting quadrants. The
tabulated data for the mechanical losses must obey the convention in the figure, with
positive values at positive angular velocities and negative values at negative angular velocities.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data - volumetric and
mechanical losses`.

### **Minimum volumetric efficiency** — Lower saturation bound on volumetric efficiency input signal `1e-3` (default) | scalar in the range (0,1)

Smallest allowed value of the volumetric efficiency. The input from the physical
signal port **EV** saturates inputs below this value.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal - volumetric and
mechanical efficiencies`.

### **Maximum volumetric efficiency** — Upper saturation bound on volumetric efficiency input signal `1` (default) | positive scalar

Largest allowed value of the volumetric efficiency. The input from the physical
signal port **EV** saturates inputs above this value.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal - volumetric and
mechanical efficiencies`.

### **Minimum mechanical efficiency** — Lower saturation bound on volumetric efficiency input signal `1e-3` (default) | scalar in the range (0,1)

Smallest allowed value of the mechanical efficiency. The input from the physical
signal port **EM** saturates inputs below this value.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal - volumetric and
mechanical efficiencies`.

### **Maximum mechanical efficiency** — Upper saturation bound on volumetric efficiency input signal `1` (default) | scalar in the range (0,1)

Largest allowed value of the mechanical efficiency. The input from the physical
signal port **EM** saturates inputs above this value.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal - volumetric and
mechanical efficiencies`.

### **Pressure gain threshold for motor-pump transition** — Pressure gain at which to initiate smooth transition between motor and pump modes `1e-3` `MPa` (default) | scalar

Pressure gain from the inlet to the outlet below which the block begins to
transition between the motor and pump modes. The block uses a hyperbolic tangent
function to smooth the leakage flow rate and friction torque.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal - volumetric and
mechanical efficiencies` or `Input signal - volumetric
and mechanical losses`.

### **Angular velocity threshold for motor-pump transition** — Angular velocity at which to initiate smooth transition between pump and motor modes `100` `rpm` (default) | scalar

Shaft angular velocity below which the block begins to transition between the
motor and pump modes. The block uses the hyperbolic tangent function to smooth the
leakage flow rate and friction torque.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal - volumetric and
mechanical efficiencies` or `Input signal - volumetric
and mechanical losses`.

### **Cross-sectional area at ports A and B** — Flow area at component inlet and outlet `0.01` `m^2` (default) | positive scalar

Flow area at the component inlet and outlet. The areas are assumed equal.

### **Report when fluid is not fully liquid** — Notification when fluid is not fully liquid `None` (default) | `Warning` | `Error`

Whether the block does nothing, generates a warning, or generates an error when
the vapor quality is greater than 0, which indicates that the fluid is not fully
liquid.

### **Check if operating beyond the range of supplied tabulated data** — Simulation warning mode for operating conditions outside range of tabulated data `None` (default) | `Warning` | `Error`

Simulation warning mode for operating conditions outside the range of tabulated
data. If you select `Warning`, the block generates a warning
when the fluid pressure gain or the shaft angular velocity cross outside the specified
tabular data. The warning does not cause simulation to stop. If you select
`Error`, the simulation will stop for conditions outside
the range of tabulated data.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to:

- `Tabulated data - volumetric and mechanical
  efficiencies`
- `Tabulated data - volumetric and mechanical
  losses`

### **Check if operating outside of pump mode** — Simulation warning mode for operating conditions outside pump mode `None` (default) | `Warning` | `Error`

Simulation warning mode for operating conditions outside the pump mode. When you
set this parameter to `Warning`, the block generates a
warning if the pump transitions to motoring mode. The warning does not cause
simulation to stop. If you select `Error`, the simulation
will stop for conditions outside the pump mode.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal - volumetric and
mechanical losses`.

### Faults

### **Displacement fault** — Option to model displacement fault `Add fault`

Option to model a displacement fault in the block. When a fault occurs, the
displacement scales by the value of the **Faulted displacement
factor** parameter. To add a fault, click the **Add
fault** hyperlink.

### **Faulted displacement factor** — Factor by which to scale faulted displacement `0.5` (default) | positive scalar

Factor that the block uses to scale the displacement when a fault
occurs.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Displacement fault** parameter.

### **Leakage fault** — Option to model leakage fault `Add fault`

Option to model a leakage fault in the block. When a fault occurs, the
volumetric efficiencies or losses scale by the value of the **Faulted
leakage factor** parameter. To add a fault, click the **Add
fault** hyperlink.

### **Faulted leakage factor** — Factor by which to scale leakage fault `2.0` (default) | positive scalar

Factor that the block uses to scale the volumetric efficiencies or losses when
a fault occurs.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Leakage fault** parameter.

### **Shaft friction torque fault** — Option to model shaft friction torque fault `Add fault`

Option to model a shaft friction torque fault in the block. When a fault
occurs, the mechanical efficiencies or losses scale by the value of the
**Faulted shaft friction torque factor** parameter. To add
a fault, click the **Add fault** hyperlink.

### **Faulted shaft friction torque factor** — Factor by which to scale shaft friction torque fault `2.0` (default) | positive scalar

Factor that the block uses to scale the mechanical efficiencies or losses when
a fault occurs.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Shaft friction torque fault**
parameter.
## Libraries

Simscape / Fluids / Two-Phase Fluid / Fluid Machines

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

### R2024b: Model faults with the Simscape faults interface

The Fixed-Displacement Pump (2P) block now supports the Simscape faults interface. To learn more, see
Introduction to Simscape Faults.

### R2024a: Check if block operates outside range of calculated data

The **Check if operating beyond the quadrants of supplied tabulated
data** parameter has been renamed to **Check if operating beyond the
range of supplied tabulated data**. You can enable the **Check if
operating beyond the range of supplied tabulated data** parameter to check if the
block is operating beyond the data specified in the block parameters, that is, operating in
a region where the block has extended the data.

## Description

Mechanical-hydraulic power conversion device

The Fixed-Displacement Pump (2P) block represents a pump that extracts
power from a mechanical rotational network and delivers it to a two-phase fluid network. The
pump displacement is fixed at a constant value that you specify through the
**Displacement** parameter.

Ports **A** and **B** represent the pump inlets. Ports
**R** and **C** represent the drive shaft and case. During
normal operation, the pressure gain from port **A** to port
**B** is positive if the angular velocity at port **R**
relative to port **C** is positive.

The Fixed-Displacement Pump (2P) block assumes that liquid
enters the pump inlet. You can use the **Report when fluid is not fully
liquid** parameter to choose what the block does when the fluid does not meet
liquid conditions. To move vapor in a two-phase fluid network, use a compressor.

### Operating Modes

The block has four modes of operation, as shown by this image.

The working mode depends on the pressure gain from port **A** to port
**B**, *Δp = p*B –
*p*A and the angular velocity, *ω =
ω*R – *ω*C:

- The quadrant labeled **1** represents the forward
  pump mode. In this mode, the positive shaft angular velocity causes a pressure
  increase from port **A** to port **B** and flow from
  port **A** to port **B**
- The quadrant labeled **2** represents the reverse
  motor mode. In this mode, the flow from port **B** to port
  **A** causes a pressure decrease from **B** to
  **A** and negative shaft angular velocity.
- The quadrant labeled **3** represents the reverse
  pump mode. In this mode, the negative shaft angular velocity causes a pressure
  increase from port **B** to port **A** and flow from
  port **B** to port **A**
- The quadrant labeled **4** represents the forward
  motor mode. In this mode, the flow from port **A** to port
  **B** causes a pressure decrease from **A** to
  **B** and positive shaft angular velocity.

The response time of the pump is negligible in comparison with the system response time.
The pump reaches steady state nearly instantaneously and is treated as a quasi-steady
component.

### Energy Balance

The block associates the mechanical work done by the pump with an energy exchange. The
governing energy balance equation is

ϕA+ϕB+Phydro=0,

where:

- *Φ*A and
  *Φ*B are the energy flow rates at ports
  **A** and **B**, respectively.
- *P*hydro is the pump hydraulic power,
  which is a function of the pressure difference between the pump ports: Phydro=Δpm˙ρ.

The block generates mechanical power due to torque, *τ*,
and angular velocity, *ω*:

Pmech=τω.

### Flow Rate and Driving Torque

The mass flow rate generated at the pump is

m˙=m˙Ideal−m˙Leak,

where:

- m˙ is the actual mass flow rate.
- m˙Ideal is the ideal mass flow rate.
- m˙Leak is the internal leakage mas flow rate.

The driving torque required to power the pump is

τ=τIdeal+τFriction,

where:

- *τ* is the actual driving torque.
- *τ*Ideal is the ideal driving
  torque.
- *τ*Friction is the friction torque.

**Ideal Flow Rate and Ideal Torque**

The ideal mass flow rate is

m˙Ideal=ρDω,

and the ideal required torque is

τIdeal=DΔp,

where:

- *ρ* is the average of the fluid densities at ports
  **A** and **B**.
- *D* is the **Displacement** parameter.
- *ω* is the shaft angular velocity.
- *Δp* is the pressure gain from inlet to outlet.

### Leakage and Friction Parameterization

You can parameterize leakage and friction analytically, by using tabulated efficiencies
or losses, or by using input efficiencies or input losses.

**Analytical**

When you set the **Leakage and friction parameterization** parameter
to `Analytical`, the leakage flow rate is

m˙Leak=KHPρAvgΔpμAvg,

and the friction torque is

τFriction=(τ0+KTP|Δp|)tanh(4ω(5⋅10−5)ωNom),

where:

- *K*HP is the Hagen-Poiseuille
  coefficient for laminar pipe flows. The block computes this coefficient from the
  specified nominal parameters.
- *μ* is the dynamic viscosity of the fluid, which is the average
  of the values at the ports.
- *K*TP is the friction torque vs.
  pressure gain coefficient at nominal displacement, which the block determines from
  the **Mechanical efficiency at nominal conditions** parameter,
  *ηm*:

  k=τfr,nom−τ0Δpnom.

  *τfr,nom* is the friction
  torque at nominal conditions:

  τfr,nom=(1−ηm,nomηm,nom)DΔpnom.
- *Δp*Nom is the value of the
  **Nominal pressure gain** parameter. This value is the pressure
  gain at which the nominal volumetric efficiency is specified.
- *τ*0 is the value of the
  **No-load torque** parameter.
- *ω*Nom is the value of the
  **Nominal shaft angular velocity** parameter.

The block determines the Hagen-Poiseuille coefficient from the nominal fluid and
component parameters

KHP=DωNomμNom(1−ηv,Nom)ΔpNom,

where:

- *ω*Nom is the value of the
  **Nominal shaft angular velocity** parameter. This value is the
  angular velocity at which the block specifies the nominal volumetric
  efficiency.
- *μ*Nom is the value of the
  **Nominal Dynamic viscosity** parameter. This value is the
  dynamic viscosity at which the block specifies the nominal volumetric efficiency.
- *η*v,Nom is the value of the
  **Volumetric efficiency at nominal conditions** parameter. This
  is the volumetric efficiency that corresponds to the specified nominal
  conditions.

**Tabulated Efficiencies**

When you set the **Leakage and friction parameterization** parameter
to `Tabulated data - volumetric and mechanical efficiencies`, the
leakage flow rate is

m˙Leak=m˙Leak,Pump(1+α)2+m˙Leak,Motor(1−α)2,

and the friction torque is

τFriction=τFriction,Pump1+α2+τFriction,Motor1−α2,

where:

- *α* is a numerical smoothing parameter for the motor-pump
  transition.
- m˙Leak,Motor is the leakage flow rate in motor mode.
- m˙Leak,Pump is the leakage flow rate in pump mode.
- *τ*Friction,Motor is the friction torque
  in motor mode.
- *τ*Friction,Pump is the friction torque
  in pump mode.

This hyperbolic function describes the smoothing parameter *α*

α=tanh(4ΔpΔpThreshold)·tanh(4ωωThreshold),

where:

- *Δp*Threshold is the value of the
  **Pressure gain threshold for motor-pump transition**
  parameter.
- *ω*Threshold is the value of the
  **Angular velocity threshold for motor-pump transition**
  parameter.

The block calculates the leakage flow rate from the volumetric efficiency, which the
 **Volumetric efficiency table** parameter specifies over the
*Δp*–*ɷ* domain. When operating in pump mode, the
leakage flow rate is:

m˙Leak,Pump=(1−ηv)m˙Ideal,

where *η*v is the volumetric
efficiency, which the block obtains either by interpolation or extrapolation of the
tabulated data. Similarly, when operating in motor mode, the leakage flow rate is:

m˙Leak,Motor=−(1−ηv)m˙.

The block calculates the friction torque from the mechanical efficiency, which the
**Mechanical efficiency table** parameter specifies over the
*Δp*–*ɷ* domain. When operating in pump mode, the
friction torque is

τFriction,Pump=(1−ηm)τ,

where *η*m is the mechanical
efficiency, which the block obtains either by interpolation or extrapolation of the
tabulated data. Similarly, when operating in motor mode, the friction torque is

τFriction,Motor=−(1−ηm)τIdeal.

**Tabulated Losses**

When you set the **Leakage and friction parameterization** parameter
to `Tabulated data - volumetric and mechanical losses`, the block
specifies the leakage volumetric flow rate in tabulated form over the
*Δp*–*ɷ* domain:

qLeak=qLeak(Δp,ω).

The block calculates the mass flow rate due to leakage from the
volumetric flow rate:

m˙Leak=ρqLeak.

The block calculates the friction torque in tabulated form:

τFriction=τLoss(Δp,ω)tanh(4ωωthreshold),

where *q*Leak(*Δp*,*ω*) and *τ*Loss(*Δp*,*ω*) are the volumetric and mechanical losses, specified through
interpolation or extrapolation of the tabulated data in the **Volumetric loss
table** and **Mechanical loss table** parameters.

**Input Efficiencies**

When you set the **Leakage and friction parameterization** parameter
to `Input signal - volumetric and mechanical efficiencies`, the
leakage flow rate and friction torque calculations are identical to the
`Tabulated data - volumetric and mechanical efficiencies`
setting. The block replaces the volumetric and mechanical efficiency lookup tables with
the physical signal input ports **EV** and
**EM**.

The efficiencies are positive quantities with values between `0` and
`1`.The block sets input values outside of these bounds to
`0` for inputs smaller than `0` or
`1` for inputs greater than `1`. The block saturates
the efficiency signals at the value of the **Minimum volumetric
efficiency** or **Minimum mechanical efficiency**  parameter
and the **Maximum volumetric efficiency** or **Maximum mechanical
efficiency** parameter.

**Input Losses**

When you set the **Leakage and friction parameterization** parameter
to `Input signal - volumetric and mechanical losses`, the leakage
flow rate and friction torque calculations are identical to the `Tabulated
data - volumetric and mechanical efficiencies` setting. The block replaces
the volumetric and mechanical loss lookup tables with the physical signal input ports
**LV** and **LM**.

The block expects the inputs to be positive and sets the signs automatically from the
*Δp*–*ɷ* quadrant where the component is operating. If
you provide a negative signal, the block returns zero losses.

### Faults

To model a fault, in the **Faults** section,
click the **Add fault** hyperlink next to the fault that you want to model. Use
the fault parameters to specify the fault properties. For more information about fault modeling,
see Introduction to Simscape Faults.

You can model a displacement fault, leakage, or a shaft friction torque fault.

When you enable the **Displacement fault** parameter, the block scales the
displacement by the value of the **Faulted displacement factor** parameter
when the fault triggers,

DFault=fDD,

where *fD* is the value of the **Faulted
displacement factor** parameter. When the **Leakage and friction
parameterization** parameter is `Analytical`, the
block does not use the faulted displacement value to calculate the Hagen-Poiseuille
coefficient or the friction torque at nominal conditions.

When you enable the **Leakage fault** parameter and **Leakage and
friction parameterization** is `Analytical`,
`Tabulated data - volumetric and mechanical efficiencies`, or
`Input signal - volumetric and mechanical efficiencies`, the
faulted volumetric efficiency is

ηv,Fault=ηvfLeak,

where *fLeak* is the value of the
**Faulted leakage factor** parameter and
*ηv* is the volumetric efficiency. When
**Leakage and friction parameterization** is
`Analytical`, the block uses the faulted volumetric efficiency
to calculate the Hagen-Poiseuille coefficient.

When **Leakage and friction parameterization** is `Tabulated data
- volumetric and mechanical losses` or `Input signal -
volumetric and mechanical losses`, the faulted leakage volumetric flow rate
is

qLeak,Fault=fLeakqLeak.

When you enable the **Shaft friction torque fault** parameter and
**Leakage and friction parameterization** is
`Analytical`, `Tabulated data - volumetric and
mechanical efficiencies`, or `Input signal - volumetric and
mechanical efficiencies`, the faulted mechanical efficiency is

ηm,Fault=ηmfFriction,

where *fFriction* is the value
of the **Faulted shaft friction torque factor** parameter and
*ηm* is the mechanical efficiency. When
**Leakage and friction parameterization** is
`Analytical`, the block uses the faulted mechanical efficiency
to calculate the friction torque at nominal conditions.

When **Leakage and friction parameterization** is `Tabulated data
- volumetric and mechanical losses` or `Input signal -
volumetric and mechanical losses`, the faulted friction torque is

τFriction,Fault=fFrictionτFriction.

### Assumptions and Limitations

- The block treats the pump as a quasi-steady component.
- The block ignores the effects of fluid inertia and elevation.
- The pump wall is rigid.
- The block ignores external leakage.
