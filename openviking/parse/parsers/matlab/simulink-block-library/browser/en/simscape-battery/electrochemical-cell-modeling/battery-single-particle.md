---
type: simulink-block
title: 'Battery Single Particle'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Electrochemical Cell Modeling'
documentation_page: 'batterysingleparticle'
documentation_source_path: 'ref/batterysingleparticle.html'
language: en
---

# Battery Single Particle

## Ports

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the positive battery terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the negative battery terminal.

### **H** — Battery thermal mass thermal

Thermal conserving port associated with the thermal mass of the battery.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Extrapolation method for all tables** — Method of extrapolation for tables `Nearest` (default) | `Linear` | `Error`

Extrapolation method for the table-based parameters:

- `Linear` — Estimate values beyond the data by
  creating a tangent line at the end of the known data and extending it beyond that
  limit.
- `Nearest` — Extrapolate a value at a query point that
  is the value at the nearest sample grid point.
- `Error` — Return an error if the value goes beyond
  the known data. If you select this option, the block does not use
  extrapolation.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ExtrapolationMethod` |
| **Values:** | `"nearest"` (default) | `"linear"` | `"error"` |

### Geometry

### **Anode thickness** — Thickness of anode `3.4E-5` `m` (default) | positive scalar

Thickness of the anode.

### **Electrolyte layer count of anode** — Electrolyte layer count of anode `10` (default) | scalar greater than 3

Electrolyte layer count of the anode.

### **Separator thickness** — Thickness of separator `2.5E-5``m` (default) | positive scalar

Thickness of the separator.

### **Electrolyte layer count of separator** — Electrolyte layer count of separator `5` (default) | scalar greater than 3

Electrolyte layer count of the separator.

### **Cathode thickness** — Thickness of cathode `8E-5``m` (default) | positive scalar

Thickness of the cathode.

### **Electrolyte layer count of cathode** — Electrolyte layer count of cathode `10` (default) | scalar greater than 3

Electrolyte layer count of the cathode.

### **Electrode plate area** — Area of electrode plate `1.8E-1``m^2` (default) | positive scalar

Area of the electrode plate.

### **Anode particle radius** — Particle radius of anode `5E-6``m` (default) | positive scalar

Particle radius of the anode.

### **Anode shell count** — Number of shells for anode `10` (default) | positive scalar greater than 3

Number of shells for the anode.

### **Cathode particle radius** — Particle radius of cathode `5E-8``m` (default) | positive scalar

Particle radius of the cathode.

### **Cathode shell count** — Number of shells for cathode `10` (default) | positive scalar greater than 3

Number of shells for the cathode.

### Electrodes Properties

### **Volume fraction of anode active material** — Volume fraction of active material in anode `0.58` (default) | scalar in the range (0,1)

Volume fraction of the active material in the anode.

### **Volume fraction of cathode active material** — Volume fraction of active material in cathode `0.374` (default) | scalar in the range (0,1)

Volume fraction of the active material in the cathode.

### **Stoichiometry breakpoints specification** — Option to specify stoichiometry breakpoints `Normalized` (default) | `Absolute`

*Since R2025a*

Option to specify the stoichiometry breakpoints. Set this parameter to
`Normalized` to specify the open-circuit potentials
normalized to the relative stoichiometry. Set this parameter to
`Absolute` to specify the open-circuit potentials
normalized to the absolute stoichiometry.

### **Normalized stoichiometry breakpoints** — Normalized stoichiometry breakpoints for open-circuit potential of electrode `linspace(0.025, 0.975, 39)` (default) | vector of elements in the range [0,1]

Normalized stoichiometry breakpoints for the open-circuit potential of the
electrode. The size of this parameter must be equal to the size of the **Anode
open-circuit potential relative to normalized stoichiometry** and
**Cathode open-circuit potential relative to normalized
stoichiometry** parameters.

**Note**

A value of `0` means that the stoichiometry of the particle is
equal to the minimum stoichiometry of the electrode, as you specify in the
**Anode minimum stoichiometry** and **Cathode minimum
stoichiometry** parameters. A value of `1` means that
the stoichiometry of the particle is equal to the maximum stoichiometry of the
electrode, as you specify in the **Anode maximum stoichiometry**
and **Cathode maximum stoichiometry** parameters.

Overall, the block calculates the values of the normalized stoichiometry by
using this equation:

NormalizedSurfaceStoichiometry = ElectrodeStoichiometry(end) - MinimumStoichiometryMaximumStoichiometry - MinimumStoichiometry.

#### Dependencies

To enable this parameter, set **Stoichiometry breakpoints
specifications** to `Normalized`.

### **Anode open-circuit potential relative to normalized stoichiometry** — Open-circuit potential of anode relative to normalized stoichiometry `[.435; .325; .259; .221; .204; .194; .179; .166; .155; .145; .137; .131; .128; .127; .126; .125; .124; .123; .122; .121; .118; .117; .112; .109; .105; .1; .098; .095; .094; .093; .091; .09; .089; .088; .087; .086; .085; .084; .083]` `V` (default) | vector of positive elements

*Since R2025a*

Open-circuit potential of the anode relative to the normalized stoichiometry. The
size of this parameter must be equal to the size of the **Normalized
stoichiometry breakpoints** parameter.

#### Dependencies

To enable this parameter, set **Stoichiometry breakpoints
specifications** to `Normalized`.

### **Cathode open-circuit potential relative to normalized stoichiometry** — Open-circuit potential of cathode relative to normalized stoichiometry `[3.598; 3.53; 3.494; 3.474; 3.46; 3.455; 3.454; 3.453; 3.4528; 3.4526; 3.4524; 3.452; 3.4518; 3.4516; 3.4514; 3.4512; 3.451; 3.4508; 3.4506; 3.4503; 3.45; 3.4498; 3.4495; 3.4493; 3.449; 3.4488; 3.4486; 3.4484; 3.4482; 3.4479; 3.4477; 3.4475; 3.4473; 3.447; 3.4468; 3.4466; 3.4464; 3.4462; 3.4458]` `V` (default) | vector of positive elements

*Since R2025a*

Open-circuit potential of the cathode relative to the normalized stoichiometry.
The size of this parameter must be equal to the size of the **Normalized
stoichiometry breakpoints** parameter.

#### Dependencies

To enable this parameter, set **Stoichiometry breakpoints
specifications** to `Normalized`.

### **Absolute anode stoichiometry breakpoints** — Absolute stoichiometry breakpoints for open-circuit potential of anode `linspace(0.025, 0.975, 39)` (default) | vector of elements in the range [0,1]

*Since R2025a*

Absolute stoichiometry breakpoints for the open-circuit potential of the anode.
The size of this parameter must be equal to the size of the **Anode
open-circuit potential relative to absolute stoichiometry**
parameter.

#### Dependencies

To enable this parameter, set **Stoichiometry breakpoints
specifications** to `Absolute`.

### **Anode open-circuit potential relative to absolute stoichiometry** — Open-circuit potential of anode relative to absolute stoichiometry `[.484; .335; .253; .209; .2; .181; .165; .151; .139; .131; .128; .125; .124; .124; .123; .122; .119; .117; .111; .108; .101; .098; .095; .093; .092; .088; .088; .088; .088; .087; .087; .087; .085; .082; .079; .071; .064; .049; .026]` `V` (default) | vector of positive elements

*Since R2025a*

Open-circuit potential of the anode relative to the absolute stoichiometry. The
size of this parameter must be equal to the size of the **Absolute anode
stoichiometry breakpoints** parameter.

#### Dependencies

To enable this parameter, set **Stoichiometry breakpoints
specifications** to `Absolute`.

### **Absolute cathode stoichiometry breakpoints** — Absolute stoichiometry breakpoints for open-circuit potential of cathode `linspace(0.025, 0.975, 39)` (default) | vector of elements in the range [0,1]

*Since R2025a*

Absolute stoichiometry breakpoints for the open-circuit potential of the cathode.
The size of this parameter must be equal to the size of the **Cathode
open-circuit potential relative to absolute stoichiometry**
parameter.

#### Dependencies

To enable this parameter, set **Stoichiometry breakpoints
specifications** to `Absolute`.

### **Cathode open-circuit potential relative to absolute stoichiometry** — Open-circuit potential of cathode relative to absolute stoichiometry `[3.81; 3.608; 3.512; 3.478; 3.459; 3.453; 3.45257; 3.45214; 3.45171; 3.45128; 3.45085; 3.45042; 3.44999; 3.44956; 3.44913; 3.4487; 3.44827; 3.44784; 3.44741; 3.44698; 3.44655; 3.44612; 3.44569; 3.44526; 3.44483; 3.4444; 3.44397; 3.44354; 3.44311; 3.44268; 3.44225; 3.44182; 3.44139; 3.44096; 3.44053; 3.44; 3.412; 3.304; 2.968]` `V` (default) | vector of positive elements

*Since R2025a*

Open-circuit potential of the cathode relative to the absolute stoichiometry. The
size of this parameter must be equal to the size of the **Absolute cathode
stoichiometry breakpoints** parameter.

#### Dependencies

To enable this parameter, set **Stoichiometry breakpoints
specifications** to `Absolute`.

### **Anode maximum ion concentration** — Maximum ion concentration in anode `30555` `mol/m^3` (default) | positive scalar

Maximum ion concentration in the anode.

### **Anode maximum stoichiometry** — Maximum stoichiometry in anode `0.811` (default) | positive scalar

Maximum stoichiometry in the anode. The value of this parameter must be greater
than the value of the **Anode minimum stoichiometry**
parameter.

### **Anode minimum stoichiometry** — Minimum stoichiometry in anode `0.0132` (default) | positive scalar

Minimum stoichiometry in the anode. The value of this parameter must be less than
the value of the **Anode maximum stoichiometry** parameter.

### **Cathode maximum ion concentration** — Maximum ion concentration in cathode `22806` `mol/m^3` (default) | positive scalar

Maximum ion concentration in the cathode.

### **Cathode maximum stoichiometry** — Maximum stoichiometry in cathode `0.74` (default) | positive scalar

Maximum stoichiometry in the cathode. The value of this parameter must be greater
than the value of the **Cathode minimum stoichiometry**
parameter.

### **Cathode minimum stoichiometry** — Minimum stoichiometry in cathode `0.035` (default) | positive scalar

Minimum stoichiometry in the cathode. The value of this parameter must be less
than the value of the **Cathode maximum stoichiometry**
parameter.

### **Diffusion coefficient of anode active material** — Diffusion coefficient of active material in anode `3E-15` `m^2/s` (default) | positive scalar

Diffusion coefficient of the active material in the anode.

### **Diffusion coefficient of cathode active material** — Diffusion coefficient of active material in cathode `5.9E-20` `m^2/s` (default) | positive scalar

Diffusion coefficient of the active material in the cathode.

### **Anode conductivity** — Conductivity of anode `100` `S/m` (default) | positive scalar

Conductivity of the anode.

### **Cathode conductivity** — Conductivity of cathode `0.5` `S/m` (default) | positive scalar

Conductivity of the cathode.

### **Current collector resistance** — Resistance of current collector `0` `Ohm` (default) | nonnegative scalar

Resistance of the current collector.

### Electrolyte Properties

### **Volume fraction of electrolyte in anode** — Fraction of volume of electrolyte in anode `0.3874` (default) | scalar in the range (0,1)

Fraction of the volume of the electrolyte in the anode.

### **Volume fraction of electrolyte in separator** — Fraction of volume of electrolyte in separator `0.45` (default) | scalar in the range (0,1)

Fraction of the volume of the electrolyte in the separator.

### **Volume fraction of electrolyte in cathode** — Fraction of volume of electrolyte in cathode `0.5725` (default) | scalar in the range (0,1)

Fraction of the volume of the electrolyte in the cathode.

### **Electrolyte conductivity** — Conductivity of electrolyte `0.29` `S/m` (default) | positive scalar

Conductivity of the electrolyte.

### **Anode Bruggeman exponent** — Bruggeman exponent of anode `1.5` (default) | scalar greater than or equal to 1

Bruggeman exponent of the anode.

### **Separator Bruggeman exponent** — Bruggeman exponent of separator `1.5` (default) | scalar greater than or equal to 1

Bruggeman exponent of the separator.

### **Cathode Bruggeman exponent** — Bruggeman exponent of cathode `1.5` (default) | scalar greater than or equal to 1

Bruggeman exponent of the cathode.

### **Transference number** — Fraction of total electric current that ion carries in electrolyte `0.363` (default) | scalar in the range [0,1]

Fraction of the total electric current that an ion carries in an
electrolyte.

### **Diffusion coefficient of electrolyte** — Diffusion coefficient of electrolyte `2E-10` `m^2/s` (default) | positive scalar

Diffusion coefficient of the electrolyte that the block uses inside the Fick's Law
equation.

### Reaction Kinetics

### **Charge transfer rate constant for Anode** — Rate constant of charge transfer for anode `8.8E-11` `m^(5/2)/(mol^(1/2)*s)` (default) | positive scalar

Rate constant of the charge transfer for the anode. The block uses this value in
the Butler-Volmer equation to model the electrochemical kinetics at the
electrode-electrolyte interface.

### **Charge transfer rate constant for Cathode** — Rate constant of charge transfer for cathode `2.8E-13` `m^(5/2)/(mol^(1/2)*s)` (default) | positive scalar

Rate constant of the charge transfer for the cathode. The block uses this value in
the Butler-Volmer equation to model the electrochemical kinetics at the
electrode-electrolyte interface.

### Thermal

### **Battery thermal mass** — Thermal mass of battery associated with thermal port `77` `J/K` (default) | positive scalar

Thermal mass at the thermal port **H**. This parameter represents the
energy required to raise the temperature of the thermal port by one kelvin.

### **Arrhenius reference temperature** — Arrhenius reference temperature `298.15` `K` (default) | positive scalar

Arrhenius reference temperature.

### **Activation energy for diffusion in anode active material** — Activation energy for diffusion inside active material of anode `39000` `J/mol` (default) | positive scalar

Activation energy for the diffusion inside the active material of the
anode.

### **Activation energy for diffusion in cathode active material** — Activation energy for diffusion inside active material of cathode `35000` `J/mol` (default) | positive scalar

Activation energy for the diffusion inside the active material of the
cathode.

### **Activation energy for diffusion in electrolyte** — Activation energy for diffusion inside electrolyte `26600` `J/mol` (default) | positive scalar

Activation energy for the diffusion inside the electrolyte.

### **Activation energy for conduction in anode** — Activation energy for conduction inside anode `3000` `J/mol` (default) | positive scalar

Activation energy for the conduction inside the anode.

### **Activation energy for conduction in cathode** — Activation energy for conduction inside cathode `3000` `J/mol` (default) | positive scalar

Activation energy for the conduction inside the cathode.

### **Activation energy for conduction in electrolyte** — Activation energy for conduction inside electrolyte `11000` `J/mol` (default) | positive scalar

Activation energy for the conduction inside the electrolyte.

### **Activation energy for charge transfer in Anode** — Activation energy for charge transfer inside anode `13000` `J/mol` (default) | positive scalar

Activation energy for the charge transfer inside the anode.

### **Activation energy for charge transfer in Cathode** — Activation energy for charge transfer inside cathode `20000` `J/mol` (default) | positive scalar

Activation energy for the charge transfer inside the cathode.

### Faults

### **Additional resistance fault** — Option to fault series-connected resistance `Add fault`

*Since R2025a*

Option to fault a series-connected resistance. Use this fault to model an
open-circuit cell if the additional resistance is greater than 1000 ohm, or an
abnormal internal resistance.

To add a fault, click the **Add fault**
hyperlink.

### **Additional resistance when faulted** — Additional resistance when block is faulted `1e5` `Ohm` (default) | positive scalar

*Since R2025a*

Value of the additional resistance when the block is in a faulted state.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for
the **Additional resistance fault** parameter.

### **Trigger type** — Type of fault trigger `Always On` (default) | `Timed` | `Additional triggers` | `Conditional` | `Manual`

*Since R2025a*

Trigger type. Choose one of these options:

- `Always On` — The fault injects at the start of simulation.
- `Timed` — The fault injects when the simulation time reaches the value you specify for the **Trigger fault at time** parameter.
- `Additional triggers` — The fault injects as result
  of additional triggers not available in the block dialog box. Select this option
  and click the **Open fault properties** hyperlink to set the
  **Trigger type** to one of these values in the Property
  Inspector:

  - `Conditional` — The fault injects as a result
    of a condition that reflects a behavior associated with a signal.
    Conditionals evaluate the Boolean expression in the
    **Condition** parameter at each time step. To model
    irreversible faults, select the **Trigger stays on once
    activated** parameter in the Property Inspector. The block
    enters the faulted state when the trigger condition becomes true for the
    first time and remains in the faulted state for the rest of the
    simulation. To model reversible faults, clear the **Trigger
    stays on once activated** parameter. The block enters the
    faulted state when the trigger condition is true and enters the
    unfaulted state when the trigger condition is false. To learn more, see
    Create and Manage Conditionals.
  - `Manual` — The fault injects or clears when
    you toggle the status in the **Fault Dashboard** pane.
    To learn more, see Manually Trigger Faults in Models.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for
the **Additional resistance fault** parameter.

### **Trigger fault at time** — Time before entering faulted state `0` `s` (default) | nonnegative scalar

*Since R2025a*

Simulation time at which the block enters the faulted state.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for
the **Additional resistance fault** parameter and set
**Trigger type** to `Timed`.

### **Trigger Configuration** — Option to enable additional trigger types for exothermic reactions fault `Open fault properties`

*Since R2025a*

Option to enable additional trigger types not available in the block dialog box. To set the
**Trigger type** parameter to `Conditional` or
`Manual`, click the **Open fault properties**
hyperlink and set the **Trigger type** in the Property Inspector.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for
the **Additional resistance fault** parameter and set
**Trigger type** to `Additional
Triggers`.

## Libraries

Simscape / Battery / Cells

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

### R2025a: Inject additional resistance fault and configure fault behaviors

The Battery Single Particle block now supports the new
interface for modeling faults. This interface separates the system model files from files
that store the fault information. You can systematically model the fault as an open-circuit
cell when the additional series-connected resistance is high (greater than 1000 ohm) or when
there is an abnormal internal resistance. You can also safely separate the nominal model
behavior from the faulted model behavior to avoid safety tasks interfering with design
tasks. For more information, see Introduction to Simscape Faults.

### R2025a: Specify open-circuit potentials normalized to absolute stoichiometry

The new **Stoichiometry breakpoints specification** parameter allows
you to specify the open-circuit potentials of the electrodes normalized to either the
relative or absolute stoichiometry. To specify the open-circuit potentials normalized to the
absolute stoichiometry, set **Stoichiometry breakpoints specification** to
`Absolute`. The block then exposes these four parameters:

- **Absolute anode stoichiometry breakpoints**
- **Anode open-circuit potential relative to absolute
  stoichiometry**
- **Absolute cathode stoichiometry breakpoints**
- **Cathode open-circuit potential relative to absolute
  stoichiometry**

## Description

Battery model with single-particle approach

The Battery Single Particle block represents a battery by
using a single-particle model. This implementation considers the ohmic and mass transport
overpotentials in both the liquid electrolyte and solid electrode phases. Additionally, it
considers the reaction kinetics and the current collector resistance.

The battery comprises two electrodes, the anode and cathode, and a porous separator
between the electrodes. In this block, the *anode* refers to the negative
electrode during discharge and the *cathode* refers to the positive
electrode during discharge. The block models the ohmic overpotentials of the electrodes and
electrolyte, as well as the concentration across the cell cross section from the anode current
collector to the cathode current collector, in a one-dimensional framework.

This figure illustrates a representative concentration in the electrolyte during
discharge. The model comprises the anode (*x*=[0 …
*L*-]), the separator
(*x*=[*L*- …
*L*-+*L*sep])
and the cathode
(*x*=[*L*-+*L*sep…
*L*-+*L*sep+*L*+]).

Representative concentration in the electrolyte during discharge. The model comprises the anode, the separator, and the cathode.

The block calculates the concentration in the electrodes in representative spherical
particles across the radial dimension *r*. This figure shows the
concentration gradient in the representative particles during a continuous discharge of the
battery:

Concentration gradient in the representative particles during a continuous discharge of the battery.

### Species Conservation in Solid Phase

When the block is in solid phase, the single-particle approach models the positive and
negative electrodes as a single representative spherical particle.

**Note**

The superscripts in these equations refer to the respective electrodes. A
*+* superscript refers to the cathode. A *-*
superscript refers to the anode. A *sep* superscript refers to the
separator. A *±* superscript means that the equation applies to both
anode and cathode. For example,
*c+s* is the
solid-phase concentration of the cathode and
*c-s* is the
solid-phase concentration of the anode.

This equation uses Fick's law to describe the concentration, *c*, of
the cation in the negative or positive electrode. The block uses the radial coordinates only
to calculate the concentration in the electrodes. The diffusion in the spherical particle
drives the mass transfer,

∂cs±∂t(r,t)=∂∂r[Ds±∂cs±∂r(r,t)],

where:

- *cs* is the solid-phase
  concentration.
- *Ds* is the diffusion coefficient in solid
  phase.
- *r* is the radius.
- *t* is the time.

At the center of the particle, the concentration gradient is equal to 0:

Ds±∂cs±∂r(0,t)=0.

This equation calculates the ion concentration gradient at the surface of the particle:

Ds±∂cs±∂r(Rs±,t)=∓Js±as± F.

In this equation, *F* is Faraday's constant, and
*J* is the molar flux,

J±(t)=I(t)A L±,

where:

- *I* is the current applied to the cell.
- *A* is the total area of the current collector.
- *L* is the length of the respective electrode.

Additionally, *a* is the active surface area per electrode
unit volume,

a±=3ε±R±,

where:

- *ε* is the active material fraction of the electrode.
- *R* is the total radius of the active particle.

To solve the differential equation, the Battery Single
Particle block discretizes the particle with the radius
*R* into *n* shells. Each shell has a radial distance
equal to δr=Rn from the adjacent spheres.

For the *i*th sphere, this equation calculates the rate of change of
concentration, *δc/δt*:

c˙si=Dsδr2{(i−1i)csi−1−2csi+(i+1i)csi+1}.

For the innermost shell in the particle, the block implements this boundary condition:

c˙1=2Dsδr2{cs2−cs1}.

To implement the boundary condition at the surface of the particle, the block adds an
additional node around the surface. The block does not calculate the concentration of this
node because it does not physically exist. The block uses this node to calculate the
boundary condition between the outermost shell in the particle and the non-existent shell
around it by using the Neumann boundary condition. This equation describes the discretized
result at the surface of the particle:

c˙send=2Dsδr2{csend−1−csend}−2n+1nJF A δr.

### Mass Transport Overpotential in Solid Phase

When the block is in solid phase, the open-circuit potential depends on the
concentration. To calculate the mass transport overpotential at the electrodes, the
Battery Single Particle block subtracts the open-circuit
potential of the average relative concentration in the particle from the open-circuit
potential of the average relative concentration at the surface,

η±diffusion,s=ocp±(cs,surface,relative±)−ocp±(c¯s,relative±),

where:

- *η*diffusion,*s*
  is the solid-phase mass transport overpotential.
- *ocp(cs*,surface,relative*)*
  is the open-circuit potential for the concentration at the surface of the
  particle.
- *ocp(cs*relative*)*
  is the open-circuit potential for the average concentration of the particle.

The block uses the same equation to calculate the mass transport
overpotential for both the anode and the cathode.

### Ohmic Overpotential in Solid Phase

To calculate the ohmic overpotential when the block is in the solid phase, the
Battery Single Particle block linearly approximates the
current across the electrodes and the current at the current collector to a value equal to
the electric current applied to the cell. The current at the interface between the current
separator and the electrode is zero. This equation defines the ohmic overpotential in the
solid phase,

η±ohmic,s=Ibatt2A∗L±κ±,

where:

- *ηohmic,s* is the solid-phase ohmic
  overpotential.
- *Ibatt/A* is the cell cross
  section.
- *L* is the length of the respective electrode and depends on the
  thickness of the anode or cathode.
- *κ* is the conductivity. The conductivity depends on the
  temperature of the cell. *κ* is equal to the **Anode
  conductivity** parameter when the block calculates the ohmic overpotential
  of the anode and is equal to the **Cathode conductivity** parameter
  when the block calculates the ohmic overpotential of the cathode.

The block uses the same equation to calculate the ohmic overpotential in solid phase for
both the anode and the cathode.

### Species Conservation in Liquid Phase

When the block is in liquid phase, this equation describes the concentration in the
electrolyte at both electrodes and at the separator. To calculate the concentration across
the separator, the block considers the diffusive flow induced by concentration gradient,

∂cε±∂t(x,t)=∂∂x[Dε∂cε±∂x(x,t)],

where:

- *cε* is the concentration in the
  electrolyte.
- *Dε* is the diffusion coefficient in
  liquid phase.
- *x* is the location in the thickness of the battery, from the
  anode current collector to the cathode current collector.
- *t* is the time.

At the positive and negative electrodes, the block considers both the diffusive flow and
the cation flux from the solid electrode into the electrolyte,

∈ε±∂cε±∂t(x,t)=∂∂x[Dεeff∂cε±∂x(x,t)±(1−t+0)JF],

where:

- *∈* is the volume fraction of the electrolyte.
- *Deffε* is the
  diffusion coefficient in the liquid phase that considers the porosity of the material.
  The diffusivity of the liquid electrolyte depends on the properties of the surrounding
  solid electrode material. The electrode comprises multiple components, such as the
  active material and the filler, that form a characteristic porous material.
- *J* is the molar flux.
- *t+* is the transference number of the
  cation.
- *F* is Faraday's constant.

Because the electrolyte is a continuous fluid, the cation concentration at the border
between the negative and positive electrodes and the separator must be equal. For the
concentration in the electrolyte at the anode-separator and cathode-separator interfaces,
the block must define the boundary conditions between the three sections of the battery. The
block represents both electrodes and the separator as cuboids.

This block considers the electrolyte as a continuous medium across the electrodes and
the separator. Because the concentrations on both sides of the interface must be equal, a
continuity boundary condition exists for the interface between the electrodes and the
separator.

This equation describes the continuity boundary condition for the concentration at the
interface between the anode and the separator,

cε−(L−,t)=cεsep(L−,t),

where:

- cε−(L−,t) is the concentration in the anode at the border between the anode
  and the separator.
- cεsep(L−,t) is the concentration in the separator at the border between the
  anode and the separator.

This equation describes the continuity boundary condition for the concentration at the
interface between separator and cathode,

cεsep(L−+Lsep,t)=cε+(L−+Lsep,t),

where:

- cεsep(L−+Lsep,t) is the concentration in the separator at the border between the
  separator and the cathode.
- cε+(L−+Lsep,t) is the concentration in the cathode at the border between the
  separator and the cathode.

The block also applies a flux boundary condition to the interfaces between the
electrodes and the separator. The flux at both sides of the interface must be equal,

Deff−∂cε−∂x(L−,t)=Deffsep∂cεsep∂x(L−,t)Deff+∂cε+∂x(L−+Lsep,t)=Deffsep∂cεsep∂x(L−+Lsep,t)

where:

- Deff− is the diffusion coefficient of the anode.
- Deff+ is the diffusion coefficient of the cathode.
- Deffsep is the diffusion coefficient of the separator.
- ∂cε−∂x(L−,t) is the concentration gradient of the anode at the border between the
  anode and the separator.
- ∂cεsep∂x(L−,t) is the concentration gradient of the separator at the border between
  the anode and the separator.
- ∂cε+∂x(L−+Lsep,t) is the concentration gradient of the cathode at the border between
  the cathode and the separator.
- ∂cεsep∂x(L−+Lsep,t) is the concentration gradient of the separator at the border between
  the cathode and the separator.

This equation specifies the concentration at the boundaries between the electrodes and
the current collectors. The flux is proportional to the flux at the current collector, which
is equal to zero because the block does not store any ions there. Hence the resulting flux
at the interface is zero,

∂cε−∂x(0,t)=∂cε+∂x(L−+Lsep+L+,t)=0,

where:

- ∂cε−∂x(0,t) is the concentration gradient in the anode at the border between the
  anode and the leftmost current collector.
- ∂cε+∂x(L−+Lsep+L+,t) is the concentration gradient in the cathode at the border between
  the cathode and the rightmost current collector.

Similar to the solid phase, the block solves the differential equation by dividing the
electrolyte into *n* sections of equal size. This equation expresses the
concentration in the *i*th section with a distance *δx*
between sections, and is valid for all [1,Ms-1] sections:

∂cε∂t(x,t)=Dε,eff±ci+1+ci−1−2ci∂x2+(1−t+0)JF.

The block discretizes the separator using the equation:

∂cε∂t(x,t)=Dε,effsepci+1+ci−1−2ciδx2.

To calculate the concentrations at the interfaces between the electrodes
and the separator, the block applies all the boundary conditions. For example, for the
interface between the anode and the separator, the block applies the equation:

cε,i=1sep=εε−εεsepcε,i=0−cε,i=−1sep∂x∂x−cε,i=0.

### Mass Transport Overpotential in Liquid Phase

When the block is in the liquid phase, it uses the concentrations at the interfaces
between the current collector and the anode and at the interfaces between the cathode and
the current collector to calculate the mass transport overpotential in the electrolyte using
the equation,

ηdiffusion,ε=2RTF(1−tε0)lncε(L−+Lsep+L+,t)cε(0,t),

where:

- *R* is the universal gas constant.
- *T* is the temperature.
- *F* is Faraday's constant.

### Ohmic Overpotential in Liquid Phase

When the block is in the liquid phase, it calculates the ohmic overpotential by linearly
approximating the ionic current in each section of the battery. For the electrodes, the
ionic current at the interface to the current collector is zero. At the interface to the
separator, the ionic current is equal to the electric current of the battery,
*Ibatt*. Across the separator, the block
approximates the ionic current as constant and equal to the electric current applied to the
battery. The block calculates the ohmic overpotential using the equation

ηohmic,ε=−Ibatt2A∗(L+κeff++2Lsepκeffsep+L−κeff−),

where *κeff* is the effective
conductivity that the block calculates by using the Bruggeman coefficient. For more
information about effective parameters, see the Effective Electrolyte Properties section.

### Charge Transfer Overpotential

To model the charge transfer overpotential, this block uses the Butler-Volmer equation.
The Butler-Volmer equation describes the relationship between the current density,
*j*, and the overpotential, *η*, which is the difference
between the actual electrode potential and the thermodynamic equilibrium potential. The
Butler-Volmer equation is

J±(t)=j0,k(t)[exp(αnεFRTη±(t))−exp(−(1−α)nεFRTη±(t))],

where:

- *α* is the charge transfer coefficient for the oxidation and
  reduction.
- *j0* is the exchange current
  density.

Solving the equation for the electrode overpotential results in these equations:

ηkinetic,s=RTαFln(ξ±+(ξ±)2+1)ξ±=j±2a±i0±

*i±0* is the exchange
current density in the anode and in the cathode and is equal to

i0±=k±[c¯ε±(cs,max±−cs,surf±)cs,surf±]α,

where:

- *k* is the charge transfer rate constant and is equal to the
  value of the **Charge transfer rate constant for Anode** parameter
  for the anode and to the value of the **Charge transfer rate constant for
  Cathode** parameter for the cathode.
- c¯ε± is the average electrolyte concentration.
- *cs,max* is the maximum electrode
  concentration.
- *cs,surf* is the electrode surface
  concentration.

To calculate the kinetic overpotential of the complete cell, the block subtracts the
kinetic overpotential at the anode from the kinetic overpotential at the cathode:

ηkinetic,s=η+kinetic,s−η−kinetic,s.

### Current Collector Resistance

This block models the current collector resistance as a single resistance. You can set
the current collector resistance by specifying the **Current collector
resistance** parameter.

### Cell Voltage

To model the cell voltage, this block considers the potentials at the surfaces of each
electrode, the overpotentials, and the voltage loss due to the current collector resistance
by using the equation

V(t)=ocp+(csurface,relative+)−ocp−(csurface,relative−)+ηdiffusion,ε+ηohmic,ε+ηkinetic,s+ηohmic−+ηohmic++IbattRCurrentCollector,

where:

- *ocp+(c+surface,relative)*
  is the open-circuit potential for the concentration at the surface of the cathode
  particle.
- *ocp-(c-surface,relative)*
  is the open-circuit potential for the concentration at the surface of the anode
  particle.
- *η*diffusion,ε is the mass transport
  overpotential in the electrolyte.
- *η*ohmic,ε is the ohmic overpotential in
  the electrolyte.
- *η*kinetic,s is the charge transfer
  overpotential in the electrodes.
- *η*-ohmic is
  the ohmic overpotential in the anode.
- *η*+ohmic is
  the ohmic overpotential in the cathode.
- *I*batt is the battery current.
- *R*CurrentCollector is the resistance of
  the current collector.

You can parameterize the open-circuit potential as table data by using
normalized or absolute stoichiometry breakpoints:

- If you set the **Stoichiometry breakpoints specification**
  parameter to `Normalized`, you specify the open-circuit
  potentials normalized to the relative stoichiometry by setting the **Anode
  open-circuit potential**, **Cathode open-circuit
  potential**, and **Normalized stoichiometry breakpoints**
  parameters. The stoichiometry breakpoints are identical for both the anode and the
  cathode.
- If you set the **Stoichiometry
  breakpoints specification** parameter to
  `Absolute`, you specify the open-circuit potentials
  normalized to the absolute stoichiometry. With this option, you can specify the
  stoichiometry breakpoints for the anode and the cathode independently by setting the
  **Absolute anode stoichiometry breakpoints** and **Absolute
  cathode stoichiometry breakpoints** parameters.  *(since R2025a)*

To calculate the relative concentration, the block considers the maximum concentration
and the maximum and minimum stoichiometry of each electrode. The **Anode maximum ion
concentration** and the **Cathode maximum ion concentration**
parameters represent the theoretically possible maximum concentration of each electrode. To
obtain the achievable maximum and minimum concentrations, the block multiplies the values of
these parameters with the value of the **Anode maximum stoichiometry**,
**Anode minimum stoichiometry**, **Cathode maximum
stoichiometry**, and **Cathode minimum stoichiometry**
parameters, respectively. Then, the block calculates the relative concentration by using the equation

cs,relative=cscs,max−ΝminΝmax−Νmin,

where:

- *cs*,max is the
  maximum concentration.
- *N*max is the maximum
  stoichiometry.
- *N*min is the minimum
  stoichiometry.

### Effective Electrolyte Properties

Set the values of these parameters based on the microstructure of the porous electrodes
you want to model:

- **Diffusion coefficient of electrolyte** — Set this parameter to
  the value of the diffusion coefficient of the electrolyte that influences the mass
  transport in the electrolyte.
- **Electrolyte conductivity** — Set this parameter to the value of the
  conductivity of the electrolyte.

To model this dependency, this block uses the Bruggeman correlation,

Parametereffective=Parameterblock∗φεα,

where:

- *φε* is the volume fraction of the
  electrolyte. This value is equal to the value of the **Volume fraction of
  electrolyte in anode**, **Volume fraction of electrolyte in
  separator**, and **Volume fraction of electrolyte in
  cathode** parameters, accordingly.
- *α* is the Bruggeman exponent. This value is equal to the value
  of the **Anode Bruggeman exponent**, **Separator Bruggeman
  exponent**, and **Cathode Bruggeman exponent** parameters,
  accordingly.

### Thermal

The block considers the temperature constant across the cell. These block parameters
depend on the temperature of the cell:

- **Diffusion coefficient of anode active material** and
  **Diffusion coefficient of cathode active material**— These
  parameters are the diffusion coefficients of electrodes that influence the mass
  transport in the electrodes.
- **Diffusion coefficient of electrolyte** — This parameter is the
  diffusion coefficient of electrolyte that influences the mass transport in the
  electrolyte.
- **Electrolyte conductivity** — This parameter is the conductivity of
  the electrolyte.
- **Anode conductivity** and **Cathode
  conductivity** — These parameters are the conductivity of the
  electrodes.
- **Charge transfer rate constant for Anode** and **Charge
  transfer rate constant for Cathode** — These parameters are the charge
  transfer rate constants of the electrodes.

To calculate the temperature-adjusted values of these parameters, the block
uses the Arrhenius equation,

ParameterT-adjusted=Parameterblock∗eEaR(1Tref−1T),

where:

- *Parameterblock* is the value of the
  temperature-dependent parameters.
- *Ea* is the activation energy and is equal
  to the value of the activation energy parameters in the **Thermal**
  settings.
- *Tref* is the value of the
  **Arrhenius reference temperature** parameter.
- *T* is the battery temperature.

### Heat Generation of Battery

This block models the battery as a lumped thermal mass. The single-particle model
calculates the irreversible heat generation that the overpotentials cause in the battery by
using this equation:

Q=Ibatt(ηdiffusion,ε+ηohmic,ε+ηohmic,s−+ηohmic,s++IbattRCurrentCollector+ηkinetic,s+η+diffusion+η−diffusion).

### Model Faults

*Since R2025a*

To model a fault in the Battery Single Particle block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

The Battery Single Particle block models the fault as an
open-circuit cell when the additional series-connected resistance is high (greater than 1000
ohm) or when there is an abnormal internal resistance.

**Fault Triggers**

You specify how and when faults occur by using the **Trigger Type**
parameter.

If you set the **Trigger Type** parameter to
`Timed`, the Battery Single Particle block triggers fault events when the
simulation time reaches the value you specify for the **Trigger fault at
time** parameter.

If you set the **Trigger
Type** to `Conditional`, you can choose whether faults
in the Battery Single Particle block are reversible *(since R2025a)*. To model irreversible faults, click
**Open fault properties** to open the Property Inspector and select the
**Trigger stays on once activated** parameter. The block enters the faulted
state when the trigger condition becomes true for the first time and remains in the faulted
state for the rest of the simulation. To model reversible faults, clear the **Trigger
stays on once activated** parameter. The block enters the faulted state when the
trigger condition is true and enters the unfaulted state when the trigger condition is
false.

For more information about adding faults to blocks and
specifying fault triggers, see Introduction to Simscape Faults.

### Public Variables

You can use the Probe
block to access these variables in the Battery Single
Particle block. The units are the default values.

- `anodeModel.averageStoichiometry` — Average stoichiometry in
  the anode.
- `anodeModel.massTransportOverpotential` — Mass transport
  overpotential, in volts.
- `anodeModel.normalizedAverageStoichiometry`  — Average
  stoichiometry normalized to the minimum and maximum values.
- `anodeModel.normalizedSurfaceStoichiometry` — Surface
  stoichiometry normalized to the minimum and maximum values.
- `anodeModel.ohmicOverpotential` — Ohmic overpotential of the
  anode, in volts.
- `anodeModel.shellConcentration`  — Concentration of the modeled
  shells, in mol/m^3. The number of shells is equal to the value of the **Anode
  Shell Count** parameter.
- `anodeModel.shellStoichiometry`  — Stoichiometry of the modeled
  shells. The number of shells is equal to the **Anode Shell Count**
  parameter.
- `anodeModel.surfaceConcentration`  — Concentration at the
  surface of the particle, in mol/m^3.
- `anodeModel.surfacePotential`  — Potential at the surface of
  the particle, in volts.
- `anodeModel.temperatureAdjustedConductivity`  — Conductivity
  adjusted to the battery temperature, in S/m.
- `anodeModel.temperatureAdjustedDiffusionCoefficient`  —
  Diffusion coefficient adjusted to the battery temperature, in m^2/s.
- `averageElectrolyteConcentration` — Average concentration in
  the particle, in mol/m^3.
- `batteryCurrent` — Total current measured through the battery
  terminals, in amperes.
- `batteryTemperature` — Battery average temperature that the
  block uses for the table lookup of resistances and open-circuit voltage. If you set
  the **Thermal model** parameter to `Constant
  temperature`, the `batteryTemperature` variable is
  equal to the specified temperature value. If you set the **Thermal
  model** parameter to `Lumped thermal mass`, the
  `batteryTemperature` variable is a differential state that varies
  during the simulation.
- `batteryVoltage` — Battery terminal voltage, or the voltage
  difference between the positive and the negative terminals, in volts.
- `cathodeModel.averageStoichiometry` — Average stoichiometry in
  the cathode.
- `cathodeModel.massTransportOverpotential` — Mass transport
  overpotential, in volts.
- `cathodeModel.normalizedAverageStoichiometry`  — Average
  stoichiometry normalized to the minimum and maximum values.
- `cathodeModel.normalizedSurfaceStoichiometry` — Surface
  stoichiometry normalized to the minimum and maximum values.
- `cathodeModel.ohmicOverpotential` — Ohmic overpotential of the
  cathode, in volts.
- `cathodeModel.shellConcentration`  — Concentration of the
  modeled shells, in mol/m^3. The number of shells is equal to the value of the
  **Anode Shell Count** parameter.
- `cathodeModel.shellStoichiometry`  — Stoichiometry of the
  modeled shells. The number of shells is equal to the **Anode Shell
  Count** parameter.
- `cathodeModel.surfaceConcentration`  — Concentration at the
  surface of the particle, in mol/m^3.
- `cathodeModel.surfacePotential`  — Potential at the surface of
  the particle, in volts.
- `cathodeModel.temperatureAdjustedConductivity`  — Conductivity
  adjusted to the battery temperature, in S/m.
- `cathodeModel.temperatureAdjustedDiffusionCoefficient`  —
  Diffusion coefficient adjusted to the battery temperature, in m^2/s.
- `electrolyteModel.averageConcentration` — Average concentration
  in the electrolyte across the whole cell, in mol/m^3.
- `electrolyteModel.averageConcentrationAnode` — Average
  concentration in the electrolyte inside the anode, in mol/m^3.
- `electrolyteModel.averageConcentrationCathode` — Average
  concentration in the electrolyte inside the cathode, in mol/m^3.
- `electrolyteModel.averageConcentrationSeparator` — Average
  concentration in the electrolyte inside the separator, in mol/m^3.
- `electrolyteModel.concentrationAnode` — Concentration of the
  modeled layers of the electrolyte in the anode, in mol/m^3. The number of elements is
  equal to the **Electrolyte layer count of anode** parameter.
- `electrolyteModel.concentrationCathode` — Concentration of the
  modeled layers of the electrolyte in the cathode, in mol/m^3. The number of elements
  is equal to the **Electrolyte layer count of cathode**
  parameter.
- `electrolyteModel.concentrationSeparator` — Concentration of
  the modeled layers of the electrolyte in the separator, in mol/m^3. The number of
  elements is equal to the **Electrolyte layer count of electrolyte**
  parameter.
- `electrolyteModel.currentDensityAnode` — Current density in the
  anode, in A/m^3.
- `electrolyteModel.currentDensityCathode` — Current density in
  the cathode, in A/m^3.
- `electrolyteModel.diffusionCoefficientAnode` —
  Temperature-adjusted effective diffusion coefficient of the electrolyte in the anode,
  in m^s/s.
- `electrolyteModel.diffusionCoefficientCathode` —
  Temperature-adjusted effective diffusion coefficient of the electrolyte in the
  cathode, in m^s/s.
- `electrolyteModel.diffusionCoefficientSeparator` —
  Temperature-adjusted effective diffusion coefficient of the electrolyte in the
  separator, in m^s/s.
- `electrolyteModel.conductivityAnode` — Temperature-adjusted
  effective conductivity of the electrolyte in the anode, in S/m.
- `electrolyteModel.conductivityCathode` — Temperature-adjusted
  effective conductivity of the electrolyte in the cathode, in S/m.
- `electrolyteModel.effectiveConductivitySeparator` —
  Temperature-adjusted effective conductivity of the electrolyte in the separator, in
  S/m.
- `electrolyteModel.massTransportOverpotential` — Mass transport
  overpotential of the electrolyte, in volts.
- `electrolyteModel.ohmicOverpotential` — Ohmic overpotential of
  the electrolyte, in volts.
- `electrolyteModel.temperatureAdjustedConductivity` —
  Temperature-adjusted conductivity of the electrolyte, in S/m.
- `electrolyteModel.temperatureAdjustedDiffusionCoefficient` —
  Temperature adjusted diffusion coefficient of the electrolyte, in m^s/s.
- `heatGenerationRate` — Total battery heat generation rate, in
  watts. The block calculates the heat generation rate by adding the resistive losses
  and the reversible heating contributions.
- `power_dissipated` — Resistive heat generation rate or
  dissipated power, in watts.
- `reactionKineticsModel.chargeTransferOverpotential` — Charge
  transfer overpotential of the battery, in volts.
- `reactionKineticsModel.exchangeCurrentDensityAnode` — Exchange
  current density in the anode, in C/(m^2\*s).
- `reactionKineticsModel.exchangeCurrentDensityCathode` —
  Exchange current density in the cathode, in C/(m^2\*s).
- `reactionKineticsModel.temperatureAdjustedChargeTransferRateAnode`
  — Temperature-adjusted charge transfer rate constant for the anode, in
  m^(5/2)/(mol^(1/2) \* s).
- `reactionKineticsModel.temperatureAdjustedChargeTransferRateCathode`
  — Temperature-adjusted charge transfer rate constant for the cathode, in
  m^(5/2)/(mol^(1/2) \* s).
- `stateOfCharge` — Battery state of charge obtained from Coulomb
  counting.
- `thermalModel.batteryTemperature` — Temperature of the battery,
  in K.
- `thermalModel.cellTemperature` — Temperature output by the
  cell.
- `thermalModel.heatDissipationRate` — Heat dissipation rate of
  the battery, in watts.
- `thermalModel.heatGeneration` — Heat that the battery
  generates, in watts.
- `thermalModel.thermalMass` — Thermal mass of the battery, in
  J/K.
