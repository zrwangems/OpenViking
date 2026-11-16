---
type: simulink-block
title: 'Variable-Displacement Pump (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid Library / Fluid Machines'
documentation_page: 'variabledisplacementpump2p'
documentation_source_path: 'ref/variabledisplacementpump2p.html'
language: en
---

# Variable-Displacement Pump (2P)

## Ports

### Input

### **D** — Displacement volume, cm^3/rev physical signal

Physical signal input port for the volume of fluid displaced rotation. A smoothing
function eases the transition between positive and negative input values.

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

### **Leakage and friction parameterization** — Parameterization of leakage flow rate and friction torque `Analytical` (default) | `Tabulated data - volumetric and mechanical efficiencies` | `Tabulated data - volumetric and mechanical losses` | `Input signal - volumetric and mechanical efficiencies` | `Input signal - volumetric and mechanical losses`

Method to compute the flow-rate and torque losses due to internal leaks and
friction. Use the `Analytical` if the block parameters are
generally available from component data sheets. When you select `Tabulated
data - volumetric and mechanical efficiencies` or `Tabulated
data - volumetric and mechanical losses`, the block uses lookup tables to
map pressure gain, angular velocity, and displacement to component efficiencies or
losses.

When you select `Input signal - volumetric and mechanical
efficiencies` or `Input signal - volumetric and mechanical
losses`, the block performs the leakage flow rate and friction torque
calculations the same as the `Tabulated data - volumetric and mechanical
efficiencies` or `Tabulated data - volumetric and mechanical
losses` settings, respectively. When you select `Input signal
- volumetric and mechanical efficiencies`, the block enables the
**EV** and **EM** ports. You use these ports to
specify the volumetric and mechanical efficiency. When you select `Input
signal - volumetric and mechanical losses`, the block enables the
**LV** and **LM** ports. You use these ports to
specify the volumetric and mechanical losses.

### **Nominal displacement** — Displacement at which to specify volumetric efficiency `30` `cm^3/rev` (default) | positive scalar

Fluid displacement for a given volumetric efficiency. The standard operating
conditions in the manufacturer data sheet typically list these values. The block uses
this parameter to calculate the leakage flow rate and friction torque.

### **Nominal shaft angular velocity** — Shaft angular velocity for given volumetric efficiency `1800` `rpm` (default) | scalar

Angular velocity of the rotary shaft that corresponds to the given volumetric
efficiency. The standard operating conditions in the manufacturer data sheet typically
list these values. The block uses this parameter to calculate the leakage flow rate and
friction torque.

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

Dynamic viscosity of the hydraulic fluid for the given volumetric efficiency. These
values are typically available at standard operating conditions in manufacturer data
sheet. The block uses this parameter to calculate the internal leakage flow rate.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Analytical`.

### **Volumetric efficiency at nominal conditions** — Volumetric efficiency at specified nominal conditions `0.92` (default) | scalar in the range (0,1)

Volumetric efficiency for the given conditions. The block defines the volumetric
efficiency as the ratio of actual to ideal volumetric flow rates. The standard operating
conditions in the manufacturer data sheet typically list these values. The block uses
this parameter to calculate the internal leakage flow rate.

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

Specify the data for a single octant, (*ɷ*, *Δp*,
*D*). Refer to Operating Modes for the operation
modes corresponding to parameter specifications and the resulting octants.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data - volumetric and
mechanical efficiencies` or `Tabulated data - volumetric
and mechanical losses`.

### **Shaft angular velocity vector, w** — Angular velocities at which to specify volumetric and mechanical efficiencies or losses `[250, 500, 1000, 2000, 3000, 4000]` `rpm` (default) | vector

Shaft angular velocities for the corresponding tabular efficiency or loss data. The
vector must be at least two elements in strictly increasing order.

Specify the data for a single octant, (*ɷ*, *Δp*,
*D*). Refer to Operating Modes for the operation
modes corresponding to parameter specifications and the resulting octants.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data - volumetric and
mechanical efficiencies` or `Tabulated data - volumetric
and mechanical losses`.

### **Displacement vector, D** — Displacements at which to specify the volumetric and mechanical efficiencies or losses `[-30, -19, 19, 30]` `cm^3/rev` (default) | vector

Displacements at which to specify the efficiencies or losses tabular data. The
vector must be at least two elements in strictly increasing order.

Specify the data for a single octant, (*ɷ*, *Δp*,
*D*). Refer to Operating Modes for the operation
modes corresponding to parameter specifications and the resulting octants.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data - volumetric and
mechanical efficiencies` or `Tabulated data - volumetric
and mechanical losses`.

### **Volumetric efficiency table, e\_v(dp,w,D)** — Volumetric efficiencies for given pressure gains, angular velocities, and displacements `repmat([.816, .908, .954, .977, .981, .984; .325, .663, .831, .916, .925, .946; .137, .568, .78, .892, .893, .91], 1, 1, 4)` (default) | matrix

Volumetric efficiencies at the specified fluid pressure gains, shaft angular
velocities, and displacements. The efficiencies must be in the range of
`0`–`1`. *M*, *N*,
and *L* are the sizes of the specified lookup-table vectors:

- *M* is the number of vector elements in the
  **Pressure gain vector, dp** parameter.
- *N* is the number of vector elements in the **Shaft
  angular velocity vector, w** parameter.
- *L* is the number of vector elements in the
  **Displacement vector, D** parameter.

Specify the data for a single octant, (*ɷ*, *Δp*,
*D*). Refer to Operating Modes for the operation
modes corresponding to parameter specifications and the resulting octants.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data - volumetric and
mechanical efficiencies`.

### **Mechanical efficiency table, e\_m(dp,w,D)** — Mechanical efficiencies for given pressure gains, angular velocities, and displacements `repmat([.996, .996, .996, .996, .996, .996; .988, .989, .989, .989, .989, .99; .981, .981, .982, .982, .983, .984], 1, 1, 4)` (default) | matrix

Mechanical efficiencies that correspond to the specified fluid pressure gains, shaft
angular velocities, and displacements. The efficiencies must be in the range of
`0`–`1`. *M*, *N*,
and *L* are the sizes of the specified lookup-table vectors:

- *M* is the number of vector elements in the
  **Pressure gain vector, dp** parameter.
- *N* is the number of vector elements in the **Shaft
  angular velocity vector, w** parameter.
- *L* is the number of vector elements in the
  **Displacement vector, D** parameter.

Specify the data for a single octant, (*ɷ*, *Δp*,
*D*). Refer to Operating Modes for the operation
modes corresponding to parameter specifications and the resulting octants.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data - volumetric and
mechanical efficiencies`.

### **Volumetric loss table, q\_loss(dp,w,D)** — Internal leakage flow rates for corresponding pressure gains, angular velocities, and displacements `repmat([.0282, .0253, .0241, .0235, .0291, .0325; .2596, .1271, .1017, .0917, .1216, .1142; .7874, .1901, .141, .1211, .1797, .1978] * 1e-3, 1, 1, 4)` `m^3/s` (default) | matrix

Volumetric losses at the specified fluid pressure gains, shaft angular velocities,
and displacements. The block defines volumetric loss the internal leakage volumetric
flow rate between port **A** and port **B**.
*M* and *N* are the sizes of the specified
lookup-table vectors:

- *M* is the number of vector elements in the
  **Pressure gain vector, dp** parameter.
- *N* is the number of vector elements in the **Shaft
  angular velocity vector, w** parameter.
- *L* is the number of vector elements in the
  **Displacement vector, D** parameter.

Specify the data for a single octant, (*ɷ*, *Δp*,
*D*). Refer to Operating Modes for the operation
modes corresponding to parameter specifications and the resulting octants.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data - volumetric and
mechanical losses`.

### **Mechanical loss table, torque\_loss(dp,w,D)** — Friction torques for corresponding pressure gains, angular velocities, and displacements `repmat([.002, .002, .002, .002, .002, .002; .06, .055, .055, .055, .055, .05; .19, .19, .18, .18, .17, .16], 1, 1, 4)` `N*m` (default) | matrix

Mechanical losses for the given pressure gains, shaft angular velocities, and
displacements. The block defines mechanical loss as the friction torque due to seals and
internal components. *M* and *N* are the sizes of the
specified lookup-table vectors:

- *M* is the number of vector elements in the
  **Pressure gain vector, dp** parameter.
- *N* is the number of vector elements in the **Shaft
  angular velocity vector, w** parameter.
- *L* is the number of vector elements in the
  **Displacement vector, D** parameter.

Specify the data for a single octant, (*ɷ*, *Δp*,
*D*). Refer to Operating Modes for the operation
modes corresponding to parameter specifications and the resulting octants. The tabulated
data for the mechanical losses must obey the convention in the figure, with positive
values at positive angular velocities and negative values at negative angular velocities.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Tabulated data - volumetric and
mechanical losses`.

### **Minimum volumetric efficiency** — Lower saturation bound on volumetric efficiency input signal `1e-3` (default) | scalar in the range (0,1)

Smallest allowed value of the volumetric efficiency. The input from the physical
signal port **EV** saturates inputs below this value.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal - volumetric and mechanical
efficiencies`.

### **Maximum volumetric efficiency** — Upper saturation bound on volumetric efficiency input signal `1` (default) | scalar in the range (0,1)

Largest allowed value of the volumetric efficiency. The input from the physical
signal port **EV** saturates inputs above this value.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal - volumetric and mechanical
efficiencies`.

### **Minimum mechanical efficiency** — Lower saturation bound on volumetric efficiency input signal `1e-3` (default) | scalar in the range (0,1)

Smallest allowed value of the mechanical efficiency. The input from the physical
signal port **EM** saturates inputs below this value.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal - volumetric and mechanical
efficiencies`.

### **Maximum mechanical efficiency** — Upper saturation bound on volumetric efficiency input signal `1` (default) | scalar in the range (0,1)

Largest allowed value of the mechanical efficiency. The input from the physical
signal port **EM** saturates inputs above this value.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal - volumetric and mechanical
efficiencies`.

### **Pressure gain threshold for motor-pump transition** — Pressure gain at which to initiate smooth transition between motor and pump modes `1e-3` `MPa` (default) | scalar

Pressure gain from the inlet to the outlet below which the block begins to
transition between the motor and pump modes. The block uses a hyperbolic tangent
function to smooth the leakage flow rate and friction torque.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal - volumetric and mechanical
efficiencies` or `Input signal - volumetric and mechanical
losses`.

### **Angular velocity threshold for motor-pump transition** — Angular velocity at which to initiate smooth transition between pump and motor modes `100` `rpm` (default) | scalar

Shaft angular velocity below which the block begins to transition between the motor
and pump modes. The block uses the hyperbolic tangent function to smooth the leakage
flow rate and friction torque.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal - volumetric and mechanical
efficiencies` or `Input signal - volumetric and mechanical
losses`.

### **Cross-sectional area at ports A and B** — Flow area at component inlet and outlet `0.01` `m^2` (default) | positive scalar

Flow area at the component inlet and outlet. The areas are assumed equal.

### **Report when fluid is not fully liquid** — Notification when fluid is not fully liquid `None` (default) | `Warning` | `Error`

Whether the block does nothing, generates a warning, or generates an error when the
vapor quality is greater than 0, which indicates that the fluid is not fully
liquid.

### **Check if operating beyond the range of supplied tabulated data** — Simulation warning mode for operating conditions outside range of tabulated data `None` (default) | `Warning` | `Error`

Simulation warning mode for operating conditions outside the range of tabulated
data. If you select `Warning`, the block generates a warning
when the fluid pressure gain or the shaft angular velocity cross outside the specified
tabular data. The warning does not cause simulation to stop. If you select
`Error`, the simulation will stop for conditions outside the
range of tabulated data.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to:

- `Tabulated data - volumetric and mechanical
  efficiencies`
- `Tabulated data - volumetric and mechanical
  losses`

### **Check if operating outside of pump mode** — Simulation warning mode for operating conditions outside pump mode `None` (default) | `Warning` | `Error`

Simulation warning mode for operating conditions outside the pump mode. When you set
this parameter to `Warning`, the block generates a warning if
the pump transitions to motoring mode. The warning does not cause simulation to stop.
If you select `Error`, the simulation will stop for conditions
outside the pump mode.

#### Dependencies

To enable this parameter, set **Leakage and friction
parameterization** to `Input signal - volumetric and mechanical
losses`.

## Libraries

Simscape / Fluids / Two-Phase Fluid / Fluid Machines

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

### R2024a: Check if block operates outside range of calculated data

The **Check if operating beyond the octants of supplied tabulated
data** parameter has been renamed to **Check if operating beyond the
range of supplied tabulated data**. You can enable the **Check if
operating beyond the range of supplied tabulated data** parameter to check if the
block is operating beyond the data specified in the block parameters, that is, operating in
a region where the block has extended the data.

## Description

Variable-displacement bidirectional two-phase fluid pump

The Variable-Displacement Pump (2P) block represents a device that extracts
power from a mechanical rotational network and delivers it to a two-phase fluid network. The
pump displacement varies during simulation according to the physical input signal at port
**D**.

Ports **A** and **B** represent the pump inlets. Ports
**R** and **C** represent the drive shaft and case. During
normal operation, the pressure gain from port **A** to port
**B** is positive if the angular velocity at port **R**
relative to port **C** is positive.

The Variable-Displacement Pump (2P) block assumes that
liquid enters the pump inlet. You can use the **Report when fluid is not fully
liquid** parameter to choose what the block does when the fluid does not meet
liquid conditions. To move vapor in a two-phase fluid network, use a compressor.

### Operating Modes

The block has four modes of operation, as shown by this image.

The working mode depends on the pressure gain from port **A** to port
**B**, *Δp = p*B –
*p*A; the angular velocity, *ω =
ω*R – *ω*C; and
the fluid volumetric displacement at port **D**. The figure above maps
these modes to the octants of a
*Δp*-*ω*-*D* chart:

- The quadrant labeled **1** represents the forward pump
  mode. In this mode, the positive shaft angular velocity causes a pressure increase from
  port **A** to port **B** and flow from port
  **A** to port **B**
- The quadrant labeled **2** represents the reverse motor
  mode. In this mode, the flow from port **B** to port
  **A** causes a pressure decrease from **B** to
  **A** and negative shaft angular velocity.
- The quadrant labeled **3** represents the reverse pump
  mode. In this mode, the negative shaft angular velocity causes a pressure increase from
  port **B** to port **A** and flow from port
  **B** to port **A**
- The quadrant labeled **4** represents the forward motor
  mode. In this mode, the flow from port **A** to port
  **B** causes a pressure decrease from **A** to
  **B** and positive shaft angular velocity.
- The quadrant labeled **5** represents the reverse motor
  mode. In this mode, the flow from port **B** to port
  **A** causes a pressure decrease from **B** to
  **A** and positive shaft angular velocity.
- The quadrant labeled **6** represents the forward pump
  mode. In this mode, the negative shaft angular velocity causes a pressure increase from
  port **A** to port **B** and flow from port
  **A** to port **B**
- The quadrant labeled **7** represents the forward motor
  mode. In this mode, the flow from port **A** to port
  **B** causes a pressure decrease from **A** to
  **B** and negative shaft angular velocity.
- The quadrant labeled **8** represents the reverse pump
  mode. In this mode, the positive shaft angular velocity causes a pressure increase from
  port **B** to port **A** and flow from port
  **B** to port **A**

The response time of the pump is negligible in comparison with the system response time.
The pump reaches steady state nearly instantaneously and is treated as a quasi-steady
component.

### Energy Balance

The block associates the mechanical work done by the pump with an energy exchange. The
governing energy balance equation is:

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
- *ω* is the shaft angular velocity.
- *Δp* is the pressure gain from inlet to outlet.
- *D* is the **Displacement** specified at
  physical signal port **D**.

### Leakage and friction parameterization

You can parameterize leakage and friction analytically, by using tabulated efficiencies
or losses, or by using input efficiencies or input losses.

**Analytical**

When you set the **Leakage and Friction Parameterization** parameter
to `Analytical`, the leakage flow rate is

m˙Leak=KHPρAvgΔpμAvg,

and the friction torque is

τFriction=(τ0+KTP|Δp||D|DNomtanh4ω(5e−5)ωNom),

where:

- *K*HP is the Hagen-Poiseuille
  coefficient for laminar pipe flows. The block computes this coefficient from the
  specified nominal parameters.
- *μ* is the dynamic viscosity of the fluid, which is the average
  of the values at the ports.
- *k* is the friction torque vs. pressure gain coefficient at
  nominal displacement, which the block determines from the **Mechanical
  efficiency at nominal conditions** parameter,
  *ηm,nom*:

  k=τfr,nom−τ0Δpnom.

  *τfr,nom* is the friction
  torque at nominal conditions:

  τfr,nom=(1−ηm,nomηm,nom)DnomΔpnom.
- *Δp*Nom is the value of the
  **Nominal pressure gain** parameter. This value is the pressure
  gain at which the nominal volumetric efficiency is specified.
- *D*Nom is the value of the
  **Nominal Displacement** parameter.
- *τ*0 is the value of the
  **No-load torque** parameter.
- *ω*Nom is the value of the
  **Nominal shaft angular velocity** parameter.

The block determines the Hagen-Poiseuille coefficient from the nominal fluid and
component parameters

KHP=DNomωNomμNom(1−ηv,Nom)ΔpNom,

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

α=tanh(4ΔpΔpThreshold)·tanh(4ωωThreshold)·tanh(4DDThreshold),

where:

- *Δp*Threshold is the value of the
  **Pressure gain threshold for pump-motor transition** block
  parameter.
- *ω*Threshold is the value of the
  **Angular velocity threshold for pump-motor transition** block
  parameter.
- *D*Threshold is the value of the
  **Angular velocity threshold for motor-pump transition** block
  parameter.

The block calculates the leakage flow rate from the volumetric efficiency, which the
 **Volumetric efficiency table** parameter specifies over the
*Δp*–*ɷ*–*D* domain. When operating
in pump mode, the leakage flow rate is:

m˙Leak,Pump=(1−ηv)m˙Ideal,

where *η*v is the volumetric
efficiency, which the block obtains either by interpolation or extrapolation of the
tabulated data. Similarly, when operating in motor mode, the leakage flow rate is:

m˙Leak,Motor=−(1−ηv)m˙.

The block calculates the friction torque from the mechanical efficiency, which the
**Mechanical efficiency table** parameter specifies over the
*Δp*–*ɷ*–*D* domain. When operating
in pump mode, the friction torque is

τFriction,Pump=(1−ηm)τ,

where *η*m is the mechanical
efficiency, which the block obtains either by interpolation or extrapolation of the
tabulated data. Similarly, when operating in motor mode, the friction torque is

τFriction,Motor=−(1−ηm)τIdeal.

**Tabulated Losses**

When you set the **Leakage and friction parameterization** parameter
to `Tabulated data - volumetric and mechanical losses`, the block
specifies the leakage volumetric flow rate in tabulated form over the
*Δp*–*ɷ*–*D* domain:

qLeak=qLeak(Δp,ω,D).

The block calculates the mass flow rate due to leakage from the
volumetric flow rate:

m˙Leak=ρqLeak.

The block calculates the friction torque in tabulated form:

τFriction=τFriction(Δp,ω,D),

where *q*Leak(*Δp*,*ω*,*D*) and *τ*Friction(*Δp*,*ω*,*D*) are the volumetric and mechanical losses, specified through
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

When you set the **Leakage and friction parameterization** parameter
to `Input signal - volumetric and mechanical losses`, the leakage
flow rate and friction torque calculations are identical to the `Tabulated
data - volumetric and mechanical efficiencies` setting. The block replaces
the volumetric and mechanical loss lookup tables with the physical signal input ports
**LV** and **LM**.

**Input Losses**

When you set **Leakage and friction parameterization** to
`Input signal - volumetric and mechanical efficiencies`, the
leakage flow rate and friction torque calculations are identical to the
`Tabulated data - volumetric and mechanical efficiencies`
setting. The volumetric and mechanical loss lookup tables are replaced with physical
signal inputs that you specify through ports **LV** and
**LM**.

The block expects the inputs to be positive and sets the signs automatically from the
*Δp*–*ɷ* quadrant where the component is operating. If
you provide a negative signal, the block returns zero losses.

### Assumptions and Limitations

- The block treats the pump as a quasi-steady component.
- The block ignores the effects of fluid inertia and elevation.
- The pump wall is rigid.
- The block ignores external leakage.
