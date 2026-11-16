---
type: simulink-block
title: 'Heat Exchanger Interface (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Fundamental Components'
documentation_page: 'heatexchangerinterfacetl'
documentation_source_path: 'ref/heatexchangerinterfacetl.html'
language: en
---

# Heat Exchanger Interface (TL)

## Ports

### Output

### **C** — Heat capacity rate physical signal

Physical signal output port for the thermal capacity rate of the thermal
liquid.

### **HC** — Heat transfer coefficient physical signal

Physical signal output port for the heat transfer coefficient between the thermal
liquid and the interface wall.
### Conserving

### **A** — Thermal liquid port thermal liquid

Thermal liquid conserving port representing the thermal liquid inlet.

### **B** — Thermal liquid port thermal liquid

Thermal liquid conserving port representing the thermal liquid outlet.

### **H** — Thermal inlet temperature thermal

Thermal conserving port associated with the thermal liquid inlet
temperature.

## Parameters

### **Minimum free-flow area** — Cross-sectional area of flow channel at its narrowest point `0.01 m^2` (default) | scalar

Smallest total cross-sectional flow area between inlet and outlet. If the channel is
a collection of ducts, tubes, slots, or grooves, the value of this parameter is the sum
of the smallest areas at the minimum flow area point. This parameter is the area where
the fluid velocity is highest. For example, if the fluid flows perpendicular to a bank
of tubes, the value of this parameter is the sum of the gaps between the tubes in one
cross-section where the sum of the gaps is smallest is smallest.

### **Hydraulic diameter for pressure loss** — Diameter or equivalent diameter of channel `0.1 m` (default) | scalar

Hydraulic diameter of the tubes or channels comprising the heat exchange interface.
The hydraulic diameter is the ratio of the flow cross-sectional area to the channel
perimeter.

### **Thermal liquid volume** — Total volume of fluid contained in flow channel `0.01 m^3` (default) | scalar with units of length squared

Total volume of the fluid contained in the thermal liquid flow channel.

### **Laminar flow upper Reynolds number limit** — Start of transition between laminar and turbulent regimes `2000` (default) | scalar

Start of the transition from the laminar regime to the turbulent regime. Above this
number, inertial forces become increasingly dominant. The default value is given for
circular pipes and tubes with smooth surfaces.

### **Turbulent flow lower Reynolds number limit** — End of transition between laminar and turbulent regimes `4000` (default) | scalar

End of the transition from the laminar regime to the turbulent regime. Below this
number, viscous forces become increasingly dominant.

### **Pressure loss model** — Mathematical model for pressure loss due to friction `Pressure loss coefficient` (default) | `Correlation for flow inside tubes` | `Tabulated data - Darcy friction factor vs. Reynolds number` | `Tabulated data - Euler number vs. Reynolds number`

Mathematical model for pressure loss due to friction. This setting determines which
expressions to use for calculation and which block parameters to specify as input. See
the Heat Exchanger Interface (TL) blocks
for the calculations by parameterization.

### **Pressure loss coefficient** — Aggregate loss coefficient for all flow resistances between the ports `0.1` (default) | scalar

Aggregate loss coefficient for all flow resistances in the flow channel, including
wall friction (major losses) and local resistances due to bends, elbows, and other
geometry changes (minor losses).

The loss coefficient is an empirical, dimensionless number used to express the
pressure losses due to friction. It can be calculated from experimental data or obtained
from product data sheets.

#### Dependencies

To enable this parameter, set **Pressure loss model** to
`Pressure loss coefficient`.

### **Length of flow path from inlet to outlet** — Distance traveled from port to port `1 m` (default) | scalar with units of length

Total distance the flow must travel between the ports. In multi-pass shell-and-tube
exchangers, the total distance is the sum over all shell passes. In tube bundles,
corrugated plates, and other channels where the flow is split into parallel branches, it
is the distance covered in a single branch. The longer the flow path, the steeper the
major pressure loss due to friction at the wall.

#### Dependencies

To enable this parameter, set **Pressure loss model** to
`Correlation for flow inside tubes` or
`Tabulated data - Darcy friction factor vs Reynolds
number`.

### **Aggregate equivalent length of local resistances** — Aggregate minor pressure loss expressed in length `0.1 m` (default) | scalar

Aggregate minor pressure loss, expressed as a length. The length of a straight
channel results in equivalent losses to the sum of existing local resistances from
elbows, tees, and unions. The larger the equivalent length, the steeper the minor
pressure loss due to the local resistances.

#### Dependencies

To enable this parameter, set **Pressure loss model** to
`Correlation for flow inside tubes`.

### **Internal surface absolute roughness** — Mean height of wall surface variations that contribute to frictional losses `15e-6 m` (default) | scalar with units of length

Average height of all surface defects on the internal surface of the pipe. The
surface roughness enables the calculation of the friction factor in the turbulent flow
regime.

#### Dependencies

To enable this parameter, set **Pressure loss model** to
`Correlation for flow inside tubes`.

### **Laminar friction constant for Darcy friction factor** — Pressure loss correction for flow cross section in laminar flow conditions `64` (default) | scalar

Pressure loss correction for laminar flow. This parameter is referred to as the
shape factor, and can be used to derive the Darcy friction factor for pressure loss
calculations in the laminar regime. The default value is for cylindrical pipes and
tubes.

Some additional shape factors for non-circular cross-sections can be determined from
analytical solutions to the Navier-Stokes equations. A square duct has a shape factor of
`56`, a rectangular duct with an aspect ratio of 2:1 has a shape
factor of `62`, and an annular tube has a shape factor of
`96`. A slender conduit between parallel plates also has a shape
factor of `96`.

#### Dependencies

To enable this parameter, set **Pressure loss model** to
`Correlation for flow inside tubes`.

### **Reynolds number vector for Darcy friction factor** — Reynolds number at each breakpoint in Darcy friction factor lookup table `[400, 1000, 1500, 3000, 4000, 6000, 10000, 20000, 40000, 60000, 100000, 100000000]` (default) | array

Vector of Reynolds numbers at which to specify the Darcy friction factor. The block
uses this vector to create a lookup table for the Darcy friction factor.

#### Dependencies

To enable this parameter, set **Pressure loss model** to
`Tabulated data - Darcy friction factor vs. Reynolds
number`.

### **Darcy friction factor vector** — Darcy friction factor at each breakpoint in Reynolds number lookup table `[.264, .112, .071, .0417, .0387, .0268, .025, .0232, .0226, .022, .0214, .0214]` (default) | array

Vector of Darcy friction factors corresponding to the values specified in the
**Reynolds number vector for Darcy friction factor** parameter. The
block uses this vector to create a lookup table for the Darcy friction factor.

#### Dependencies

To enable this parameter, set **Pressure loss model** to
`Tabulated data - Darcy friction factor vs. Reynolds
number`.

### **Reynolds number vector for Euler number** — Reynolds number at each breakpoint in the Euler number lookup table `[50, 500, 1000, 2000]` (default) | array

Vector of Reynolds numbers at which to specify the Euler number. The block uses
this vector to create a lookup table for the Euler number.

#### Dependencies

To enable this parameter, set **Pressure loss model** to
`Tabulated data - Euler number vs. Reynolds number`.

### **Euler number vector** — Euler number at each breakpoint in the Reynolds number lookup table `[4.4505, .6864, .4791, .3755]` (default) | array

Vector of Euler numbers corresponding to the values specified in the
**Reynolds number vector for Euler number** parameter. The block uses
this vector to create a lookup table for the Euler number.

#### Dependencies

To enable this parameter, set **Pressure loss model** to
`Tabulated data - Euler number vs. Reynolds number`.

### **Heat transfer coefficient model** — Mathematical model for heat transfer between fluid and wall `Constant heat transfer coefficient` (default) | `Correlation for flow inside tubes` | `Tabulated data - Colburn factor vs. Reynolds number` | `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`

Parameterization used to compute the heat transfer rate between the heat exchanger
fluids. You can assume a constant pressure loss coefficient, use empirical correlation
for flow inside tubes, or specify tabulated data for the Colburn or Nusselt number.

### **Liquid-wall heat transfer coefficient** — Heat transfer coefficient for convection between fluid and wall `100 W/(m^2 * K)` (default) | scalar

Heat transfer coefficient between the thermal liquid and the heat-transfer
surface.

#### Dependencies

To enable this parameter, set **Heat transfer coefficient model**
to `Constant heat transfer coefficient`.

### **Heat transfer surface area** — Effective surface area used in heat transfer between fluid and wall `0.4 m^2` (default) | scalar with units of length squared

Aggregate surface area available for heat transfer between the heat exchanger
fluids.

### **Length of flow path for heat transfer** — Characteristic length traversed in heat transfer between fluid and wall `1 m` (default) | scalar with units of length

Distance traversed by the fluid along which heat exchange takes place.

#### Dependencies

To enable this parameter, set **Heat transfer coefficient model**
to `Tabulated data - Colburn factor vs. Reynolds number` or
`Tabulated data - Nusselt number vs. Reynolds number and Prandtl
number`.

### **Nusselt number for laminar flow heat transfer** — Constant assumed for Nusselt number in laminar flow `3.66` (default) | positive scalar

Proportionality constant between convective and conductive heat transfer in the
laminar regime. This parameter enables the calculation of convective heat transfer rates
in laminar flows. The appropriate value to use depends on component geometry.

#### Dependencies

To enable this parameter, set **Heat transfer coefficient model**
to `Correlation for flow inside tubes`.

### **Reynolds number vector for Colburn factor** — Reynolds number at each breakpoint in Colburn factor lookup table `[100, 150, 1000]` (default) | array

Vector of Reynolds numbers at which to specify the Colburn factor. The block uses
this vector to create a lookup table for the Colburn number. The number of values in
this vector must be equal to the size of the **Colburn factor vector**
parameter to calculate tabulated breakpoints.

#### Dependencies

To enable this parameter, set **Heat transfer coefficient model**
to `Tabulated data - Colburn factor vs. Reynolds
number`.

### **Colburn factor vector** — Colburn factor at each breakpoint in Reynolds number lookup table `[.019, .013, .002]` (default) | array

Vector of Colburn factors corresponding to the values specified in the
**Reynolds number vector for Colburn number** parameter. The block
uses this vector to create a lookup table for the Colburn factor.

#### Dependencies

To enable this parameter, set **Heat transfer coefficient model**
to `Tabulated data - Colburn factor vs. Reynolds
number`.

### **Reynolds number vector for Nusselt number** — Reynolds number at each breakpoint in Nusselt number lookup table `[100, 150, 1000]` (default) | array

Vector of Reynolds numbers at which to specify the Nusselt number. The block uses
this vector to create a lookup table for the Nusselt number.

#### Dependencies

To enable this parameter, set **Heat transfer coefficient model**
to `Tabulated data - Nusselt number vs. Reynolds number and Prandtl
number`.

### **Prandtl number vector for Nusselt number** — Prandtl number at each breakpoint in the Nusselt number lookup table `[1, 10]` (default) | array

Vector of Prandtl numbers at which to specify the Nusselt number. The block uses
this vector to create a lookup table for the Nusselt number.

#### Dependencies

To enable this parameter, set **Heat transfer coefficient model**
to `Tabulated data - Nusselt number vs. Reynolds number and Prandtl
number`.

### **Nusselt number table, Nu(Re,Pr)** — Nusselt number at each breakpoint in Reynolds-Prandtl number lookup table `[3.72, 4.21; 3.75, 4.44; 4.21, 7.15]` (default) | array

Matrix of Nusselt numbers corresponding to the values specified in the
**Reynolds number vector for Nusselt number** and **Prandtl
number vector for Nusselt number** parameters. The block uses this vector to
create a lookup table for the Nusselt factor.

#### Dependencies

To enable this parameter, set **Heat transfer coefficient model**
to `Tabulated data - Nusselt number vs. Reynolds number and Prandtl
number`.

### **Fouling factor** — Increased resistance due to fouling `1e-4 m^2*K/W` (default) | scalar

Empirical parameter used to quantify the increased thermal resistance due to dirt
deposits on the heat transfer surface.

#### Effects and Initial Conditions

### **Enable dynamic compressibility** — Setting for liquid compressibility in heat exchanger `On` (default) | `Off` | scalar

Option to model the pressure dynamics inside the heat exchanger. Setting this
parameter to `Off` removes the pressure derivative terms from
the component energy and mass conservation equations. The pressure inside the heat
exchanger is then reduced to the weighted average of the two port pressures.

### **Thermal Liquid nominal temperature** — Temperature at nominal operating conditions `293.15 K` (default) | scalar

Thermal liquid temperature at nominal operating conditions. The block uses this
value to calculate the nominal density to use in the mass and energy conservation
equation when dynamic compressibility is disabled.

#### Dependencies

To enable this parameter, clear the **Enable dynamic
compressibility** checkbox.

### **Thermal Liquid nominal pressure** — Pressure at nominal operating conditions `0.101325 MPa` (default) | scalar

Thermal liquid pressure at nominal operating conditions. The block uses this value
to calculate the nominal density to use in the mass and energy conservation equation
when dynamic compressibility is disabled.

#### Dependencies

To enable this parameter, clear the **Enable dynamic
compressibility** checkbox.

### **Thermal Liquid initial temperature** — Temperature in the thermal liquid channel at the start of simulation `293.15 K` (default) | scalar with units of temperature

Temperature in the thermal liquid channel at the start of simulation

### **Thermal Liquid initial pressure** — Pressure in the thermal liquid channel at the start of simulation `0.101325 MPa` (default) | scalar with units of pressure

Pressure in the thermal liquid channel at the start of simulation.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**.

## Libraries

Simscape / Fluids / Heat Exchangers / Fundamental Components

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016a**

## Description

Thermal interface between a thermal liquid and its surroundings

The Heat Exchanger Interface (TL) block represents a liquid interface in a
thermal liquid network for heat transfer with other fluids. The block models the pressure drop
and temperature change between the thermal liquid inlet and outlet of a thermal interface and
when combined with the E-NTU Heat Transfer block models the heat transfer
rate across the interface between two fluids.

### Mass Balance

The form of the mass balance equation depends on the dynamic compressibility setting. If
you clear the **Enable dynamic compressibility** checkbox, the mass balance
equation is

m˙A+m˙B=0,

where:

- *m˙A* and *m˙B* are the mass flow rates into the interface through
  ports **A** and **B**.

If you select **Enable dynamic compressibility**, the mass balance
equation is

m˙A+m˙B=(dpdt1β−dTdtα)ρV,

where:

- *p* is the pressure of the thermal liquid volume.
- *T* is the temperature of the thermal liquid volume.
- *ɑ* is the isobaric thermal expansion coefficient of the thermal
  liquid volume.
- *β* is the isothermal bulk modulus of the thermal liquid
  volume.
- *ρ* is the mass density of the thermal liquid volume.
- *V* is the volume of thermal liquid in the heat exchanger
  interface.

### Momentum Balance

The momentum balance in the heat exchanger interface depends on the fluid dynamic
compressibility setting. If you select **Enable dynamic compressibility**,
the momentum balance factors in the internal pressure of the heat exchanger interface
explicitly. The momentum balance in the half volume between port **A** and
the internal interface node is

pA−p=ΔpLoss,A,

while in the half volume between port **B** and the
internal interface node it is

pB−p=ΔpLoss,B,

where:

- *p*A and
  *p*B are the pressures at ports
  **A** and **B**.
- *p* is the pressure in the internal node of the interface
  volume.
- *Δp*Loss,A and
  *Δp*Loss,B are the pressure losses between
  port **A** and the internal interface node and between port
  **B** and the internal interface node.

If you clear the **Enable dynamic compressibility** checkbox, the
momentum balance in the interface volume is computed directly between ports
**A** and **B** as

pA−pB=ΔpLoss,A−ΔpLoss,B.

### Pressure Loss Calculations

The exact form of the pressure loss terms depends on the **Pressure loss
model** setting in the block dialog box. If the pressure loss model is set to
`Pressure loss coefficient`, the pressure loss in the half volume
adjacent to port **A** is

ΔpLoss,A={m˙AμA(CP)LossReL14Dh,pρASMin,ReA≤ReL(CP)Lossm˙A|m˙A|4ρASMin2,ReA≥ReT,

while in the half volume adjacent to port **B** it is

ΔpLoss,B={m˙BμB(CP)LossReL14Dh,pρBSMin,ReB≤ReL(CP)Lossm˙B|m˙B|4ρBSMin2,ReB≥ReT,

where:

- *μ*A and
  *μ*B are the fluid dynamic viscosities at
  ports **A** and **B**.
- *CP*Loss is the **Pressure loss
  coefficient** parameter specified in the block dialog box.
- *Re*L is the Reynolds number upper bound
  for the laminar flow regime.
- *Re*T is the Reynolds number lower bound
  for the turbulent flow regime.
- *D*h,p is the hydraulic diameter for
  pressure loss calculations.
- *ρ*A and
  *ρ*B are the fluid mass densities at ports
  **A** and **B**.
- *S*Min is the total minimum free-flow
  area.

If the pressure loss model is set to `Correlation for flow inside
tubes`, the pressure loss in the half volume adjacent to port
**A** is

ΔpLoss,A={m˙AμAλ(Lpress+Ladd)4Dh,pρASMin,ReA≤ReLfT,A(Lpress+Ladd)4Dh,pm˙A|m˙A|ρASMin2,ReA≥ReT,

while in the half volume adjacent to port **B** it is

ΔpLoss,B={m˙BμBλ(Lpress+Ladd)4Dh,pρBSMin,ReB≤ReLfT,B(Lpress+Ladd)4Dh,pm˙B|m˙B|ρBSMin2,ReB≥ReT,

where:

- *L*press is the flow path length from
  inlet to outlet.
- *L*add is the aggregate equivalent length
  of local resistances.
- *f*T,A and
  *f*T,B are the turbulent-regime Darcy
  friction factors at ports **A** and **B**.

The Darcy friction factor in the half volume adjacent to port **A** is

fT,A=1[−1.8log10(6.9ReA+r3.7Dh,p)1.11]2,

while in the half volume adjacent to port **B** it is

fT,B=1[−1.8log10(6.9ReB+r3.7Dh,p)1.11]2,

where *r* is the internal surface absolute
roughness.

If the pressure loss model is set to `Tabulated data — Darcy friction
factor vs. Reynolds number`, the pressure loss in the half volume adjacent to
port **A** is

ΔpLoss,A={m˙AμAλLpress4Dh,p2ρASMin,ReA≤ReLf(ReA)Lpress4Dh,pm˙A|m˙A|ρASMin2,ReA≥ReT,

while in the half volume adjacent to port **B** it is

ΔpLoss,B={m˙BμBλLpress4Dh,p2ρBSMin,ReB≤ReLf(ReB)Lpress4Dh,pm˙B|m˙B|ρBSMin2,ReB≥ReT,

where:

- *λ* is the shape factor for laminar flow viscous friction.
- *f*(*Re*A) and *f*(*Re*B) are the Darcy friction factors at ports **A** and
  **B**. The block obtains the friction factors from tabulated data
  specified relative to the Reynolds number.

If the pressure loss model is set to `Tabulated data — Euler number
vs. Reynolds number`, the pressure loss in the half volume adjacent to port
**A** is

ΔpLoss,A={m˙AμAEu(ReL)ReL14Dh,pρASMin,ReA≤ReLEu(ReA)m˙A|m˙A|4ρASMin2,ReA≥ReT,

while in the half volume adjacent to port **B** it is

ΔpLoss,B={m˙BμBEu(ReL)ReL14Dh,pρBSMin,ReB≤ReLEu(ReB)m˙B|m˙B|4ρBSMin2,ReB≥ReT,

where:

- *Eu*(*Re*L) is the Euler number at the Reynolds number upper bound for laminar
  flows.
- *Eu*(*Re*A) and *Eu*(*Re*B) are the Euler numbers at ports **A** and
  **B**. The block obtains the Euler numbers from tabulated data
  specified relative to the Reynolds number.

### Energy Balance

The energy balance in the heat exchanger interface depends on the fluid dynamic
compressibility setting. If you select **Enable dynamic compressibility**,
the energy balance is

dpdtdUdp+dTdtdUdT=ϕA+ϕB+QH,

where:

- *U* is the internal energy contained in the volume of the heat
  exchanger interface.
- *ϕ*A and
  *ϕ*B are the energy flow rates through ports
  **A** and **B** into the volume of the heat
  exchanger interface.
- *Q*H is the heat flow rate through port
  **H**, representing the interface wall, into the volume of the heat
  exchange interface.

The internal energy derivatives are defined as

dUdp=[1β(ρu+p)−Tα]V

and

dUdT=[cp−α(u+pρ)]ρV,

where *u* is the specific internal energy of the thermal
liquid, or the internal energy contained in a unit mass of the same.

If you clear the **Enable dynamic compressibility** checkbox, the
thermal liquid density is treated as a constant. The bulk modulus is then effectively
infinite and the thermal expansion coefficient zero. The pressure and temperature
derivatives of the compressible case vanish and the energy balance is restated as

dEdt=ϕA+ϕB+QH,

where *E* is the total internal energy of the
incompressible thermal liquid, or

E=ρuV.

The block calculates *ρ* from the **Nominal
liquid temperature** and **Nominal liquid pressure**
parameters.

### Heat Transfer Correlations

The block calculates and outputs the liquid-wall heat transfer coefficient value. The
calculation depends on the **Heat transfer coefficient specification**
setting in the block dialog box. If the heat transfer coefficient specification is
`Constant heat transfer coefficient`, the heat transfer
coefficient is simply the constant value specified in the block dialog box,

hL−W=hConst,

where:

- *h*L-W is the liquid-wall heat transfer
  coefficient.
- *h*Const is the **Liquid-wall heat
  transfer coefficient value** specified in the block dialog box.

For all other heat transfer coefficient parameterizations, the heat transfer coefficient
is defined as the arithmetic average of the port heat transfer coefficients:

hL−W=hA+hB2,

where:

- *h*A and
  *h*B are the liquid-wall heat transfer
  coefficients at ports **A** and **B**.

The heat transfer coefficient at port **A** is

hA=NuAkADh,heat,

while at port **B** it is

hB=NuBkBDh,heat,

where:

- *Nu*A and
  *Nu*B are the Nusselt numbers at ports
  **A** and **B**.
- *kA* and
  *kB* are the thermal conductivities at
  ports **A** and **B**.
- *Dh,heat* is the hydraulic diameter for
  heat transfer calculations.

The hydraulic diameter used in heat transfer calculations is defined as

Dh,heat=4SMinLheatSheat,

where:

- *L*heat is the flow path length used in
  heat transfer calculations.
- *S*heat is the total heat transfer surface
  area.

### Nusselt Number Calculations

The Nusselt number calculation depends on the **Heat transfer coefficient
specification** setting in the block dialog box. If the heat transfer
specification is set to `Correlation for flow inside tubes`, the
Nusselt number at port **A** is

NuA={NuL,ReA≤ReL(fT,A8)(ReA−1000)PrA1+12.7(fT,A8)1/2(PrB2/3−1),ReA≥ReT,

while at port B it is

NuB={NuL,ReB≤ReL(fT,B8)(ReB−1000)PrB1+12.7(fT,B8)1/2(PrB2/3−1),ReB≥ReT,

where:

- *Nu*L is the **Nusselt number for
  laminar flow heat transfer** value specified in the block dialog
  box.
- *Pr*A and
  *Pr*B are the Prandtl numbers at ports
  **A** and **B**.

If the heat transfer specification is set to `Tabulated data —
Colburn data vs. Reynolds number`, the Nusselt number at port
**A** is

NuA=j(ReA,heat)ReA,heatPrA1/3,

while at port **B** it is

NuB=j(ReB,heat)ReB,heatPrB1/3,

where:

- *j*(*Re*A,heat) and *j*(*Re*B,heat) are the Colburn numbers at ports **A** and
  **B**. The block obtains the Colburn numbers from tabulated data
  provided as a function of the Reynolds number.
- *Re*A,heat and
  *Re*B,heat are the Reynolds numbers based on
  the hydraulic diameters for heat transfer calculations at ports **A**
  and **B**. This parameter is defined at port **A** as

  ReA,heat=m˙ADh,heatSMinμA,

  and at port **B** as

  ReB=m˙BDh,heatSMinμB.

If the heat transfer specification is set to `Tabulated data —
Nusselt number vs. Reynolds number and Prandtl number`, the Nusselt number at
port **A** is

NuA=Nu(ReA,heat,PrA),

while at port **B** it is

NuB=Nu(ReB,heat,PrB).

### Hydraulic Diameter Calculations

The hydraulic diameter used in heat transfer calculations can differ from the hydraulic
diameter employed in pressure loss calculations, and are different if the heated and
friction perimeters are not the same. For a concentric pipe heat exchanger with an annular
cross-section, the hydraulic diameter for heat transfer calculations is

Dh,heat=4(π/4)(Do2−Di2)πDi=Do2−Di2Di,

while the hydraulic diameter for pressure calculations is

Dh,p=4(π/4)(Do2−Di2)π(Di+Do)=Do−Di,

where:

- *D*o is the outer annulus diameter.
- *D*i is the inner annulus diameter.

**Annulus Schematic**

The difference between the outer diameter and the inner diameter depicted in orange
represents the thermal liquid. The blue region within the inner diameter is the fluid that
exchanges heat with the thermal liquid.
